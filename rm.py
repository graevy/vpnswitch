import os
import subprocess as sp


# TODO: any testing after i do backups of my DE
def rm(vpn):
    vpns = os.path.dirname(__file__) + os.sep + 'vpns' + os.sep
    if vpn not in os.listdir(vpns):
        raise Exception(f"argument {vpn} not understood. valid vpns to remove are: {os.listdir(vpns)}")

    # the important step
    sp.run("rm -r " + vpns + vpn)

    # the esoteric step to get the vpn service name and disable it
    # this is about as simple as i could manage to get it with wg
    # wg output starts with "interface: vpn_name\n", so splitting is pretty simple
    wg_out = sp.run("wg", capture_output=True, text=True).stdout.split(maxsplit=2)[1]

    # in case splitting ever fails..
    if vpn not in wg_out:
        raise Exception("rm is broken because it can't read wg output! please submit a github issue")

    sp.run(f"systemctl disable --now wg-quick@{wg_out}".split())
