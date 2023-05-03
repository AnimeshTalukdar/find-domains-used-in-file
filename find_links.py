import os
import re

file = os.popen("cat file.txt").read()
# print(file)

htmls = re.findall("http?[^:]:\/\/[A-Za-z1-9.]*", file)
print(htmls)
m = {}
for html in htmls:
    m[html] = m.get(html, 0) + 1
with open("domains.txt", "w") as domains:
    for k, v in m.items():
        print(k, v)
        domains.write(k + "\t" + str(v) + "\n")
