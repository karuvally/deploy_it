#!/usr/bin/env python3
# deploy_it, alpha release
# Copyright 2019, Aswin Babu Karuvally

# import the serious stuff
import json
import shutil
import sys
import os


# build the deployment archive
def build_archive(config):
    # basic checks
    if not os.path.isdir(config["basics"]["source_dir"]):
        print("source directory is not accessible :(")
        sys.exit()


# the main function
def main():
    # basic checks
    if not os.path.exists("config.json"):
        print("it seems config.json is missing :(")
        sys.exit()

    # read the configution
    config_file = open("config.json")
    config_string = config_file.read()
    config = json.loads(config_string)


    # build the archive
    build_archive(config)


if __name__ == "__main__":
    main()
