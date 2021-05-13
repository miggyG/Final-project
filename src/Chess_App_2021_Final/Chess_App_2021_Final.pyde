import ChessBoard
#import Bishop
#bish = Bishop.bishop
pieces = ChessBoard.chessboard(10, 10)


def setup():
    size(1200,1226)
    backimg = loadImage("ChessBack.png")
    background(backimg)
    
    
    
    
    
def draw():
    repi = 9
    row = 87
    col = 100
    rowList = []
    for i in range(8):
        col = 100
        pieces.piece(row,col)
        rowList.append(row)
        println(rowList)
        for i in range(8):
            pieces.piece(row,col)
            col +=126.5
        row += 127
        
    
    
