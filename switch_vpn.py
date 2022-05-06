import subprocess


def switch_vpn(conf_filename):
    # remove .conf suffix from wg config file to produce systemd service name
    new_service = "wg-quick@" + conf_filename.rsplit('.', 1)[0]

    # fetch current wireguard systemd service for next step:
    current_service = subprocess.run(['wg'], capture_output=True, text=True).stdout.split('\n', 1)[0]
    # wg output is "interface: conf_filename"
    # so the split list is ["interface:", conf_filename]


    # disable current wg service if there is one
    if current_service:
        current_service = "wg-quick@" + current_service[1]
        subprocess.run(("systemctl disable --now " + current_service).split())


    # enable and start new wg service from vpn
    subprocess.run(("systemctl enable --now " + new_service).split())
