class Adapter:

    def __init__(self, iface_id="none", device_name="none", driver="none", mode="none", power="none",):
        self.iface_id = iface_id
        self.device_name = device_name
        self.driver = driver
        self.mode = mode
        self.power = power


    def fullname(self):
        return '{} {}'.format(self.device_name, self.iface_id)
        #  print(adapter1.fullname())

    # def initialize(self):
        # if self.interface_id == "wlan"
