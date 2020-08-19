


class Device:

    def __init__(self, some_list, version, version_id, product_id, manufacturer, device_type, serial, mxpwr, driver):
        self.bus_device_num = some_list
        self.version = version
        self.vendor_id = version_id
        self.product_id = product_id
        self.manufacturer = manufacturer
        self.device_type = device_type
        self.serial = serial
        self.mxpwr = mxpwr
        self.driver = driver

        self.mac = {}




class WirelessAdapter(Device):

    def __init__(self, some_list, version, version_id, product_id, manufacturer, device_type, serial, mxpwr, driver):
        super().__init__(some_list, version, version_id, product_id, manufacturer, device_type, serial, mxpwr, driver)

        self.interfaces = []


    def add_interface(self, interface):
        self.interfaces.append(interface)



class Interface:

    def __init__(self, iface_id="none"):
        self.iface_id = iface_id
        self.isup = False
        self.mode = {}
        self.test = False


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
