# import subprocess
from init_adapter import create_adapter_class

'''
startup_message = input("| Hi! Setup ? |" + " YES/NO:")
if startup_message != "YES":
    print("| exiting...")
    raise SystemExit
else:
    input("| OK! Let me discover your wireless interfaces. |" + "     | Press Enter |")
'''

results = create_adapter_class('ls -la', "admin", "a", 5, 8)
# for wlan(x) and -mon on linux: ('iw dev', "wlan", "mon", 5, 8)
print(results)

wlan_class_list = create_adapter_class('ls -la', "admin", "a", 5, 8)[0]
mon_class_list = create_adapter_class('ls -la', "admin", "a", 5, 8)[1]

# Status
print('| Found {} wlan(x) interface names.'.format(len(wlan_class_list)))
print('| Found {} -mon in interface names.'.format(len(mon_class_list)))

# Gatekeeper
if len(wlan_class_list) == 0 and len(mon_class_list) == 0:
    print("No valid interface names found. Make sure they are up.")
    raise SystemExit
elif len(wlan_class_list) == 0:
    print("Make sure you have at least 1 interface in managed mode to continue.")
    raise SystemExit



# adapter0 = wlan_class_list[0]
# print(adapter0)
