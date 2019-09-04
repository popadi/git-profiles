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

    git.add_profile(Profile(loc, loc, loc, loc))
    git.add_profile(Profile(glb, glb, glb, glb))

    yield git, loc, glb

    os.remove(".test-config")


class TestListProfiles:
    def test_current_locally(self, capsys, prepare):
        arg_parser = parser.get_arguments_parser()

        # Set an account locally
        arguments = arg_parser.parse_args(["-f", "./.test-config", "use", "test_current_locally"])
        executor.execute_command(arguments)

        # Check if set
        arguments = arg_parser.parse_args(["-f", "./.test-config", "current"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert not err
        assert str(prepare[1]) in out
        assert msg.INFO_PROFILE_CURR_LOC in out

    def test_current_globally(self, capsys, prepare):
        arg_parser = parser.get_arguments_parser()

        # Set an account globally
        arguments = arg_parser.parse_args(["-gf", "./.test-config", "use", "test_current_globally"])
        executor.execute_command(arguments)

        # Check if set
        arguments = arg_parser.parse_args(["-gf", "./.test-config", "current"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert not err
        assert str(prepare[2]) in out
        assert msg.INFO_PROFILE_CURR_GLO in out

    def test_current_not_set(self, capsys):
        # Empty the configuration file
        with open(".test-config", "w"):
            pass

        # Check if set
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["-f", "./.test-config", "current"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert not err
        assert msg.INFO_PROFILE_NOSET in out
