#!/usr/bin/env python3
# deploy_it, alpha release
# Copyright 2019, Aswin Babu Karuvally

# import the serious stuff
import json
import shutil


# build the deployment archive
def build_archive(config):
    pass


# the main function
def main():
    # read the configution
    if os.path.exists("config.json"):
        config_file = open("config.json")
        config = json.loads(config_file)
    else:
        print("it seems config.json is missing :(")

    # build the archive
    build_archive(config)


if __name__ == "__main__":
    main()
