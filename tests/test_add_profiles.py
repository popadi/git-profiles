import io
import os
import sys
import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")

from src.git_manager.git_manager import GitManager
from src.executor import executor, parser
from src.profile.profile import Profile
import src.utils.messages as msg


@pytest.fixture(autouse=True)
def prepare():
    git = GitManager()
    yield git


class TestAddProfile:
    def test_invalid_config(self, capsys):
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["-qf", "/abc/xyz/pqr/def", "add", "test"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert not out
        assert not err

    def test_add_profile_ok(self, capsys, monkeypatch):
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["add", "test_add_profile_ok"])

        fake_input = io.StringIO("\n".join(["test_add_profile_ok"] * 3))
        monkeypatch.setattr("sys.stdin", fake_input)
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert not err
        assert msg.BUILD_USER_INPUT in out
        assert msg.BUILD_MAIL_INPUT in out
        assert msg.BUILD_SKEY_INPUT in out

        success = msg.INFO_ADD_SUCCESS.format("test_add_profile_ok")
        assert success in out

        arguments = arg_parser.parse_args(["del", "test_add_profile_ok"])
        executor.execute_command(arguments)
        out, err = capsys.readouterr()

        delmsg = msg.INFO_DEL_SUCCESS.format("test_add_profile_ok")
        assert delmsg in out
        assert not err

    def test_add_profile_exists(self, capsys, monkeypatch):
        # Add a test profile
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["add", "test_add_profile_ok"])
        fake_input = io.StringIO("\n".join(["test_add_profile_ok"] * 3))
        monkeypatch.setattr("sys.stdin", fake_input)
        executor.execute_command(arguments)

        # Try to add it again
        arguments = arg_parser.parse_args(["add", "test_add_profile_ok"])
        executor.execute_command(arguments)

        # Check if the error message was displayed
        out, err = capsys.readouterr()
        errmsg = msg.ERR_PROFILE_EXISTS.format("test_add_profile_ok")
        assert errmsg in out
        assert not err

        # Delete the test profile
        arguments = arg_parser.parse_args(["del", "test_add_profile_ok"])
        executor.execute_command(arguments)
        out, err = capsys.readouterr()

        delmsg = msg.INFO_DEL_SUCCESS.format("test_add_profile_ok")
        assert delmsg in out
        assert not err

    def test_add_profile_quiet(self, capsys, monkeypatch):
        arg_parser = parser.get_arguments_parser()
        arguments = arg_parser.parse_args(["-q", "add", "test_add_profile_ok"])

        fake_input = io.StringIO("\n".join(["test_add_profile_ok"] * 3))
        monkeypatch.setattr("sys.stdin", fake_input)
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        success = msg.ERR_PROFILE_EXISTS.format("test_add_profile_ok")
        assert success not in out
        assert not err

        arguments = arg_parser.parse_args(["-q", "del", "test_add_profile_ok"])
        executor.execute_command(arguments)

        out, err = capsys.readouterr()
        assert not out
        assert not err
