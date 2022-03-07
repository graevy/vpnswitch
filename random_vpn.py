import json
import random
import os

import switch_vpn


if __name__ == '__main__':
    with open(os.path.dirname(__file__) + os.sep + 'confs' + os.sep + 'all.json') as f:
        vpn = random.choice(json.load(f))

    switch_vpn.switch_vpn(vpn)
