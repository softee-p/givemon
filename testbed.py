# import subprocess
# from my_tools import cmd_find_words



text1 = "Example wlan of wlan0 andwlan1 so wlan2can be tested. "
text2 = text1.split( )
print(text2)
keyword = "a"

for word in text2:
    if keyword not in word:
        text2.remove(word)
print(text2)

'''''''''
for line in text1:
    if keyword in line:
        results_list.append(line)
'''''''''
