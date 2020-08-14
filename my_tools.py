import subprocess


def cmd_grep(target):
    grep_list = subprocess.run(['iw', 'dev'], capture_output=True, text=True)

    if grep_list.returncode == 0:

        interface_name0 = subprocess.run(['grep', target], stdout=subprocess.PIPE, text=True,
                                         input=grep_list.stdout)

        if interface_name0.stdout != "":
            return grep_list.stdout

    else:
        print("Command failed. Exit code ", grep_list.returncode)


def cmd_find_lines(command, option, keyword):
    temp = subprocess.Popen([command, option], stdout=subprocess.PIPE)
    output = str(temp.communicate())

    if temp.returncode == 0:

        output = output.split("\n")
        output = output[0].split('\\')

        output_list = []
        for line in output:
            if keyword in line and line not in output_list:
                output_list.append(line)
        return output_list

    else:
        print("Command failed. Exit code ", temp.returncode)




def cmd_find_words(command, keyword, maxlen):
    # find whole words starting with "keyword"

    var1 = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
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
            print("No matching words found")
        return all_results
    else:
        print("Command failed. Exit code ", var1.returncode)












def cmd_find_words_old(command, keyword, append):
    results_list = []

    p1 = subprocess.run([command], capture_output=True, text=True, shell=True)

    # print(p1.stdout.count(keyword))

    if p1.returncode == 0:

        if p1.stdout.count(keyword) != 0:
            #  print("Found ", p1.stdout.count(keyword), "words containing the keyword:", keyword)

            pos1 = p1.stdout.find(keyword)
            pos2 = p1.stdout.find(keyword, pos1 + len(keyword) + int(append))

            for poopoo in range(p1.stdout.count(keyword)):
                results_list.append(p1.stdout[pos1:pos1 + len(keyword) + int(append)])

                pos1 = pos2

        else:
            print("keyword found 0 times.")

    else:
        print("command failed")
    return results_list
