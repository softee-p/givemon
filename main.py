# import subprocess
from my_tools import cmd_find_words
from adapter import Adapter

'''
startup_message = input("| Hi! Setup ? |" + " YES/NO:")
if startup_message != "YES":
    print("| exiting...")
else:
    input("| OK! Let me discover your wireless interfaces. |" + "     | Press Enter |")
'''

iface_ids = cmd_find_words("ls -la", "admin", 10)

if len(iface_ids) == 0:
    print("| No valid wireless interface-id found. Plug in an adapter.")
    raise SystemExit

print(iface_ids)
print(" ")


mon_iface_ids = []
for iface_id in iface_ids:
    if "ad" in iface_id:
        mon_iface_ids.append(iface_id)      # splitting wlan and -mon adapters
    if len(iface_id) > 5:
        iface_ids.remove(iface_id)

mon_iface_ids.sort()
iface_ids.sort()
print(mon_iface_ids)
print(iface_ids)

adapters = []
for iface_id in iface_ids:
    adapters.append(Adapter(iface_id))

print('| adapters in managed mode: {}'.format(len(adapters)))
print('| adapters in monitor mode: {}'.format(len(mon_iface_ids)))
# ifa ce_id_list = cmd_words_list("ls -la", "DS", "1")
#  print(iface_ids_list)


# TODO: Test if new function init_adapter can replace this.