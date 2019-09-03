from abc import ABC, abstractmethod
from src.git_manager.git_manager import GitManager


class BaseCommand(ABC):
    def __init__(self, args):
        self.args = args
        self.quiet = args.quiet
        self.globally = args.globally

        self.git_manager = GitManager({
            "config": args.file,
            "quiet": args.quiet,
            "globally": args.globally,
        })

    @abstractmethod
    def execute(self):
        """Executes a command using the given arguments"""
