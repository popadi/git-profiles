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

    profiles_to_add = []
    git = GitManager({
        "config": ".test-config"
    })

    for i in range(10):
        test = "test-local-{0}".format(i)
        profile = Profile(test, test, None, test)
        profiles_to_add.append(profile)

    for p in profiles_to_add:
        git.add_profile(p)

    yield git

    os.remove(".test-config")


class TestListProfiles:
    def test_destroy_profiles(self, capsys):
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["-f", "./.test-config", "destroy"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert not err
        assert msg.INFO_DESTROY_SUCCESS.format(10) in out
