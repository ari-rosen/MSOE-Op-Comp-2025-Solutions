from collections import Counter

content = ""
with open("caveMice.txt", "r") as file:
    content = file.read()

counter = Counter(content)

print(counter["o"])
