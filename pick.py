import os
import json
import random

import switch_vpn


# this function can get called without any args, so most conditional logic
# is determining how to interpret args
def main(args):
    root = os.path.dirname(__file__) + os.sep
    vpns = root + 'vpns' + os.sep
    cfg = root + 'cfg' + os.sep

    # if no vpn is supplied after calling switch, grab the default vpn from the cfg dir
    # this is a vpn host (a wg peer), e.g. "mullvad"
    if not args or args[0] not in os.listdir(root + 'vpns'):
        with open(cfg + 'default_vpn.txt') as f:
            vpn = vpns + f.readline()
    # otherwise, interpret the first arg as the vpn, and then slice out the first arg
    else:
        vpn = vpns + args[0]
        args = args[1:]
    
    vpn += os.sep
    
    # now choose which vpn set to load.
    # e.g. every vpn from that provider minus 14-eyes nations, every european vpn, etc.
    # TODO: polish this control flow
    if args:
        if not args[0].endswith('.json'):
            args[0] += '.json'
        if args[0] in os.listdir(vpn):
            vpn += args[0]
            args = args[1:]
        else:
            vpn += 'default.json'
    else:
        vpn += 'default.json'

    with open(vpn) as f:
        vpn = json.load(f)

    for location in args:
        vpn = vpn[location]
    
    while isinstance(vpn, dict):
        vpn = random.choice(list(vpn.values()))

    if isinstance(vpn, list):
        vpn = random.choice(vpn)

    switch_vpn.switch_vpn(vpn)
