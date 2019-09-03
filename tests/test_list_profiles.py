import os
import sys
import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.git_manager.git_manager import GitManager
from src.executor import executor, parser
from src.profile.profile import Profile
import src.utils.messages as msg


@pytest.fixture(autouse=True)
def prepare():
    git = GitManager({})
    profiles_to_add = []

    # Generate 10 profiles
    for i in range(10):
        test = "test-local-{0}".format(i)
        profile = Profile(test, test, None, test)
        profiles_to_add.append(profile)

    for p in profiles_to_add:
        git.add_profile(p)

    yield git

    # Delete the added profiles
    for p in profiles_to_add:
        git.del_profile("profile.{0}".format(p.profile_name))


class TestListProfiles:
    def test_invalid_config(self, capsys):
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["-f", "/abc/xyz/pqr/def", "list"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert not out
        assert not err

    def test_no_profiles(self, capsys):
        fake_config = "./fake_config"
        with open(fake_config, 'w+') as f:
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
        arguments = arg_parser.parse_args(["list"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert msg.INFO_AVAIL_PROFILES in out

        for i in range(10):
            test = "test-local-{0}".format(i)
            assert test in out
