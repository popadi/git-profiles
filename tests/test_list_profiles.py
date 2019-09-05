import os
import sys
import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")

import src.utils.messages as msg
from src.executor import executor, parser
from src.git_manager.git_manager import GitManager
from src.profile.profile import Profile


@pytest.fixture(autouse=True)
def prepare():
    with open(".test-config", "w+"):
        pass

    git = GitManager({"config": ".test-config"})
    loc = "test_current_locally"
    glb = "test_current_globally"

    # Generate two profiles to test for active locally/globally
    profiles_to_add = [Profile(loc, loc, loc, loc), Profile(glb, glb, glb, glb)]

    # Generate 10 profiles
    for i in range(10):
        test = "test-local-{0}".format(i)
        profile = Profile(test, test, None, test)
        profiles_to_add.append(profile)

    for p in profiles_to_add:
        git.add_profile(p)

    yield git, loc, glb

    os.remove(".test-config")


class TestListProfiles:
    def test_no_profiles(self, capsys):
        fake_config = "./fake_config"
        with open(fake_config, "w+") as f:
            pass

        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["-f", fake_config, "list"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert msg.INFO_NO_PROFILES in out

        try:
            os.remove(fake_config)
        except OSError:
            pass

    def test_list_profiles(self, capsys):
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["-f", "./.test-config", "list"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert msg.INFO_AVAIL_PROFILES in out

        for i in range(10):
            test = "test-local-{0}".format(i)
            assert test in out

    def test_list_active(self, capsys):
        arg_parser = parser.get_arguments_parser()

        arguments = arg_parser.parse_args(["-gf", "./.test-config", "use", "test_current_globally"])
        executor.execute_command(arguments)

        arguments = arg_parser.parse_args(["-f", "./.test-config", "use", "test_current_locally"])
        executor.execute_command(arguments)

        arguments = arg_parser.parse_args(["-f", "./.test-config", "list"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert "test_current_globally <-- active globally" in out
        assert "test_current_locally <-- active locally" in out
        assert not err
