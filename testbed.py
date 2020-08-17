from my_tools import cmd_find_lines, cmd_find_words, cmd_find_segments



xa = cmd_find_words("ls -la", "admin")








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
