class Adapter:
    number_of_adapters = 0



    def __init__(self, iface_id="none"):
        self.iface_id = iface_id
        self.device_name = {}
        self.driver = {}
        self.mode = {}
        self.power = {}


        Adapter.number_of_adapters += 1






    def present(self):
        return '{} {} {} {} {}'.format(self.iface_id, self.device_name, self.driver, self.mode, self.power)
        #  print(adapter1.fullname())

        # def initialize(self):
        # if self.interface_id == "wlan"
