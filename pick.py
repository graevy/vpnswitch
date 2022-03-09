import json
import sys
import os
import subprocess
import random

import switch_vpn


def main(*args):
    root = os.path.dirname(__file__) + os.sep
    vpns = os.listdir(root + 'vpns')

    if not args or args[0] not in vpns: 
        with open(root + 'cfg' + os.sep + 'default_vpn.txt') as f:
            vpn = json.load(f)
    else:
        with open(root + 'vpns' + os.sep + args[0]) as f:
            vpn = json.load(f)

    with open(root + ('vpns' + os.sep + args[0]) if args or args[0] in vpns else ('cfg' + os.sep + 'default_vpn.txt')) as f:
        vpn = json.load(f)
    
    for location in args[1:]:
        vpn = vpn[location]
    
    if isinstance(vpn, list):
        vpn = random.choice(vpn)

    switch_vpn.switch_vpn(vpn)

    

    # for arg in args:
    #     if isinstance(iterable, dict):
    #         iterable = iterable[arg]
    #     else:
    #         for elem in iterable:
    #             if elem == arg:
    #                 iterable = elem
    #                 break
    
    # if hasattr(iterable,'__iter__'):
    #     vpn = random.choice(iterable) if isinstance(iterable, list) else random.sample(iterable.values(), 1)
    # else:
    #     vpn = iterable

    # if not args:
    #     vpn = open(root + 'cfg' + os.sep + 'default_vpn.txt').readline()
    # elif args[0] in os.listdir(root + 'vpns'):
    #     vpn = args[0]


    # # parsing passed args for which vpn folder to use, and which country inside that folder to use
    # if len(sys.argv) <3:
    #     if len(sys.argv) == 1:
    #         print("expected args vpn, country")
    #         return
    #     else:
    #         with open(confs + 'default_vpn.txt') as f:
    #             vpn = f.readline()
    #             country = sys.argv[1]
    # else:
    #     # check country input against valid input by loading the vpn's country:configurations hashmap
    #     with open(confs + vpn + os.sep + 'all.json') as f:
    #         countries = json.load(f)

    #     # if the first arg isn't a country,
    #     if sys.argv[1] not in countries:
    #         with open(confs + 'aliases.json') as f:
    #             aliases = json.load(f)
    #         # if it also isn't an alias for a country, it's probably a vpn
    #         if sys.argv[1] not in aliases:
    #             # if it's a vpn, set it
    #             if sys.argv[1] in os.listdir(confs):
    #                 vpn = sys.argv[1]
    #     vpn = sys.argv[1]
    #     country = sys.argv[2]


    # if country not in countries:
    #     # if it's not in the hashmap, check against the general aliases dict
    #     with open(root + 'aliases.json') as f:
    #         aliases = json.load(f)
    #     if country in aliases:
    #         country = aliases[country]
    #     else:
    #         print("invalid country")
    #         return

    # # pick a random configuration filename from the vpn's country's available configurations
    # # actual files are stored in the default wireguard directory (typically /etc/wireguard)
    # conf = random.choice(countries[country])
    # switch_vpn.switch_vpn(conf)

if __name__ == '__main__':
    main()
