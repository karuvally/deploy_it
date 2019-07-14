#!/usr/bin/env python3
# deploy_it uninstall script
# Copyright 2019, Aswin Babu Karuvally

# import serious stuff
import os
import logging
import json


# execute command
def execute_command(command):
    return_code = subprocess.call(command, shell=True)

    if return_code != 0:
        logging.warning(command + " cannot be executed, exiting")
        sys.exit(1)


# remove symlink
def remove_symlink(config):
    if not config["symlink"]["enable"]:
        return

    link_path = os.path.join(config["symlink"]["link_path"])
    execute_command("rm " + link_path)
    logging.info("removed symlink at " + link_path)


# setup logging
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


    # stop and remove service
    def remove_service(config):
        if not config["systemd_service"]["enable"]:
            return

        unit_file = config["systemd_service"]["unit_file"]
        execute_command("systemctl stop " + os.path.basename(unit_file))
        execute_command("systemctl disable " + os.path.basename(unit_file))
        execute_command("rm /etc/systemd/system" + unit_file)

        logging.info("removed service")


# the main function
def main():
    # setup logging
    setup_logging()

    # check if user is root
    if os.getuid() != 0:
        logging.critical("Script cannot be run as normal user, exiting")
        sys.exit(1)

    # read configuration
    config_file = open("config.json")
    config = config_file.read()
    config = json.loads(config)
    config_file.close()

    # remove symlink
    remove_symlink(config)

    # remove service
    remove_service(config)


# call the main function
if __name__ == "__main__":
    main()

