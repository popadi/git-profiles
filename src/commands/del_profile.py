import src.utils.messages as msg
from src.commands.base_command import BaseCommand


class DelProfile(BaseCommand):
    def execute(self):
        """
        Delete a profile from the configuration file. If there
        isn't a profile with the given name, the user will be
        alerted.
        """
        if not self.git_manager.has_valid_config():
            return

        # Check if the profile exists
        profile_name = self.args.profile[0]
        if not self.git_manager.check_profile_exist(profile_name):
            if not self.quiet:
                print(msg.ERR_NO_PROFILE.format(profile_name))
            return

        full_profile = "profile.{0}".format(profile_name)
        self.git_manager.del_profile(full_profile)

        if self.quiet:
            return
        print(msg.INFO_DEL_SUCCESS.format(profile_name))
