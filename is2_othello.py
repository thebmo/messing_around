game=[
	['O','O','O','W','O','O','O','O'],
	['O','B','O','B','O','O','O','O'],
    ['O','O','B','B','O','O','O','O'],
    ['W','B','B','O','B','B','B','W'],
    ['O','O','B','B','B','O','O','O'],
    ['O','B','O','B','O','B','O','O'],
    ['W','O','O','B','O','O','B','O'],
    ['O','B','B','W','O','B','B','W']
    ]

# Logic to check if any matches are found
def check_lines(coords, off_s, color, o_color):

    x = coords[0]
    y = coords[1]

    dx = off_s[0]
    dy = off_s[1]

    flip_these = []

    try:
        # checks the rows to see if pieces should be flipped
        while(x+dx < len(game) and y+dy < len(game) and game[x+dx][y+dy] == o_color):
            x+=dx
            y+=dy
            
            flip_these.append((x, y))

        # flips the pieces
        if game[x+(dx)][y+(dy)] == color:
            for f in flip_these:
                game[f[0]][f[1]] = color

    except IndexError:
        pass


# main call to handle test game flow
def main():
    color = 'W'   # player color
    o_color = 'B' # opponent's color

    coords = [3, 3] # the move the player makes

    dxs = (-1, 0, 1)
    dys = (-1, 0, 1)

    # prints starting game board
    print '\nBefore piece played'
    for row in game:
        print row
        
    # plays the piece
    game[coords[0]][coords[1]] = color

    # checks if pieces needs to be flipped
    for dx in dxs:
        for dy in dys:
            if dx == 0 and dy == 0:
                continue
            check_lines(coords, (dx, dy), color, o_color)

    # prints teh finished game board
    print '\nAfter piece played'
    for row in game:
        print row


if __name__ == '__main__':
    main()
