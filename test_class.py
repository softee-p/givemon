# from init_adapter import create_adapter_instance
import subprocess


class Device:

    def __init__(self):
        self.bus = {}
        self.bus_device = {}
        self.vendor_id = {}
        self.product_id = {}
        self.vendor_name = {}
        self.product_name = {}

        self.mac = {}
        self.driver = {}

        self.purpose = {}



class WirelessAdapter(Device):

    def __init__(self):
        super().__init__()
        self.tx_power = {}
        self.capabilities = []
        self.mode = {}

        self.interfaces = []


    def check_monitor(self, keyword):
        var1 = subprocess.Popen(['ls -la'], stdout=subprocess.PIPE, shell=True)
        output = str(var1.communicate())
        if keyword in output:
            self.capabilities.append("monitor")



    def add_interface(self, interface):
        self.interfaces.append(interface)



class Interface:

    def __init__(self, iface_id="none"):
        self.iface_id = iface_id
        self.isup = False
        self.mode = {}
        self.type = {}



'''
usb1 = classes_list[0]

print(usb1.present())


adapter0 = ManagedInterface(1102, 2466)
print(adapter0.bus_device)
adapter0.present()
adapter0.bus_device = "new"
print(adapter0.bus_device)
print(adapter0.interface_name)
'''
