theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print('-------')
    print('|' + board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + '|')
    print('-------')
    print('|' + board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] + '|')
    print('-------')
    print('|' + board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + '|')
    print('-------')

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    move = input('Turn for ' + turn + '. Move on which space? ')
    theBoard[move] = turn
    # win conditions
    if theBoard.values() in ('X','O', ' '):
        if theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R']:
            print(turn + ' wins')
            break
        elif theBoard['mid-L'] == theBoard['mid-M'] == theBoard['mid-R']:
            print(turn + ' wins')
            break
        elif theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R']:
            print(turn + ' wins')
            break
        elif theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L']:
            print(turn + ' wins')
            break
        elif theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M']:
            print(turn + ' wins')
            break
        elif theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R']:
            print(turn + ' wins')
            break
        elif theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R']:
            print(turn + ' wins')
            break
        elif theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L']:
            print(turn + ' wins')
            break
        else:
            None
    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)    
