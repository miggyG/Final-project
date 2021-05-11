import ChessBoard


def setup():
    size(1200,1226)
    backimg = loadImage("ChessBack.png")
    background(backimg)
    
    
    
    
    
def draw(): 

    ChessBoard.chessboard(30,30)
    
    
