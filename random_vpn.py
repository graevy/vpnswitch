import json
import random
import os

import switch_vpn


if __name__ == '__main__':

    countries_dir = os.path.dirname(__file__) + os.sep + 'confs' + os.sep + 'countries' + os.sep

    country = random.choice(os.listdir(countries_dir))
    vpn = random.choice(os.listdir(countries_dir + country))
    
    switch_vpn.switch_vpn(vpn)