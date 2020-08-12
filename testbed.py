import subprocess

p = subprocess.run(['ls'], capture_output=True, text=True)

print(str(p.stdout))
# adapter_id = "wlan0"
# keyword = "wlan"

# if keyword in adapter_id:
#     print(keyword + adapter_id[len(keyword)])
