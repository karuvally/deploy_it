#!/usr/bin/env python3
# deploy_it, alpha release
# Copyright 2019, Aswin Babu Karuvally

# import serious stuff
import os
import json
import subprocess
import sys
import logging
import shutil
from distutils.dir_util import copy_tree
import pdb # debug


# execute command
def execute_command(command):
    return_code = subprocess.call(command, shell=True)

    if return_code != 0:
        logging.warning(command + " cannot be executed, exiting")
        sys.exit(1)


# create virtualenv for the app
def create_virtualenv(config):
    # read config
    install_path = config["basics"]["install_path"]
    requirements_file = config["basics"]["requirements_file"]
    requirements_file_path = os.path.join(install_path, requirements_file)

    # create virtualenv
    execute_command("python3 -m venv " + install_path)

    # copy files
    copy_tree("src", os.path.join(install_path, "src"))

    # upgrade pip
    execute_command(install_path + "/bin/pip3 install --upgrade pip")

    # install requirements
    execute_command(
        install_path + "/bin/pip3 install -r " + requirements_file_path
    )


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
        sys.exit(1)

    # install virtualenv
    for command in command_list:
        execute_command(command)


# the main function
def main():
    # setup logging
    format_string = "[%(asctime)s] %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        filename = os.path.join("build.log"),
        level = logging.DEBUG,
        format = format_string,
        datefmt = date_format
    )

    # print logs to stderr
    logging.getLogger().addHandler(logging.StreamHandler())

    # read configuration
    config_file = open("config.json")
    config = config_file.read()
    config = json.loads(config)

    # install virtualenv
    install_virtualenv()
    logging.info("installed virtualenv")

    # create virtualenv
    create_virtualenv(config)
    logging.info("created virtualenv for app")

    # run post install script
    if config["post_install_script"]["enable"]:
        execute_command(config["post_install_script"]["script_file"])

    # setup service
    if config["systemd_service"]["enable"] == True:
        unit_file = config["systemd_service"]["unit_file"]

        if not os.path.isfile(unit_file):
            logging.warning(unit_file + " does not exist, exiting")
            sys.exit(1)

        shutil.copy(unit_file, "/etc/systemd/system")

        # enable  and start service
        execute_command("systemctl enable " + os.path.basename(unit_file))
        execute_command("systemctl start " + os.path.basename(unit_file))
        logging.info(os.path.basename(unit_file) + " is enabled and running")
        logging.info("installation is complete.")

    # add symlink
    if config["symlink"]["enable"]:
        target_path = os.path.join(config["basics"]["install_path"])
        link_path = config["symlink"]["link_path"]

        execute_command("ln -s " + target_path + " " + link_path)
        logging.info("creating symlink to " + link_path)


if __name__ == "__main__":
    main()
