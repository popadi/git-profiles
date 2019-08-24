import os
import sys
import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.git_manager.git_manager import GitManager
from src.executor import executor, parser
from src.profile.profile import Profile


@pytest.fixture(autouse=True)
def prepare():
    git = GitManager()

    # Create profiles
    local_profile = Profile("test-local", "test@local.com", None, "test-local")
    global_profile = Profile("test-global", "test@global.com", None, "test-global")

    # Add profiles
    git.add_profile(local_profile)
    git.add_profile(global_profile)

    # Set them
    git.set_profile(local_profile)
    git.set_profile(global_profile, True)

    yield git, local_profile, global_profile

    # Delete them
    git.del_profile("profile.{0}".format(local_profile.profile_name))
    git.del_profile("profile.{0}".format(global_profile.profile_name))


class TestCurrentProfile:
    def test_current_profile_locally(self, prepare, capsys):
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["current"])

        executor.execute_command(arguments)
        manager, local_profile, _ = prepare

        out, err = capsys.readouterr()
        assert "test-local" in out

    def test_current_profile_globally(self, prepare, capsys):
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["-g", "current"])

        executor.execute_command(arguments)
        manager, local_profile, _ = prepare

        out, err = capsys.readouterr()
        assert "test-global" in out
