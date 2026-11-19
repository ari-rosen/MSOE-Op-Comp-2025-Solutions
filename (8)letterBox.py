dict_content = ""
input_content = ""
with open("dictionary.txt", "r") as dict_file, open("letterBox.txt", "r") as input_file:
    dict_content = dict_file.read()
    input_content = input_file.read()

valid_words = set(dict_content.split())
letters = input_content.split()

size_x = len(letters) // 2
size_y = 2

valid_list = []

def is_valid_coord(coord):
    return 0 <= coord[0] < size_x and 0 <= coord[1] < size_y

def get_valid_connections(coord, visited, passed_diagonals):
    connections = []

    x = coord[0]
    y = coord[1]

    cardinals = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
    for cardinal in cardinals:
        if is_valid_coord(cardinal) and cardinal not in visited:
            connections.append((cardinal, False))

    diagonals = [(x+1, y+1), (x-1, y+1), (x-1, y-1), (x+1, y-1)]
    for diagonal in diagonals:
        line = (coord, diagonal)
        other_line = (diagonal, coord)
        if line in passed_diagonals or other_line in passed_diagonals:
            continue
        if is_valid_coord(diagonal) and diagonal not in visited:
            connections.append((diagonal, True))


    return connections


def traverse(coord, word, visited, passed_diagonals):
    if len(word) == len(letters):
        formatted = "".join(word)
        if formatted in valid_words and formatted not in valid_list:
            valid_list.append(formatted)

    for connection, is_diagonal in get_valid_connections(coord, visited, passed_diagonals):
        word.append(letters[int(connection[0] + size_x * connection[1])])
        visited.add(connection)

        if is_diagonal:
            passed_diagonals.append((coord, connection))
            passed_diagonals.append(((coord[0], (coord[1] + 1) % size_y), (connection[0], (connection[1] + 1) % size_y)))
        
        traverse(connection, word, visited, passed_diagonals)

        word.pop()
        visited.remove(connection)
        if is_diagonal:
            passed_diagonals.pop()
            passed_diagonals.pop()

for i, _ in enumerate(letters):
    x = i % size_x
    y = 0 if i < size_x else 1
    traverse((x, y), word=[letters[i]], visited={(x, y)}, passed_diagonals=[])

print(sorted(valid_list))





 


