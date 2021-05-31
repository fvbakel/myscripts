#!/bin/bash
# See https://www.wireguard.com
# enable and disable a WireGuard VPN connection as a regular user using NetworkManager
#
# works on Lubuntu
#
# import in nmcli see:
# https://www.cyberciti.biz/faq/how-to-import-wireguard-profile-using-nmcli-on-linux/
#
#  Set up shell environment variable: 
# ```file='/etc/wireguard/wg0.conf'```
# Now import it using the nmcli command: 
# ```sudo nmcli connection import type wireguard file "$file"```
# Rename profile wg0 as home-vpn: 
# ```nmcli connection modify wg0 connection.id "home-vpn"```
#
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "Wireguard connection home-vpn set to: ${GREEN}$1${NC}\n"
#sudo wg-quick $1 wg0
nmcli connection $1 home-vpn

printf "\n"

read -n 1 -s -r -p "Press any key to continue"
exit