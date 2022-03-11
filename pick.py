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
    
    # vpn is now e.g. "{path.dirname(__file__}/vpns/mullvad/"
    vpn += os.sep
    
    # now choose which vpn set to load.
    # e.g. every vpn from that provider minus 14-eyes nations, every european vpn, etc.
    # TODO support for "non14" instead of "non14.json"
    if args and args[0] in os.listdir(vpn):
        vpn += args[0]
        args = args[1:]
    else:
        vpn += 'default.json'

    # vpn is now the dict of location:[peers]
    with open(vpn) as f:
        vpn = json.load(f)

    # if the location arg passed is a country code, or "united states" etc, the alias dict will hopefully handle it
    with open(cfg + 'aliases.json') as f:
        aliases = json.load(f)

    # support for nested location dicts e.g. {america:{new york:{manhattan:[address1,address2]}, boston:[address1]}
    for location in args:
        if location in vpn:
            vpn = vpn[location]
        elif location in aliases:
            vpn = vpn[aliases[location]]
        else:
            raise Exception(
                f"{location} not understood. valid location args are:\n    {aliases.keys()}\n    {vpn.keys()}"
                )
    
    # at this point, if vpn is a host, there's nothing left to do
    # if there are still nested dicts, randomly choose a value.
    while isinstance(vpn, dict):
        vpn = random.choice(list(vpn.values()))

    # if vpn is a list, pick a random value
    if isinstance(vpn, list):
        vpn = random.choice(vpn)

    switch_vpn.switch_vpn(vpn)

# this came to me while trying to sleep
# i think it's a better implementation because the args can be anywhere,
# and it might involve less overhead, idk
# def foo(args):

#     # get the vpn
#     valid_vpns = frozenset(os.listdir(vpns))
#     # valid_vpns = {vpn:os.listdir(vpns+vpn) for vpn in os.listdir(vpns)}
#     for arg in args.copy():
#         if arg in valid_vpns:
#             vpn = arg
#             args.remove(arg)
#     else:
#         with open(cfg + 'default_vpn.txt') as f:
#             vpn = f.readline()

#     # get the locations hashmap
#     vpn_profiles = frozenset(os.listdir(vpns + vpn)) 
#     s = vpns + vpn + os.sep

#     for arg in args.copy():
#         if arg in vpn_profiles:
#             s += arg
#             args.remove(arg)
#     else:
#         s += 'default.json'

#     with open(s) as f:
#         locations = json.load(f)
#     with open(cfg + 'aliases.json') as f:
#         aliases   = json.load(f)

#     for arg in args.copy():
#         if arg in locations:
#             locations = location[arg]
#             args.remove(arg)
#         elif arg in aliases:
#             locations = location[aliases[arg]]
#             args.remove(arg)
#         else:
#             raise Exception(f"argument {arg} not understood.")
    
#     while isinstance(locations, dict):
#         locations = random.choice(list(locations.values()))

#     # if locations is a list, pick a random value
#     if isinstance(locations, list):
#         locations = random.choice(locations)

#     switch_vpn.switch_vpn(locations)