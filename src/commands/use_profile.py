from src.commands.base_command import BaseCommand
import src.utils.messages as msg


class UseProfile(BaseCommand):
    def execute(self):
        """
        Sets the given profile name as the active one, if it exists.
        By default, it is set for the current project. If the global
        parameter is given, it will be set globally.
        """
        profile_name = self.args.profile[0]
        if not self.git_manager.check_profile_exist(profile_name):
            if not self.quiet:
                print(msg.ERR_NO_PROFILE.format(profile_name))
            return

        # Get the details of the profile
        full_name = "profile.{0}".format(profile_name)
        profile = self.git_manager.get_profile(full_name)

        # Set the profile
        self.git_manager.set_profile(profile, self.args.globally)
        if not self.quiet:
            if self.args.globally:
                print(msg.INFO_SWITCH_GLOBALLY.format(profile_name))
            else:
                print(msg.INFO_SWITCH_LOCALLY.format(profile_name))
