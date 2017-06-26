import Board

def testNewBoard(board):
    if("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" == board.toString):
        return True
    else :
        return False

print("Board startposition FEN string test : " + (str)(testNewBoard( Board.Board() )) )
