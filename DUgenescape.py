import random

CELLS = [(0, 0), (0, 1), (0, 2), (0, 3),
         (1, 0), (1, 1), (1, 2), (1, 3),
         (2, 0), (2, 1), (2, 2), (2, 3),
         (3, 0), (3, 1), (3, 2), (3, 3)]


def get_locations():
    player = random.choice(CELLS)
    key = random.choice(CELLS)
    door = random.choice(CELLS)

    if key == door or door == player or player == door:
        return get_locations()

    return player, key, door



def draw_map(player, key, door):
    print(' _ _ _ _')
    tile = '|{}'

    for idx, cell in enumerate(CELLS):
        if idx in [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14]:
            if cell == player:
                print(tile.format('P'), end='')
            elif cell == door:
                print(tile.format('D'), end='')
            elif cell == key:
                print(tile.format('K'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player:
                print(tile.format('P|'))
            elif cell == door:
                print(tile.format('D|'))
            elif cell == key:
                print(tile.format('K|'))
            else:
                print(tile.format('_|'))



def move_player(player, move):
    # player = (x,y)
    x, y = player
    if x < 1 and move == 'U':
        x = 3
    elif x > 2 and move == 'D':
        x = 0
    elif y < 1 and move == 'L':
        y = 3
    elif y > 2  and move == 'R':
        y = 0
    elif move == 'D':
        x += 1
    elif move == 'U':
        x -= 1
    elif move == 'R':
        y += 1
    elif move == 'L':
        y -= 1


    return x, y


key, door, player = get_locations()

x, y = player
print("Welcome to the LaLaland!")
print("You must get the key to escape from that door!")

moves = ['R', 'L', 'U', 'D']

haskey = False



while True:
    print("(Enter QUIT to quit)")
    # print("You're currently in room {}".format(player))


    draw_map(player, key, door)

    move = input("Your move?_")

    move = move.upper()
    if move == 'QUIT':
        break
    if move in moves:
        player = move_player(player, move)
    if player == key:
        haskey = True
        print("Now go to the door")
    if haskey == True and player == door:
        print('Congrats!')
        break
    else:
        print("You must get the key!")









