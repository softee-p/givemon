from my_tools import cmd_find_segments




# Find usb adapters

xa = cmd_find_segments("usb-devices", "Bus", "802.11")

keyword = "Driver"
num_of_adapters = len(xa)
print(num_of_adapters)

new_results = []

for x in range(len(xa)):
	if keyword in xa[x]:
		new_results.append(xa[x][xa[x].find(keyword) + len(keyword):])

print(new_results)
