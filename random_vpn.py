import json
import random
import os
import sys

import switch_vpn


def main():
    root = os.path.dirname(__file__) + 'confs' + os.sep

    if len(sys.argv) < 2:
        with open(root + 'default_vpn.txt') as f:
            vpn = f.readline()
    else:
        vpn = sys.argv[1]

    with open(root + vpn + os.sep + 'all.json') as f:
        countries = json.load(f)

    country = random.sample(countries, 1)
    conf = random.choice(country)
    
    switch_vpn.switch_vpn(conf)


if __name__ == '__main__':
    main()
