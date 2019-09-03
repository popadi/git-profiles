import src.utils.messages as msg
from src.commands.base_command import BaseCommand


class CurrentProfile(BaseCommand):
    def execute(self):
        """
        The command tries to get a previously set profile and to print
        its details. A profile may be set either globally or locally
        for a project. The `-g/--global` parameter is used to specify
        how the search should be made.
        """
        # Get the current set profile by this package
        current = self.git_manager.get_current(self.args.globally)

        if current:
            full_name = "profile.{0}".format(current)
            profile = self.git_manager.get_profile(full_name)

            if self.args.globally:
                print(msg.INFO_PROFILE_CURR_GLO)
            else:
                print(msg.INFO_PROFILE_CURR_LOC)
        else:
            print(msg.INFO_PROFILE_NOSET)
            return

        print(profile)
