import json
import sys
import os
import random

import switch_vpn


def main():
    root = os.path.dirname(__file__) + os.sep + 'confs' + os.sep

    # parsing passed args for which vpn folder to use, and which country inside that folder to use
    if len(sys.argv) <3:
        if len(sys.argv) == 1:
            print("expected args vpn, country")
            return
        else:
            with open(root + 'default_vpn.txt') as f:
                vpn = f.readline()
                country = sys.argv[1]
    else:
        vpn = sys.argv[1]
        country = sys.argv[2]

    # check country input against valid input by loading the vpn's country:configurations hashmap
    with open(root + vpn + os.sep + 'all.json') as f:
        countries = json.load(f)

    if country not in countries:
        # if it's not in the hashmap, check against the general aliases dict
        with open(root + 'aliases.json') as f:
            aliases = json.load(f)
        if country in aliases:
            country = aliases[country]
        else:
            print("invalid country")
            return

    # pick a random configuration filename from the vpn's country's available configurations
    # actual files are stored in the default wireguard directory (typically /etc/wireguard)
    conf = random.choice(countries[country])
    switch_vpn.switch_vpn(conf)

if __name__ == '__main__':
    main()
