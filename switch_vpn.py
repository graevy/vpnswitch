import os


def switch_vpn(vpn):
    # fetch current wireguard configuration for next step:
    # disable current wg interface if there is one
    current_vpn = os.popen("wg | head -n 1").read()

    if current_vpn:
        # wg output is "interface: conf_filename"
        current_vpn = current_vpn.split()[1].rstrip()
        os.system("systemctl disable --now wg-quick@" + current_vpn)


    # enable and start new wg interface from vpn
    os.system("systemctl enable --now wg-quick@" + vpn[:-5]) # remove .conf suffix
