# write your code here
map = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print('---------')
print('|', map[0], map[1], map[2], '|')
print('|', map[3], map[4], map[5], '|')
print('|', map[6], map[7], map[8], '|')
print('---------')

def cell_change(a, b):
    a_1 = int(a) - 1
    b_1 = int(b) + 2
    index = (a_1 * 3 + b_1) - 3
    return index


def x_move():
    new_input = input('Enter the coordinates: ')
    cord_list = new_input.split()
    if len(cord_list) == 2:
        try:
            x, y = int(cord_list[0]), int(cord_list[1])
            if x < 1 or x > 3:
                print('Coordinates should be from 1 to 3!')
                x_move()
            elif y < 1 or y > 3:
                print('Coordinates should be from 1 to 3!')
                x_move()
            else:
                cell = cell_change(cord_list[0], cord_list[1])
                cell = int(cell)
                if map[cell] == "X" or map[cell] == "O":
                    print('This cell is occupied! Choose another one!')
                    x_move()
                else:
                    map[cell] = 'X'   
        except:
            print('You should enter numbers!')
            x_move()
    else:
        print('Enter only two numbers from 1 to 3!')
        x_move()
        
def o_move():
    new_input = input('Enter the coordinates: ')
    cord_list = new_input.split()
    if len(cord_list) == 2:
        try:
            x, y = int(cord_list[0]), int(cord_list[1])
            if x < 1 or x > 3:
                print('Coordinates should be from 1 to 3!')
                o_move()
            elif y < 1 or y > 3:
                print('Coordinates should be from 1 to 3!')
                o_move()
            else:
                cell = cell_change(cord_list[0], cord_list[1])
                cell = int(cell)
                if map[cell] == "X" or map[cell] == "O":
                    print('This cell is occupied! Choose another one!')
                    o_move()
                else:
                    map[cell] = 'O'
        except:
            print('You should enter numbers!')
            o_move()
    else:
        print('Enter only two numbers from 1 to 3!')
        o_move()

while True:
    x_move()
    print('---------')
    print('|', map[0], map[1], map[2], '|')
    print('|', map[3], map[4], map[5], '|')
    print('|', map[6], map[7], map[8], '|')
    print('---------')
    lines = [map[:3], map[3:6], map[6:], map[0::3], map[1::3], map[2::3], map[2:7:2], map[0:9:4]]
    if ['X', 'X', 'X'] in lines:
        print('X wins')
        quit()
    elif not ' ' in map:
        print('Draw')
        break
    o_move()
    print('---------')
    print('|', map[0], map[1], map[2], '|')
    print('|', map[3], map[4], map[5], '|')
    print('|', map[6], map[7], map[8], '|')
    print('---------')
    lines = [map[:3], map[3:6], map[6:], map[0::3], map[1::3], map[2::3], map[2:7:2], map[0:9:4]]
    if ['O', 'O', 'O'] in lines:
        print('O wins')
        quit()
    elif not ' ' in map:
        print('Draw')
        break
    
    
    
    

    
