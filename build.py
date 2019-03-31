#!/usr/bin/env python3
# deploy_it, alpha release
# Copyright 2019, Aswin Babu Karuvally

# import the serious stuff
import json
import shutil
import sys


# build the deployment archive
def build_archive(config):
    if not os.path.isdir(config["basics"]["source_dir"]):
        print("source directory is not accessible :(")
        sys.exit()


# the main function
def main():
    # read the configution
    if not os.path.exists("config.json"):
        print("it seems config.json is missing :(")
        sys.exit()

    config_file = open("config.json")
    config = json.loads(config_file)


    # build the archive
    build_archive(config)


if __name__ == "__main__":
    main()
