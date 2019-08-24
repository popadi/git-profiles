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
    git = GitManager()
    local_profile = Profile("test-local", "test@local.com", None, "test-local")
    global_profile = Profile("test-global", "test@global.com", None, "test-global")

    git.add_profile(local_profile)
    git.add_profile(global_profile)

    yield git

    git.del_profile("profile.{0}".format(local_profile.profile_name))
    git.del_profile("profile.{0}".format(global_profile.profile_name))


class TestListProfiles:
    def test_list_profiles(self, capsys):
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["list"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert msg.INFO_AVAIL_PROFILES in out
        assert "test-global" in out
        assert "test-local" in out
