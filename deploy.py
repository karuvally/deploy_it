#!/usr/bin/env python3
# deploy_it, alpha release
# Copyright 2019, Aswin Babu Karuvally

# import serious stuff
import os
import pdb # debug

# install virtualenv
def install_virtualenv():
    # get the distribution name
    distro = os.popen("lsb_release -i")
    distro = distro.read().rstrip()
    distro = distro.split()[2]

    # read distro specific info
    install_cmd_file = open("install_venv.json")

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
