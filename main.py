import subprocess
from adapter_check import cmd_grep
from adapter_check import cmd_run

startup = input("| Hi! Setup ? |" + " YES/NO:")
if startup != "YES":
	print("| exiting...")
else: input("| OK! Let me discover your wireless interfaces. |" + "     | Press Enter |")

interfaces = ["wlan0", "wlan1", "wlan2"]

for interface in interfaces:
	p1 = cmd_grep(interface)
	print(p1)

#while len(interfaces) < 2:
#	temp2 = cmd_run('grep -
#	interfaces.append(temp1)
#print(interfaces)
