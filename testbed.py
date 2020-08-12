import subprocess



p1 = subprocess.Popen(["ls", "-la"], stdout=subprocess.PIPE)




print(str(p1.stdout))
