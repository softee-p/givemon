import subprocess



p1 = subprocess.run(["iw", "dev"], capture_output=True ,text=True)




interface_count = p1.stdout.count("txpower")
print(interface_count)

