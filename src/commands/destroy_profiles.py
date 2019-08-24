import src.utils.messages as msg
from src.commands.base_command import BaseCommand


class DestroyProfiles(BaseCommand):
    def execute(self):
        """Lists the available git-profile profiles."""
        if not self.git_manager.has_valid_config():
            return

        # Gather the existing profiles
        available_profiles = self.git_manager.list_profiles()

        # Delete all of them
        for profile in available_profiles:
            full_name = "profile.{0}".format(profile)
            self.git_manager.del_profile(full_name)

        # Delete the current profile entry
        self.git_manager.del_profile("current-profile")

        if not self.quiet:
            print(msg.INFO_DESTROY_SUCCESS.format(len(available_profiles)))
