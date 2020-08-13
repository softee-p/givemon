# import subprocess
from my_tools import cmd_find_words

'''
startup_message = input("| Hi! Setup ? |" + " YES/NO:")
if startup_message != "YES":
    print("| exiting...")
else:
    input("| OK! Let me discover your wireless interfaces. |" + "     | Press Enter |")
'''

output1 = cmd_find_words("ls -la", "a")

if len(output1) == 0:
    print("| No valid wireless interface-id found. Connect an adapter and reboot.")
else:
    iname_list = []
    for poo in output1:
        if poo not in iname_list:
            iname_list.append(poo)  # remove duplicates from list
    # print(output1)
    iname_list.sort()
    # print(iname_list)








# ifa ce_id_list = cmd_words_list("ls -la", "DS", "1")
#  print(iface_id_list)
