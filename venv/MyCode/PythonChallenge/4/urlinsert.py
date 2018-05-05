import urllib.request
import re

nothing = 63579
while True:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(nothing)
    html = urllib.request.urlopen(url).read().decode()
    print(html)
    nothing = int(html.split()[-1])
    # print(nothing)
# data = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]
# print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))
