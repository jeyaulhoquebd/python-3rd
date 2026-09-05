#Python program to find and count specific words using RegEx

import re
txt = """The rain in spain the rain in spain """

x = re.findall("ai", txt)
print("counting word:\n",txt)
