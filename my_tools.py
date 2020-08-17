import subprocess


def find_value_of():
    pass


def cmd_grep(target):  # TODO: Update func
    grep_list = subprocess.run(['iw', 'dev'], capture_output=True, text=True)
    if grep_list.returncode == 0:
        return print("Command failed. Exit code ", grep_list.returncode)
    interface_name0 = subprocess.run(['grep', target], stdout=subprocess.PIPE, text=True, input=grep_list.stdout)
    if interface_name0.stdout != "":
        return grep_list.stdout


def cmd_find_lines(command, keyword=" "):
    # if keyword == False deactivate search.

    var1 = subprocess.Popen([command], universal_newlines=True,
                            stdout=subprocess.PIPE, shell=True,
                            stderr=subprocess.PIPE, )
    output, error = var1.communicate()

    if var1.returncode != 0:
        return print("Subprocess-command failed. Exit code: ", var1.returncode, "Error: ", error)

    output = output.split("\n")
    output = output[0].split('\\')
    if keyword == " ":
        return output

    output_list = []
    for line in output:
        if keyword in line and line not in output_list:
            output_list.append(line)
    return output_list


def cmd_find_words(command, keyword=" ", maxlen=0):     # Linux: ('ifconfig', "wlan", "mon", 5, 8)
    # find whole words starting with "keyword"

    var1 = subprocess.Popen([command], universal_newlines=True,
                            stdout=subprocess.PIPE, shell=True,
                            stderr=subprocess.PIPE, )

    output, error = var1.communicate()

    if var1.returncode != 0:
        return print("Subprocess-command failed. Exit code: ", var1.returncode, "Error: ", error)

    output_list = output.split()  # split string at every space
    if keyword == " ":
        return output_list
    all_results = []
    for word in output_list:
        if keyword in word and word not in all_results:  # remove duplicates
            if maxlen == 0:
                all_results.append(word[word.find(keyword):])  # append word from start of keyword until the end
            else:
                all_results.append(word[word.find(keyword):word.find(keyword) + maxlen])

    if len(all_results) == 0:
        return print("No matching words found")
    all_results.sort()
    return all_results


def cmd_find_segments(command, split, keyword=""):
    # ('usb-devices', "Po", False, "rt=00")
    # split and include only words starting with key: cmd_find_segments("ls -la", "Jul", True, "22"))

    var1 = subprocess.Popen([command], universal_newlines=True,
                            stdout=subprocess.PIPE, shell=True,
                            stderr=subprocess.PIPE, )
    output, error = var1.communicate()

    if var1.returncode != 0:
        return print("Subprocess-command failed. Exit code: ", var1.returncode, "Error: ", error)
    output_split = output.split(split)
    # print(output)
    # print(output_split)
    if keyword == "":
        return output_split
    results = []
    for line in output_split:
        if keyword in line:
            results.append(line)
    # print(output_split)
    return results
