# import subprocess
from my_tools import cmd_find_words

'''
startup_message = input("| Hi! Setup ? |" + " YES/NO:")
if startup_message != "YES":
    print("| exiting...")
else:
    input("| OK! Let me discover your wireless interfaces. |" + "     | Press Enter |")
'''

iface_ids = cmd_find_words("ls -la", "a", 10)

if len(iface_ids) == 0:
    print("| No valid wireless interface-id found. Connect an adapter and (preferably) reboot.")
else:
    print(iface_ids)
    print(" ")
    mon_iface_ids = []

    for iface_id in iface_ids:              # splitting wlan and -mon adapters
        if "at" in iface_id:
            iface_ids.remove(iface_id)
            mon_iface_ids.append(iface_id)

    mon_iface_ids.sort()
    iface_ids.sort()
    print(mon_iface_ids)








# ifa ce_id_list = cmd_words_list("ls -la", "DS", "1")
#  print(iface_ids_list)
