from my_tools import cmd_find_values, cmd_find_lines


class Device:
    _name_source = cmd_find_lines("lsusb", ["Bus"])
    wireless = []
    misc = []
    init_keywords = ["Dev#=", "Ver=", "Vendor=", "ProdID=", "Manufacturer=",
                     "Product=", "SerialNumber=", "MxPwr=", "Driver="]

    def __init__(self, bus_id, version, version_id, product_id,
                 manufacturer, product_type, serial, maxpwr, driver):
        self.bus_id = bus_id
        self.version = version
        self.vendor_id = version_id
        self.product_id = product_id
        self.manufacturer = manufacturer
        self.product_type = product_type
        self.serial = serial
        self.maxpwr = maxpwr
        self.driver = driver

    @classmethod    # Use as: Device.enumerate(), then get instances in Device lists
    def enumerate(cls):
        Device.wireless = []
        Device.misc = []

        re = cmd_find_values("usb-devices", cls.init_keywords, "Bus=",
                             ["Driver=hub"], ["Product=802.11", "Driver="])
        for item in re:
            if "802.11" in item[5]:
                cls.wireless.append(Wireless(item[0], item[1], item[2], item[3], item[4],
                                             item[5], item[6], item[7], item[8]))
            else:
                cls.misc.append(cls(item[0], item[1], item[2], item[3], item[4],
                                    item[5], item[6], item[7], item[8]))



    @classmethod
    def status(cls):
        if Device.wireless == [] and Device.misc == []:
            return "Devices not enumerated. Run <Device.enumerate()> first"

        print('Found {} wireless and {} misc devices\nWireless Devices')
        for device in Device.wireless:
            print(''


                  )







class Wireless(Device):

    init_keywords = ["description:", "id:", "name:", "serial:", "driver=", "ip=", "wireless="]
    re = cmd_find_values("lshw -C network", init_keywords, "*-")

    def __init__(self, bus_id, version, version_id, product_id,
                 manufacturer, product_type, serial, maxpwr, driver):
        super().__init__(bus_id, version, version_id, product_id,
                         manufacturer, product_type, serial, maxpwr, driver)
        self.mac = ""
        self.interfaces = []
        for item in Wireless.re:
            if self.driver == item[4]:
                self.mac = item[3]
                self.interfaces.append(Interface(item[0], item[1], item[2],
                                                 item[3], item[4], item[5], item[6]))

    def re_enumerate(self):
        re = cmd_find_values("lshw -C network", Wireless.init_keywords, "*-")
        self.interfaces = []

        for item in re:
            if self.driver == item[4]:
                self.mac = item[3]
                self.interfaces.append(Interface(item[0], item[1], item[2],
                                                 item[3], item[4], item[5], item[6]))


class Interface:

    def __init__(self, description, physical_id, iface_id, mac, driver, ip_addr, wireless_type):
        self.description = description
        self.physical_id = physical_id
        self.iface_id = iface_id
        self.mac = mac
        self.driver = driver
        self.ip_addr = ip_addr
        self.wireless_type = wireless_type

        self.isup = False
        self.mode = {}
        self.test = False



'''
Comments:_

'''
