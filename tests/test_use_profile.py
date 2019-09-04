import os
import sys
import pytest
from random import randrange

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")

import src.utils.messages as msg
from src.executor import executor, parser
from src.git_manager.git_manager import GitManager


@pytest.fixture(autouse=True)
def prepare():
    git = GitManager({})
    yield git


class TestListProfiles:
    def test_use_not_exist(self, capsys):
        arg_parser = parser.get_arguments_parser()

        # Set an account locally
        fake_profile = "profile-{0}".format(randrange(100000))
        arguments = arg_parser.parse_args(["use", fake_profile])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert not err
        assert msg.ERR_NO_PROFILE.format(fake_profile) in out
