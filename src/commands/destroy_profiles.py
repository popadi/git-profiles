import src.utils.messages as msg
from src.commands.base_command import BaseCommand


class DestroyProfiles(BaseCommand):
    def execute(self) -> None:
        """Lists the available git-profiles profiles."""
        # Gather the existing profiles
        available_profiles = self.git_manager.list_profiles()

        # Delete all of them
        for profile in available_profiles:
            full_name = "profile.{0}".format(profile)
            self.git_manager.del_profile(full_name)

        if not self.quiet:
            print(msg.INFO_DESTROY_SUCCESS.format(len(available_profiles)))
