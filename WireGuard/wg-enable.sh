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
# Rename profile wg0 as $con_name: 
# ```nmcli connection modify wg0 connection.id "$con_name"```
#
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
RED="\e[31m"
GREEN="\e[32m"
NC="\e[0m"

con_name=$1
action=$2


#sudo wg-quick $1 wg0
OUTPUT=$(nmcli connection $action $con_name 2>&1)

RESULT=$?
if [ $RESULT -eq 0 ]; then
    printf "Wireguard connection $con_name is ${GREEN}$action${NC}\n"
    zenity  --info --ellipsize --timeout=2 \
            --text="Wireguard connection $con_name is\n$action" \
            --title="WireGuard" \
            --window-icon=$SCRIPT_DIR/icons/WireGuard.png \
            --icon-name=go-$action
else
    printf "${RED}Error${NC} setting Wireguard connection $con_name to ${GREEN}$action${NC}\n"
    zenity  --error --ellipsize \
            --text="Error setting Wireguard connection $con_name to \n$action\n\nDetails:\n$OUTPUT" \
            --title="WireGuard" \
            --window-icon=$SCRIPT_DIR/icons/WireGuard.png \
            --icon-name=error
fi

printf "\n"

read -n 1 -s -r -p "Press any key to continue"
exit