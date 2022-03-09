def create_vpn(vpn):
    with open(confs + vpn, 'w+') as f:
        json.dump({location:nodes for location,nodes in get_locations(vpn)})