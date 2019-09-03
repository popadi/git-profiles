import os
import sys
import pytest
from random import randrange

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")

from src.git_manager.git_manager import GitManager
from src.executor import executor, parser
from src.profile.profile import Profile
import src.utils.messages as msg


@pytest.fixture(autouse=True)
def prepare():
    git = GitManager()
    profiles_to_add = []

    # Generate 10 profiles
    for i in range(10):
        test = "test-local-{0}".format(i)
        profile = Profile(test, test, test, test)
        profiles_to_add.append(profile)

    for p in profiles_to_add:
        git.add_profile(p)

    yield git

    # Delete the added profiles
    for p in profiles_to_add:
        git.del_profile("profile.{0}".format(p.profile_name))


class TestShowProfile:
    def test_invalid_config(self, capsys):
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["-f", "/abc/xyz/pqr/def", "list"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert not err
        assert msg.ERR_NO_GITCONFIG in out

    def test_show_ok(self, capsys):
        for i in range(10):
            test = "test-local-{0}".format(i)
            arg_parser = parser.get_arguments_parser()
            arguments = arg_parser.parse_args(["show", test])
            executor.execute_command(arguments)

            out, err = capsys.readouterr()
            assert not err
            assert "Name: {0}".format(test) in out
            assert "Mail: {0}".format(test) in out
            assert "Signing key: {0}".format(test) in out

    def test_show_exists(self, capsys):
        arg_parser = parser.get_arguments_parser()
        fake_profile = "profile-{0}".format(randrange(100000))

        arguments = arg_parser.parse_args(["show", fake_profile])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        fail_mesg = msg.ERR_NO_PROFILE.format(fake_profile)

        assert fail_mesg in out
        assert not err
