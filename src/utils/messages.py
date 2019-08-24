HELP_QUIET = "Executes the given command but disables the program output"
HELP_DESTROY = "Deletes all the profiles created using this package"
HELP_DEL = "Delete the given profile from the configuration file"
HELP_MOD = "Update the details of the given profile name"
HELP_VERSION = "Print the version of the current package"
HELP_GLOBAL = "Applies the other commands globally"
HELP_SHOW = "Show the details of the given profile"
HELP_LIST = "List the current available profiles"
HELP_PROFILE = "Tha name of the profile"

HELP_ADD = (
    "Adds a new profile configuration with the given name. The user"
    "will be prompted to input the username, the e-mail (required) "
    "and the signing key (optional)."
)


HELP_USE = (
    "Set the given profile as the active one for the current "
    "project. If the global parameter is specified, the new "
    "profile will be set globally"
)

HELP_CURRENT = (
    "Show the current active configuration for the current project. "
    "If the global parameter is specified, the global configuration "
    "will be returned instead"
)
HELP_CONFIG = (
    "Specify a git config file. If no configuration file is given, "
    "the default=$HOME/.gitconfig will be used; if no configuration "
    "file is found, the command won't be executed"
)

ERR_PROFILE_EXISTS = "[ERROR] The profile {0} exists. Did you mean -u/--update?"
ERR_NO_GITCONFIG = "[ERROR] .gitconfig was not found or is not a valid file"
ERR_RUN_TIMEOUT = "[ERROR] A timeout occurred while running the command"
ERR_RUN_FAILED = "[ERROR] The process returned a non-zero exit status"
ERR_NO_PROFILE = "[ERROR] Profile {0} was not found"

INFO_NO_PROFILES = "No profiles were found. Create one using " "git-profiles -add [NAME]"
INFO_PROFILE_NOSET = "No profile is set. Standard settings are used."
INFO_DESTROY_SUCCESS = "Successfully deleted {0} profiles"
INFO_ADD_SUCCESS = "Successfully created profile {0}:"
INFO_DEL_SUCCESS = "Successfully deleted profile {0}"
INFO_UPD_SUCCESS = "Successfully updated profile {0}"
INFO_PROFILE_CURR_LOC = "Locally active profile:"
INFO_PROFILE_CURR_GLO = "Globally active profile:"
INFO_SWITCH_GLOBALLY = "Switched to {0} globally"
INFO_SWITCH_LOCALLY = "Switched to {0} locally"
INFO_AVAIL_PROFILES = "Available profiles:"

BUILD_SKEY_INPUT = "Enter the profile signing key: "
BUILD_TITLE_INPUT = "Enter the profile title: "
BUILD_REQUIRED = "This parameter is required!"
BUILD_USER_INPUT = "Enter the profile user: "
BUILD_MAIL_INPUT = "Enter the profile mail: "

UPDATE_SKEY_INPUT = "Enter the new signing key ({0}): "
UPDATE_USER_INPUT = "Enter the new user ({0}): "
UPDATE_MAIL_INPUT = "Enter the new mail ({0}): "
