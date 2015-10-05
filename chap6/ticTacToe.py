

theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' ',}

def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-l'])
    print('-+-+-')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-l'])
    print('-+-+-')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-l'])

printBoard(theBoard)
