from my_tools import cmd_find_values


class Device:
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

    @classmethod
    def enumerate(cls):  # TODO: Test on linux <print(Device.enumerate())>

        re = cmd_find_values("usb-devices", cls.init_keywords, "Bus=",
                             ["Driver=hub"], ["Product=802.11", "Driver="])

        # devices_count = re[1]
        for item in re:
            if "802.11" in item[5]:
                cls.misc.append(Wireless(item[0], item[1], item[2], item[3], item[4],
                                         item[5], item[6], item[7], item[8]))
            else:
                cls.misc.append(cls(item[0], item[1], item[2], item[3], item[4],
                                    item[5], item[6], item[7], item[8]))


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

        # self._enumerate()
        # elf.mac = self.interfaces[0].mac


    def enumerate(self, interface):
        self.interfaces.append(interface)


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


# TODO 1: Crete class instances from results
'''
Comments:_

'''
