import os


def create_vpn_profile(vpn, is_conf_member, location_from_conf, is_location_member=True,
                        profile_name='default.json', confs_dir='/etc/wireguard'):

    vpn_dir = os.path.dirname(__file__) + os.sep + vpn + os.sep
    os.makedirs(vpn_dir)
    profile_dict = {}

    for conf in os.listdir(confs_dir): 
        if is_conf_member(conf):
            location = location_from_conf(conf)
            if is_location_member(location):
                location_list = profile_dict.setdefault(location,[])
                location_list += conf

    with open(vpn_dir + profile, 'w+') as f:
        json.dump(profile_dict, f)
