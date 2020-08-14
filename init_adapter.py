import subprocess
from adapter import Adapter



def create_adapter_class():
    keyword = "admin"
    maxlen = 8


    var1 = subprocess.Popen(['ls -la'], stdout=subprocess.PIPE, shell=True)
    output = str(var1.communicate())
    if var1.returncode == 0:
        output_list = output.split()  # split string at every space

        all_results = []
        for word in output_list:
            if keyword in word and word not in all_results:     # remove duplicates
                if maxlen == 0:
                    all_results.append(word[word.find(keyword):])   # append all words containing the keyword
                else:
                    all_results.append(word[word.find(keyword):word.find(keyword) + maxlen])

        all_results.sort()
        if len(all_results) == 0:
            return print("No matching words found")
    else:
        return print("Command failed. Exit code ", var1.returncode)
    if len(all_results) == 0:
        return print("| No valid wireless interface-id found. Plug in an adapter.")




    mon_all_results = []
    for iface_id in all_results:
        if "ad" in iface_id:
            mon_all_results.append(iface_id)      # splitting wlan and -mon adapters
        if len(iface_id) > 5:
            all_results.remove(iface_id)
    mon_all_results.sort()
    all_results.sort()

    adapters = []
    for iface_id in all_results:
        adapters.append(Adapter(iface_id))      # convert adapters to class objects

    return adapters, mon_all_results


#  adapter0 = create_adapter_class()[0].iface_id)

#  TODO: Push to new linux branch for testing. *CHANGE KEYWORDS ONLY*
