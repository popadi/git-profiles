import src.utils.messages as msg
from src.commands.base_command import BaseCommand


class ListProfiles(BaseCommand):
    def execute(self) -> None:
        """Lists the available git-profile profiles."""

        # Try to get the locally and globally active profiles
        active_local = self.git_manager.get_current(False)
        active_global = self.git_manager.get_current(True)

        # Gather the existing profiles
        available_profiles = self.git_manager.list_profiles()

        if len(available_profiles) == 0:
            print(msg.INFO_NO_PROFILES)
            return

        print(msg.INFO_AVAIL_PROFILES)
        for profile in available_profiles:
            active = []
            if profile == active_local:
                active.append("locally")

            if profile == active_global:
                active.append("globally")

            status = ""
            if len(active) > 0:
                status = " <-- active " + ", ".join(active)
            print("\t{0}{1}".format(profile, status))
