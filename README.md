<div align="center">
    <h1 align="center">👥 git-profile</h1>
    <p align="center">Python package that helps you easily manage and switch between multiple git configurations</p>
    <p align="center">
        <a href="https://github.com/popadi/git-profile">
            <img src="https://travis-ci.com/popadi/git-profile.svg?branch=master" alt="Build">
            <img src="https://coveralls.io/repos/github/popadi/git-profile/badge.svg?branch=master&service=github">
            <img src="https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square" alt="Software License">
        </a>
    </p>
</div>

# About
Soon

# Install
Soon

# Usage
```
usage: git_profile.py [-h] [-f [PATH]] [-g] [-v] [-q]
                      {list,current,destroy,add,use,del,update,show} ...

git-profile usage:

positional arguments:
  {list,current,destroy,add,use,del,update,show}
    list                List the current available profiles
    current             Show the current active configuration for the current
                        project. If the global parameter is specified, the
                        global configuration will be returned instead
    destroy             Deletes all the profiles created using this package
    add                 Adds a new profile configuration with the given name.
                        The userwill be prompted to input the username, the
                        e-mail (required) and the signing key (optional).
    use                 Set the given profile as the active one for the
                        current project. If the global parameter is specified,
                        the new profile will be set globally
    del                 Delete the given profile from the configuration file
    update              Update the details of the given profile name
    show                Show the details of the given profile

optional arguments:
  -h, --help            show this help message and exit
  -f [PATH], --config-file [PATH]
                        Specify a git config file. If no configuration file is
                        given, the default=$HOME/.gitconfig will be used; if
                        no configuration file is found, the command won't be
                        executed
  -g, --globally        Applies the other commands globally
  -v, --version         show program's version number and exit
  -q, --quiet           Executes the given command but disables the program
                        output
```

# Examples
Soon

# License
MIT © 2019 Pop Adrian
