content = ""
with open("aiStutter.txt", "r") as file:
    content = file.read().lower()

words = content.split();
stutters = 0

for word in words:
    i = 0
    while i < len(word):
        if i > 1 and word[i] == word[i-1] == word[i-2] and word[i].isalpha():
            stutters += 1
            print(word)
            while i < len(word) and word[i] == word[i-1] == word[i-2]:
                i += 1
        else:
            i += 1


print(stutters)

