import random
import sys
import os

import switch_vpn


if __name__ == '__main__':
    try:
        country = sys.argv[1]

        vpn = random.choice(os.listdir(
            os.path.dirname(__file__) + os.sep + 'confs' + os.sep + 'countries' + os.sep + country))

        switch_vpn.switch_vpn(vpn)

    except IndexError:
        print("expected a country name, aborting...")
