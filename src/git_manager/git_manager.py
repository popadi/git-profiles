from os.path import expanduser, isfile
from re import search
from subprocess import PIPE, CalledProcessError, TimeoutExpired, run
from sys import exit

import src.utils.messages as msg
from src.profile.profile import Profile, P


class GitManager:
    cfg_global_cmd = ["git", "config", "--global"]
    cfg_local_cmd = ["git", "config"]

    def __init__(self, config: dict) -> None:
        self.config_file_path = config.get("config", None)
        self.globally = config.get("globally", False)
        self.quiet = config.get("quiet", False)
        self.config_command_prefix = []
        self.initialize()

    def initialize(self) -> None:
        """
        Initialize the git manager with a configuration file. If
        no configuration file is given, try to open the default
        one in the home folder. If it doesn't exist, try to create
        it or exit if any error occurs.
        """
        config_file_path = None

        if not self.config_file_path:
            try:
                default = "{0}/.gpconfig".format(expanduser("~"))
                with open(default, "a+"):
                    pass
                config_file_path = default
            except IOError as e:
                exit(e.returncode)
        else:
            if isfile(self.config_file_path):
                config_file_path = self.config_file_path
            else:
                if not self.quiet:
                    print(msg.ERR_NO_GITCONFIG.format(self.config_file_path))
                exit(-1)

        if config_file_path:
            self.config_command_prefix = ["git", "config", "-f", config_file_path]
            self.config_file_path = config_file_path

    def run_command(self, cmd: list) -> str:
        """
        Run the given shell command. If an error or a timeout occurs,
        the program will exit with an appropriate exit code.
        :param cmd: command to be run as an array
        """
        try:
            result = run(cmd, stdout=PIPE)
            return result.stdout.decode("utf-8")
        except TimeoutExpired:
            if not self.quiet:
                print(msg.ERR_RUN_TIMEOUT)
            exit(-1)
        except CalledProcessError as e:
            if not self.quiet:
                print(msg.ERR_RUN_FAILED)
            exit(e.returncode)

    def check_profile_exist(self, profile_name: str) -> bool:
        """
        Check if the given profile exists in the config file.
        :return: boolean representing the checking answer.
        """
        command = [*self.config_command_prefix, "--list"]
        properties = self.run_command(command)

        if not properties:
            return False

        identifier = "profile.{0}".format(profile_name)
        return identifier in properties

    def get_profile(self, profile_name: str = "user") -> P:
        """
        Given the name of a profile, return an instance of a Profile
        with all its details (username, email, signing key).
        :param profile_name:
        :return:
        """
        user = self.run_command([*self.config_command_prefix, profile_name + ".name"])
        mail = self.run_command([*self.config_command_prefix, profile_name + ".email"])
        skey = self.run_command([*self.config_command_prefix, profile_name + ".signingkey"])

        profile = Profile(user, mail, skey, profile_name)
        return profile

    def set_profile(self, profile: P, globally: bool = False) -> None:
        """
        Set the given profile as being active either locally or globally.
        :param profile: profile to be used to set the required fields
        :param globally: boolean representing the setting mode
        """
        # Get the right prefix for the command
        cmd_prefix = self.cfg_global_cmd if globally else self.cfg_local_cmd

        # Run the commands to set the new active profile
        self.run_command([*cmd_prefix, "user.name", profile.user])
        self.run_command([*cmd_prefix, "user.email", profile.mail])
        if profile.skey:
            self.run_command([*cmd_prefix, "user.signingkey", profile.skey])

        # Update the current-profile entry in the config file
        current = "current-profile-{0}.name".format("globally" if globally else "locally")
        self.run_command([*self.config_command_prefix, current, profile.profile_name])

    def add_profile(self, profile: P) -> None:
        """
        Run the necessary commands to add a new profile.
        :param profile: profile details to be added.
        """
        # Set up placeholder and profile title/name
        pn = profile.profile_name
        ph = "profile.{0}.{1}"

        self.run_command([*self.config_command_prefix, ph.format(pn, "name"), profile.user])
        self.run_command([*self.config_command_prefix, ph.format(pn, "email"), profile.mail])
        if profile.skey:
            self.run_command(
                [*self.config_command_prefix, ph.format(pn, "signingkey"), profile.skey]
            )

    def del_profile(self, profile_name: str) -> None:
        """
        Deletes a section from the configuration file. In this case, the
        method deletes the section associated with a previously created
        profile, using this package.
        :param profile_name: the name of the profile to be deleted.
        """
        command = [*self.config_command_prefix, "--remove-section", profile_name]
        self.run_command(command)

    def list_profiles(self) -> list:
        """
        Return the name of all the profiles created using this package.
        :return: list containing the name of previously created profiles.
        """
        pattern = r"\[profile \"(.*?)\"\]"
        available_profiles = []

        with open(self.config_file_path) as gitconfig:
            for line in gitconfig.readlines():
                match = search(pattern, line)
                if match:
                    available_profiles.append(match.group(1))

        return available_profiles

    def get_current(self, globally: bool = False) -> str:
        """
        Get the current set profile by this package.
        :param globally: boolean representing the get mode
        :return: name of the current profile or empty string
        """
        current = "current-profile-{0}.name".format("globally" if globally else "locally")
        command = [*self.config_command_prefix, current]
        return self.run_command(command).strip()
