from src.commands.base_command import BaseCommand
from src.__about__ import __version__


class ShowVersion(BaseCommand):
    def execute(self):
        print("git-profile {0}".format(__version__))
