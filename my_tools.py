import subprocess



class Adapter:

    def __init__(self, interface_name, device_name, driver, mode, power,):
        self.interface_name = interface_name
        self.device_name = device_name
        self.driver = driver
        self.mode = mode
        self.power = power






def cmd_grep(target):
    interface_list = subprocess.run(['iw', 'dev'], capture_output=True, text=True)

    if interface_list.returncode == 0:


        interface_name0 = subprocess.run(['grep', target], stdout=subprocess.PIPE, text=True,
                                         input=interface_list.stdout)

        if interface_name0.stdout != "":
            return interface_list.stdout

    else:
        print("error.command failed.")


def cmd_run(command):
    var = subprocess.run(command, capture_output=True, text=True, shell=True)  # example cmd_run('iw dev')
    return var.stdout








def command_output_find(command, keyword, append):

    results_list = []

    p1 = subprocess.run(command, capture_output=True, text=True, shell=True)




    if p1.returncode == 0:


        if p1.stdout.count(keyword) != 0:
            #  print("Found ", p1.stdout.count(keyword), "words containing the keyword:", keyword)





            pos1 = p1.stdout.find(keyword)
            pos2 = p1.stdout.find(keyword, pos1 + len(keyword) + int(append))

            for poopoo in range(p1.stdout.count(keyword)):

                results_list.append(p1.stdout[pos1:pos1 + len(keyword) + int(append)])

                pos1 = pos2

            return results_list

                #  word2 = p1.stdout[p1.stdout.find(keyword, pos1):p1

                #  interface_names.append(word1)

                #  iterations += 1


        else:
            print("keyword found 0 times.")

            # for poopoo in range(p1.stdout.count(keyword)):
                # print(p1.stdout.find(keyword))
                # print(p1.stdout[92:98]


    else:
        print("command failed")


#  print(command_output_find('ls', "o", "1"))




