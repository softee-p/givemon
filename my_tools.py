import subprocess


def cmd_grep(target):
    interface_list = subprocess.run(['iw', 'dev'], capture_output=True, text=True)

    if interface_list.returncode == 0:


        interface_name0 = subprocess.run(['grep', target], stdout=subprocess.PIPE, text=True,
                                         input=interface_list.stdout)

        if interface_name0.stdout != "":
            return interface_list.stdout

    else:
        print("error.command failed.")





def cmd_find_lines(command, option):

    temp = subprocess.Popen([command, option], stdout=subprocess.PIPE)
    output = str(temp.communicate())

    output = output.split("\n")

    output = output[0].split('\\')

    output_list = []

    for line in output:
        output_list.append(line)
    return output_list


def find_line(inp, keyword):
    outp = []
    for line in inp:
        if keyword in line:
            outp.append(line)
    return outp




def cmd_words_list(command, keyword, append):

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



def cmd_find_words(command, keyword):


    var1 = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    var2 = str(var1.communicate())

    var3 = var2.split( )
    results = []

    for item in var3:
        if keyword in item:
            results.append(item[item.find(keyword):])
    return results
