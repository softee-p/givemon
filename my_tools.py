import subprocess



def cmd_grep(target):  # TODO: Update func
    grep_list = subprocess.run(['iw', 'dev'], capture_output=True, text=True)
    if grep_list.returncode != 0:
        return print("Command failed. Exit code ", grep_list.returncode)
    interface_name0 = subprocess.run(['grep', target], stdout=subprocess.PIPE, text=True, input=grep_list.stdout)
    if interface_name0.stdout != "":
        return grep_list.stdout


def cmd_find_lines(command, keywords_list=""):
    # if keyword == False deactivate search.

    var1 = subprocess.Popen([command], universal_newlines=True,
                            stdout=subprocess.PIPE, shell=True,
                            stderr=subprocess.PIPE, )
    output, error = var1.communicate()

    if var1.returncode != 0:
        return print("Subprocess-command failed. Exit code: ", var1.returncode, "Error: ", error)

    output = output.split("\n")
    output = output[0].split('\\')
    if keywords_list == "":
        return output

    output_list = []
    for keyword in keywords_list:
        for line in output:
            if keyword in line and line not in output_list:
                output_list.append(line)
    return output_list


def cmd_find_words(command, keywords_list="", maxlen=0):     # Linux: ('ifconfig', "wlan", "mon", 5, 8)
    # find whole words starting with "keyword"

    var1 = subprocess.Popen([command], universal_newlines=True,
                            stdout=subprocess.PIPE, shell=True,
                            stderr=subprocess.PIPE, )

    output, error = var1.communicate()

    if var1.returncode != 0:
        return print("Subprocess-command failed. Exit code: ", var1.returncode, "Error: ", error)

    output_list = output.split()  # split string at every space
    if keywords_list == "":
        return output_list
    all_results = []
    for keyword in keywords_list:
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


def cmd_find_segments(command, split, keywords_list=""):
    # ('usb-devices', "Bus", "802.11")
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
    if keywords_list == "":
        return output_split
    results = []
    for keyword in keywords_list:
        for line in output_split:
            if keyword in line and line not in results:
                results.append(line)
    # print(output_split)
    return results



def cmd_find_values(command, data_list, split_point, exclusion_list="", inclusion_list=""):

    var1 = subprocess.Popen([command], universal_newlines=True,
                            stdout=subprocess.PIPE, shell=True,
                            stderr=subprocess.PIPE, )
    output, error = var1.communicate()
    if var1.returncode != 0:
        return print("Subprocess-command failed. Exit code: ", var1.returncode, "Error: ", error)
    output_split = output.split(split_point)

                        # If both ex and inc are passed,
    segment_count = []  # returns number of segments for each
                        # inclusion in order of inclusion_list.
    valid_segments = []
    if exclusion_list != "":
        for exclusion in exclusion_list:
            for segment in output_split:
                if exclusion not in segment and segment not in valid_segments:
                    valid_segments.append(segment)
        output_split = valid_segments
        valid_segments = []

    if inclusion_list != "":
        for inclusion in inclusion_list:
            temp_segment_count = 0
            for segment in output_split:
                if inclusion in segment and segment not in valid_segments:
                    valid_segments.append(segment)
                    temp_segment_count += 1
            segment_count.append(temp_segment_count)
    else:
        valid_segments = output_split


    results = []
    for x in range(len(valid_segments)):
        times_not_found = 0
        temp_results = []
        valid_segments[x] = valid_segments[x].split("\n")
        for keyword in data_list:
            times_found = 0
            for sentence in valid_segments[x]:
                sentence = sentence.split()
                for (i, word) in enumerate(sentence):
                    if keyword in word:
                        times_found += 1
                        if len(word) == len(keyword):
                            # print("result is in next word")
                            # print(sentence[i])
                            temp_results.append(sentence[i + 1])
                        else:
                            temp_results.append(word[word.find(keyword) + len(keyword):])
            # print(times_found)
            if times_found == 0:
                times_not_found += 1
                temp_results.append("unknown")
        if times_not_found != data_list:
            results.append(temp_results)

    if not segment_count:
        segment_count = len(results)

    return results, segment_count


# TODO: LINUX TEST2: not tested
"""
cmd_find_values("usb-devices", Device._init_keywords, "Bus=", ["Driver=hub"], ["Product=802.11", "Driver="])

print(var2)
"""
