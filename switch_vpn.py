import os


def switch_vpn(vpn):
    # fetch current wireguard configuration for next step:
    current_vpn = os.popen("wg | head -n 1").read().rstrip().split()

    # disable current wg interface if there is one
    if current_vpn:
        # wg output is "interface: conf_filename"
        current_vpn = current_vpn[1]
        os.system("systemctl disable --now wg-quick@" + current_vpn)


    # enable and start new wg interface from vpn
    os.system("systemctl enable --now wg-quick@" + vpn.rsplit('.', 1)[0]) # remove .conf suffix
