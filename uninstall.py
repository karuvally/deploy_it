#!/usr/bin/env python3
# deploy_it uninstall script
# Copyright 2019, Aswin Babu Karuvally

# import serious stuff
import os
import logging
import json

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

    # check if user is root
    if os.getuid() != 0:
        logging.critical("Script cannot be run as normal user, exiting")
        sys.exit(1)

    # read configuration
    config_file = open("config.json")
    config = config_file.read()
    config = json.loads(config)


# call the main function
if __name__ == "__main__":
    main()

