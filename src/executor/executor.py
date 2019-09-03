from src.commands.add_profile import AddProfile
from src.commands.current_profile import CurrentProfile
from src.commands.del_profile import DelProfile
from src.commands.destroy_profiles import DestroyProfiles
from src.commands.list_profiles import ListProfiles
from src.commands.show_profile import ShowProfile
from src.commands.update_profile import UpdateProfile
from src.commands.use_profile import UseProfile


def execute_command(args):
    commands = {
        "add": AddProfile,
        "use": UseProfile,
        "del": DelProfile,
        "show": ShowProfile,
        "list": ListProfiles,
        "update": UpdateProfile,
        "current": CurrentProfile,
        "destroy": DestroyProfiles,
    }

    command = commands.get(args.command, None)
    if command:
        instance = command(args)
        print(instance.git_manager.config_file_path)
        instance.execute()
