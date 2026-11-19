content = ""
with open("telephone.txt", "r") as file:
    content = file.read()

l = content.split()
word_rate = int(l.pop()) / 100

rate = word_rate **len(l)

num_people = 1
chance = 1
while chance * rate > 0.25:
    chance *= rate
    num_people += 1

print(num_people)


