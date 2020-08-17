from init_adapter import create_adapter_instance
import subprocess


class Device:

    def __init__(self):
        self.bus = {}
        self.bus_device_nr = {}
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

        self.interfaces = []

    def enumerate(self):
        temp = create_adapter_instance('ls -la', "admin", "a", 5, 8)
        wlanx = temp[0]
        mon = temp[1]
        for iface_id in wlanx:
            if iface_id:
                self.interfaces.append(Interface(iface_id))









    def add_interface(self, interface):
        self.interfaces.append(interface)



class Interface:

    def __init__(self, iface_id="none"):
        self.iface_id = iface_id
        self.isup = False
        self.mode = {}
        self.test = False

    def check_monitor(self, keyword):
        var1 = subprocess.Popen(['ls -la'], stdout=subprocess.PIPE, shell=True)
        output = str(var1.communicate())
        if keyword in output:
            self.mode = "monitor"




# TODO: Crete class instances from results

# wlan_list = Interface.enumerate()[0]
# print(wlan_list)
# mon_list = Interface.enumerate()[1]
# print(wlan_list)
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
