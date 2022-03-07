# import json
# import os

# countries = os.listdir('/etc/wireguard/')

# def get_country_code(mullvad_str):
#     return mullvad_str[8:10]

# countries = {'austria':'at',
# 'australia':'au',
# 'belgium':'be',
# 'beta':'beta', # for the beta vpn server
# 'bulgaria':'bg',
# 'brazil':'br',
# 'canada':'ca',
# 'switzerland':'ch',
# 'czechia':'cz',
# 'germany':'de',
# 'denmark':'dk',
# 'estonia':'ee',
# 'spain':'es',
# 'finland':'fi',
# 'france':'fr',
# 'britain':'gb',
# 'hong kong':'hk',
# 'hungary':'hu',
# 'ireland':'ie',
# 'italy':'it',
# 'japan':'jp',
# 'luxembourg':'lu',
# 'latvia':'lv',
# 'moldova':'md',
# 'macedonia':'mk',
# 'netherlands':'nl',
# 'norway':'no',
# 'new zealand':'nz',
# 'poland':'pl',
# 'portugal':'pt',
# 'romania':'ro',
# 'serbia':'rs',
# 'sweden':'se',
# 'singapore':'sg',
# 'united states':'us',
# 'america':'us',
# }

# with open(os.path.dirname(__file__) + os.sep + 'confs' + os.sep + 'all.json') as f:
#     services = json.load(f)

# for conf in services:
#     with open(os.path.dirname(__file__) + os.sep + 'confs' + os.sep + 'countries' + os.sep +
#                 inverted_countries[get_country_code(conf)] + os.sep + conf, 'w+') as f:
#         pass

# United States, the United Kingdom, Australia, the Netherlands, Norway, Germany, Italy,
# Belgium, New Zealand, Canada, Denmark, France, Sweden and Spain (sp and es)
# eyes_14 = set(('us','uk','as','nl','no','de','it','be','nz','ca','da','fr','sw','sp','es'))

# # israel, japan (ja and jp), singapore, south korea
# eyes_18 = set(('us','uk','as','nl','no','de','it','be','nz','ca','da','fr','sw','sp','es','is','jp','ja','sn','ks'))

# # switzerland, iceland, romania, malaysia
# whitelist = set(('sz','ic','ro','my'))

# with open('/home/a/code/random_vpn/whitelist.json','w+') as f:
#     json.dump([country for country in countries if get_country_code(country) in whitelist], f)

# for elem in sorted(countries):
#     print(elem)