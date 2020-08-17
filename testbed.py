from my_tools import cmd_find_segments




# Find usb adapters

xa = cmd_find_segments("usb-devices", "Bus", "802.11")
print(xa)
keywords = ["Driver", "Manufacturer"]
num_of_adapters = len(xa)
print(num_of_adapters)

results = []
print(xa)
for x in range(len(xa)):
	temp_results = []
	xa[x] = xa[x].split("\n")
	for word in xa[x]:
		for keyword in keywords:
			if keyword in word:
				temp_results.append(word[word.find(keyword) + len(keyword):])
	if temp_results != []:
		results.append(temp_results)
print(results)










"""
xa = cmd_find_segments("usb-devices", "Bus", "802.11")
print(xa)
keyword = "Driver"
num_of_adapters = len(xa)
print(num_of_adapters)

new_results = []
print(xa)
for x in range(len(xa)):
        xa[x] = xa[x].split("\n")
        for word in xa[x]:
                if keyword in word:
                        new_results.append(word[word.find(keyword) + len(keyword):])

print(new_results)
"""
