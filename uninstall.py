#!/usr/bin/env python3
# deploy_it uninstall script
# Copyright 2019, Aswin Babu Karuvally

# import serious stuff
import os
import logging

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


# call the main function
if __name__ == "__main__":
    main()

