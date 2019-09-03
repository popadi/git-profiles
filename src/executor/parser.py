import argparse
import src.utils.messages as msg
from src.__about__ import __version__


def get_arguments_parser():
    args_parser = argparse.ArgumentParser(description="git-profile usage:")
    args_parser.add_argument("-f", "--file", nargs="?", metavar="PATH", help=msg.HELP_CONFIG)
    args_parser.add_argument("-g", "--globally", action="store_true", help=msg.HELP_GLOBAL)
    args_parser.add_argument("-v", "--version", action="version", version=__version__)
    args_parser.add_argument("-q", "--quiet", action="store_true", help=msg.HELP_QUIET)

    # Initializing the subparser for the commands
    subparser = args_parser.add_subparsers(dest="command")

    # Initialize the non-params commands
    subparser.add_parser("list", help=msg.HELP_LIST)
    subparser.add_parser("current", help=msg.HELP_CURRENT)
    subparser.add_parser("destroy", help=msg.HELP_DESTROY)

    # Initialize the profile-param commands
    add_cmd = subparser.add_parser("add", help=msg.HELP_ADD)
    add_cmd.add_argument("profile", nargs=1, metavar="PROFILE", help=msg.HELP_PROFILE)

    use_cmd = subparser.add_parser("use", help=msg.HELP_USE)
    use_cmd.add_argument("profile", nargs=1, metavar="PROFILE", help=msg.HELP_PROFILE)

    del_cmd = subparser.add_parser("del", help=msg.HELP_DEL)
    del_cmd.add_argument("profile", nargs=1, metavar="PROFILE", help=msg.HELP_PROFILE)

    mod_cmd = subparser.add_parser("update", help=msg.HELP_MOD)
    mod_cmd.add_argument("profile", nargs=1, metavar="PROFILE", help=msg.HELP_PROFILE)

    show_cmd = subparser.add_parser("show", help=msg.HELP_SHOW)
    show_cmd.add_argument("profile", nargs=1, metavar="PROFILE", help=msg.HELP_PROFILE)

    return args_parser
