#!/usr/bin/env python3
# deploy_it, alpha release
# Copyright 2019, Aswin Babu Karuvally

# import serious stuff
import os
import json
import pdb # debug

# install virtualenv
def install_virtualenv():
    # get the distribution name
    distro = os.popen("lsb_release -i")
    distro = distro.read().rstrip()
    distro = distro.split()[2]

    # read distro specific info
    install_cmd_file = open("install_venv.json")
    install_cmd_string = install_cmd_file.read()
    install_cmds = json.loads(install_cmd_string)

    if distro in install_cmds:
        command_list = install_cmds[distro]
    else:
        logging.warning("virtualenv cannot be installed, exiting")

    # install virtualenv
    pass


# the main function
def main():
    # install virtualenv
    install_virtualenv()

    # create virtualenv
    # copy the files
    # install requirements
    # setup service
    pass


if __name__ == "__main__":
    main()
