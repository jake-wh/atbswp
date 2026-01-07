import sys, copy, logging

logging.basicConfig(
    filename="logs/chessboard_log.txt",
    filemode='w',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
WHITE_SQUARE = '||'
BLACK_SQUARE = '  '


def print_chess_board(board):
    squares = []
    is_white_square = True
    for y in '87654321':
        for x in 'abcdefgh':
            print(x, y, is_white_square)  # DEBUG: Shows coordinates in order.
            if x + y in board.keys():
              squares.append(board[x + y])
            else:
              if is_white_square:
                squares.append(WHITE_SQUARE)
              else:
                squares.append(BLACK_SQUARE)
            is_white_square = not is_white_square
        is_white_square = not is_white_square

    print(BOARD_TEMPLATE.format(*squares))

def print_help():
    print('Interactive Chess Board')
    print('by Al Sweigart al@inventwithpython.com')
    print()
    print('Pieces:')
    print('  w - White, b - Black')
    print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
    print('Commands:')
    print('  move e2 e4 - Moves the piece at e2 to e4.')
    print('  remove e2 - Removes the piece at e2.')
    print('  set e2 wP - Sets square e2 to a white pawn.')
    print('  reset - Reset pieces back to their starting squares.')
    print('  clear - Clear the entire board.')
    print('  fill wP - Fill entire board with white pawns.')
    print('  help - Show this help information.')
    print('  quit - Quits the program.')

def is_valid_chessboard(board):
    logging.info("Checking chessboard validity...")

    if not isinstance(board, dict):
        logging.error("Argument passed is not a dictionary.")
        return False

    king_counts = {'wK': 0, 'bK': 0}

    counts = {'w': 0, 'b': 0}

    for position, piece in board.items():
        if not position[0] <= 'h':
            logging.error(f"Invalid position[0]: {position[0]}")
            return False
        elif not 0 < int(position[1]) <= 8:
            logging.error(f"Invalid position[1]: {position[1]}")
            return False
        elif piece[0] not in ['w', 'b']:
            logging.error(f"Invalid piece[0]: {piece[0]}")
            return False
        elif piece[1] not in ['P', 'R', 'N', 'B', 'Q', 'K']:
            logging.error(f"Invalid piece[1]: {piece[1]}")
            return False
        
        if piece == 'wK' or piece == 'bK':
            king_counts[piece] += 1

        counts[piece[0]] += 1
    
    for king, quantity in king_counts.items():
        if quantity > 1:
            logging.error(f"Invalid king counter: {king} - {quantity}")
            return False

    for colour, amount in counts.items():
        if amount > 16:
            logging.error(f"Invalid amount of pieces: {colour} - {amount}")
            return False

    logging.info("Chessboard successfully verified.")
    return True


main_board = copy.copy(STARTING_PIECES)
if not is_valid_chessboard(main_board):
    sys.exit()

print_help()
while True:

    print_chess_board(main_board)
    response = input('> ').split()

    if response[0] == 'move':
        main_board[response[2]] = main_board[response[1]]
        del main_board[response[1]]
    elif response[0] == 'remove':
        del main_board[response[1]]
    elif response[0] == 'set':
        main_board[response[1]] = response[2]
    elif response[0] == 'reset':
        main_board = copy.copy(STARTING_PIECES)
    elif response[0] == 'clear':
        main_board = {}
    elif response[0] == 'fill':
        for y in '87654321':
            for x in 'abcdefgh':
                main_board[x + y] = response[1]
    elif response[0] == 'help':
        print_help()
    elif response[0] == 'quit':
        sys.exit()