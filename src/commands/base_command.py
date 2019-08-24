from abc import ABC, abstractmethod
from src.git_manager.git_manager import GitManager


class BaseCommand(ABC):
    def __init__(self, args):
        self.args = args
        self.quiet = args.quiet
        self.git_manager = GitManager(config_file_path=self.args.config_file, quiet=args.quiet)

    @abstractmethod
    def execute(self):
        """Executes a command using the given arguments"""
