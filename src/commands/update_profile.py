import src.utils.messages as msg
from src.commands.base_command import BaseCommand
from src.profile.profile import Profile


class UpdateProfile(BaseCommand):
    def execute(self):
        """
        Add a new profile to the configuration file. If there is
        already a profile with the given name, the process will
        not be executed, since the update must be used.
        """
        profile_name = self.args.profile[0]
        if not self.git_manager.check_profile_exist(profile_name):
            if not self.quiet:
                print(msg.ERR_NO_PROFILE.format(profile_name))
            return

        full_profile = "profile.{0}".format(profile_name)
        profile = self.git_manager.get_profile(full_profile)

        profile.update_profile()
        self.git_manager.add_profile(profile)

        if not self.quiet:
            print(msg.INFO_UPD_SUCCESS.format(profile_name))
            print(profile)
