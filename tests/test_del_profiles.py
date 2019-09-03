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
    profiles_to_add = []

    # Generate 10 profiles
    for i in range(10):
        test = "test-local-{0}".format(i)
        profile = Profile(test, test, None, test)
        profiles_to_add.append(profile)

    for p in profiles_to_add:
        git.add_profile(p)

    yield git


class TestDelProfile:
    def test_del_profile_not_found(self, capsys):
        test = "profile-{0}".format(randrange(100000))
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["del", test])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        delmsg = msg.ERR_NO_PROFILE.format(test)

        assert delmsg in out
        assert not err

    def test_del_profile_ok(self, capsys):
        arg_parser = parser.get_arguments_parser()

        for i in range(10):
            test = "test-local-{0}".format(i)
            arguments = arg_parser.parse_args(["del", test])

            executor.execute_command(arguments)
            delmsg = msg.INFO_DEL_SUCCESS.format(test)

            out, err = capsys.readouterr()
            assert delmsg in out
            assert not err
