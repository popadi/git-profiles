import src.utils.messages as msg
from src.commands.base_command import BaseCommand
from src.profile.profile import Profile


class AddProfile(BaseCommand):
    def execute(self) -> None:
        """
        Add a new profile to the configuration file. If there is
        already a profile with the given name, the process will
        not be executed, since the update must be used.
        """
        profile_name = self.args.profile[0]
        if self.git_manager.check_profile_exist(profile_name):
            if not self.quiet:
                print(msg.ERR_PROFILE_EXISTS.format(profile_name))
            return

        profile = Profile.build_profile(profile_name)
        self.git_manager.add_profile(profile)

        if not self.quiet:
            print(msg.INFO_ADD_SUCCESS.format(profile_name))
            print(profile)
