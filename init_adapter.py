import subprocess
from adapter import Adapter


# for wlan and -mon on linux: ('ifconfig', "wlan", "mon", 5, 8)
def create_adapter_instance(command, keyword, mon_keyword, minlen, maxlen):

    # Popen output & error gatekeeper
    var1 = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    if var1.returncode == 0:
        return print("Subprocess-command failed. Exit code ", var1.returncode)

    # split string at every space
    output = str(var1.communicate())
    output_list = output.split()

    # append keyword matches
    # if maxlen 0 append whole words from start of keyword
    wlanx_results = []
    for word in output_list:
        if keyword in word and word not in wlanx_results:
            if maxlen == 0:
                wlanx_results.append(word[word.find(keyword):])
            else:
                wlanx_results.append(word[word.find(keyword):word.find(keyword) + maxlen])

    # Split keyword and mon_keyword results into lists.
    wlanx_results.sort()
    mon_results = []
    for iface_id in wlanx_results:
        if mon_keyword in iface_id and iface_id not in mon_results:
            mon_results.append(iface_id)
        if len(iface_id) > minlen:
            wlanx_results.remove(iface_id)

    mon_results.sort()
    wlanx_results.sort()


    # matched keywords become interface ids. create 2 list of classes for each.
    wlanx_classes_list = []
    for iface_id in wlanx_results:
        wlanx_classes_list.append(Adapter(iface_id))
    mon_classes_list = []
    for iface_id in mon_results:
        mon_classes_list.append(Adapter(iface_id))

    return wlanx_classes_list, mon_classes_list


#  TODO: Push to new linux branch for testing. *CHANGE KEYWORDS ONLY*
#        Also make class-creation part more universal in usage.
# ------------------------------|TEST|------------------------------
# test1 = create_adapter_instance('ls -la', "wlan", "mon", 5, 8)
# print(test1)
# adapter_class_list = create_adapter_instance()[0]
# print(adapter_class_list)
# adapter0 = adapter_class_list[0]
# print(adapter0.mode)
