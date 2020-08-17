from my_tools import cmd_find_segments




# Find usb devices
xa = cmd_find_segments("ls -la", "admin", "704")[0][0]
xb = cmd_find_segments("ls -la", "admin", "704")[1]

print(xa)
print(xb)
# find values







# TODO test on linux: cmd_find_segments('usb-devices', "Po", False, "rt=00")
'''Test1
output2 = output.split('\n')
print(output2)
output3 = output2[0].split('\\')

print(output3)
----------------------Test2
var = cmd_find_segments("ls -la", "adm")
print(var)

for line in var:
    if "root" in line:
        var.remove(line)
print(var)
'''
