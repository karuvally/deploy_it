#!/usr/bin/env python3
# deploy_it, alpha release
# Copyright 2019, Aswin Babu Karuvally

# import the serious stuff
import json
import shutil
import sys
import os
import logging


# build the deployment archive
def build_archive(config):
    # get configuration
    archive_name = config["archive"]["filename"]
    archive_format = config["archive"]["format"]
    source_dir = config["basics"]["source_dir"]

    # basic checks
    if not os.path.isdir(source_dir):
        print("source directory is not accessible :(")
        sys.exit()

    # copy deployer files
    shutil.copy("config.json", "src")
    shutil.copy("deploy.py", "src")

    # create the archive
    shutil.make_archive(
        base_name = archive_name,
        format = archive_format,
        base_dir = source_dir 
    )


# the main function
def main():
    # setup logging
    format_string = "[%(asctime)s] %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(
        filename = os.path.join(config_dir, "log"),
        level = logging.DEBUG,
        format = format_string,
        datefmt = date_format
    )

    # print logs to stderr
    logging.getLogger().addHandler(logging.StreamHandler())

    # basic checks
    logging.info("initializing deploy_it builder")
    file_list = ["config.json", "deploy.py"]

    for system_file in file_list:
        if not os.path.exists(system_file):
            logging.warning(system_file + "does not exist :(")
            sys.exit()

    # read the configution
    config_file = open("config.json")
    config_string = config_file.read()
    config = json.loads(config_string)


    # build the archive
    build_archive(config)


if __name__ == "__main__":
    main()
