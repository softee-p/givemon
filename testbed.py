from my_tools import cmd_find_segments


# Find usb adapters


xa = cmd_find_segments("usb-devices", "Bus", "802.11")

keyword = "Driver"
num_of_adapters = len(xa)
print(num_of_adapters)

results = []
print(xa)
for x in range(len(xa)):
	xa[x] = xa[x].split("\n")
	temp_results = []
	for word in xa[x]:
		if keyword in word:
			temp_results.append(word[word.find(keyword) + len(keyword):])
	results.append(temp_results)
print(results)
