dict_content = ""
input_content = ""
with open("dictionary.txt", "r") as dict_file, open("fourSquare.txt", "r") as input_file:
    dict_content = dict_file.read()
    input_content = input_file.read()

valid_words = set(dict_content.split())
letters = input_content.split()

# adjacency graph, each node is a letter in letters with their connections by index
# 3rd element is always a diagonal in the graph so we can tell
adj = [
    [1, 2, 3],
    [0, 3, 2],
    [0, 3, 1],
    [1, 2, 0]
] 

valid_list = []

def traverse(current, word, visited, passed_diagonal):
    if len(word) == 4:
        formatted = "".join(word)
        if formatted in valid_words and formatted not in valid_list:
            valid_list.append(formatted)
    
    for i, connection in enumerate(adj[current]):
        if connection in visited:
            continue

        is_diagonal = i == 2

        if passed_diagonal and is_diagonal:
            continue

        visited.add(connection)
        word.append(letters[connection])

        traverse(connection, word, visited, is_diagonal or passed_diagonal)

        visited.remove(connection)
        word.pop()


for i, _ in enumerate(letters):
    traverse(i, word=[letters[i]], visited={i}, passed_diagonal=False)

print(sorted(valid_list))
