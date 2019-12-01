#!/usr/bin/env python3
import json
import requests


def main():
    """
    This is the main entry point

    :return:
    """
    with open("config.json", 'r') as file:
        config = json.load(file)

    # First we need to get our public IP address
    ip_data = requests.get(url='https://api.ipify.org?format=json').json()

    # And now update OVH
    dynhost_url = "https://www.ovh.com/nic/update?system=dyndns&hostname={0}&myip={1}".format(config["dyn_fqdn"], ip_data["ip"])
    requests.get(dynhost_url, auth=requests.auth.HTTPBasicAuth(config["username"], config["password"]))


# Start us of in main
if __name__ == "__main__":
    main()
