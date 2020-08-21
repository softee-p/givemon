from my_tools import cmd_find_values, cmd_find_segments
# from device_classes import Device, Wireless, Interface



sauce = cmd_find_segments("ls -la", "\n")
print(sauce)



class Test:
    classes = []
    keys = ["admin", "staff"]
    misc = []
    print("passed Test!")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subclass_list = []
        self.cop()

    def cop(self):
        self.age = "overriden"



    @classmethod
    def enumeration(cls):
        var = cmd_find_values("ls -la", cls.keys, "\n", "", ["admin"])
        for item in var:
            if "70" in item[0]:
                print(item[0])
                cls.classes.append(SubTest(item[0], item[1]))
            else:
                cls.classes.append(Test(item[0], item[1]))


class SubTest(Test):
    keys = ["admin", "poo"]
    var = cmd_find_values("ls -la", keys, "\n", "", ["admin"])
    print("passed Subtest!")

    def __init__(self, name, age):
        super().__init__(name, age)
        self.mac = 0
        for item in SubTest.var:
            # print(item)
            if self.name == item[0]:
                self.mac = 123123



