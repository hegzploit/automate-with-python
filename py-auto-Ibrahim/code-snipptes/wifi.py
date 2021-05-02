#!/usr/bin/env python3
import subprocess
import sys


def run_command(command):
    output, _ = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True).communicate()
    return output.decode('utf-8').rstrip('\r\n')


def get_ssid():
    try:
        ssid = run_command(
            "nmcli -t -f active,ssid dev wifi | grep '^yes:' | sed 's/^yes://'"
        )
    except:
        print("Error")
        sys.exit(1)
    return ssid


def get_password(ssid):
    get_password_command = f'nmcli -s -g 802-11-wireless-security.psk connection show "{ssid}"'
    password = run_command(f'sudo {get_password_command}')
    return password


if __name__ == "__main__":
    ssid = get_ssid()
    password = get_password(ssid)
    print(password)
