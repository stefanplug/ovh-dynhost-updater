#!/usr/bin/env python3
import requests
from functions.json_functions import load_json


def main():
    """
    This is the main entry point

    :return:
    """
    config = load_json("config.json")

    # First we need to get our public IP address
    ip_data = requests.get(url='https://api.ipify.org?format=json').json()

    # And now update OVH
    dynhost_url = "https://www.ovh.com/nic/update?system=dyndns&hostname={0}&myip={1}".format(config["dyn_fqdn"], ip_data["ip"])
    requests.get(dynhost_url, auth=requests.auth.HTTPBasicAuth(config["username"], config["password"]))


# Start us of in main
if __name__ == "__main__":
    main()
