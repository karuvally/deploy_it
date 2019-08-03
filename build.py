#!/usr/bin/env python3
# deploy_it, alpha release
# Copyright 2019, Aswin Babu Karuvally

# import the serious stuff
import json
import shutil
import sys
import os
import logging
from distutils.dir_util import copy_tree
import pdb # debug


# stuff to check before starting process
def init_checks(config, file_list):
    for system_file in file_list:
        if not os.path.exists(system_file):
            logging.critical(system_file + " does not exist, exiting...")
            sys.exit(1)

    # config script specific checks
    if config["systemd_service"]["enable"] == True:
        unit_file = config["systemd_service"]["unit_file"]
        if not os.path.exists(unit_file):
            logging.critical(unit_file + " does not exist, exiting...")
            sys.exit(1)

    if config["post_install_script"]["enable"]:
        script_file = config["post_install_script"]["script_file"]
        if not os.path.exists(script_file):
            logging.critical(script_file + " does not exist, exiting...")


def setup_logging():
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


# build the deployment archive
def build_archive(config, file_list):
    # get configuration
    archive_name = config["archive"]["filename"]
    archive_format = config["archive"]["format"]
    source_dir = config["basics"]["source_dir"]

    # basic checks
    if not os.path.isdir(source_dir):
        logging.warning("source directory is not accessible, exiting...")
        sys.exit()

    if os.path.isdir(os.path.join(source_dir, ".git")):
        shutil.rmtree(os.path.join(source_dir, ".git"))

    # copy files
    os.mkdir(archive_name)
    for file_path in file_list:
        shutil.copy(file_path, archive_name)
    copy_tree("src", archive_name + "/src")

    # create archive
    shutil.make_archive(
        base_name = archive_name,
        format = archive_format,
        base_dir = archive_name 
    )

    # cleanup and exit
    shutil.rmtree(archive_name)
    logging.info(archive_name + "." + archive_format + " is built")


# the main function
def main():
    # check if the current dir is writable
    if not os.access("./", os.W_OK):
        print("current directory is not writable, exiting...")
        sys.exit(1)

    # essential stuff
    setup_logging()
    logging.info("initializing deploy_it builder")
    file_list = [
        "deploy.py",
        "install_venv.json",
        "uninstall.py",
        "config.json"
    ]

    if not os.path.exists("config.json"):
        logging.critical("config.json does not exist, exiting...")
        sys.exit(1)

    # read the configution
    with open("config.json") as config_file:
        config = config_file.read()
        config = json.loads(config)

    # do the initial checks
    init_checks(config, file_list)

    # build the archive
    build_archive(config, file_list)


if __name__ == "__main__":
    main()
