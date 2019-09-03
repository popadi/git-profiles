import io
import os
import sys
import pytest
from random import randrange

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")

import src.utils.messages as msg
from src.executor import executor, parser
from src.git_manager.git_manager import GitManager
from src.profile.profile import Profile


@pytest.fixture(autouse=True)
def prepare():
    git = GitManager({})
    test = "test-update-profile"

    profile = Profile(test, test, None, test)
    git.add_profile(profile)

    yield git

    git.del_profile("profile.{0}".format(profile.profile_name))


class TestAddProfile:
    def test_update_profile_ok(self, capsys, monkeypatch):
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["update", "test-update-profile"])

        fake_input = io.StringIO("\n".join(["something-else"] * 3))
        monkeypatch.setattr("sys.stdin", fake_input)
        executor.execute_command(arguments)
        out, err = capsys.readouterr()

        assert msg.INFO_UPD_SUCCESS.format("test-update-profile") in out
        assert not err

    def test_update_profile_not_exist(self, capsys):
        test = "profile-{0}".format(randrange(100000))
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["update", test])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        delmsg = msg.ERR_NO_PROFILE.format(test)

        assert delmsg in out
        assert not err
