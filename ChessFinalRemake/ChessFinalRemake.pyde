import ChessBoard
gs = ChessBoard.GameState()

def setup():
    size(1200,1226)
    backimg = loadImage("ChessBack.png")
    background(backimg)
    
def loadImages():
    loadImage("bP.png")
    loadImage("bR.png")
    loadImage("bN.png")
    loadImage("bB.png")
    loadImage("bQ.png")
    loadImage("bK.png")
    loadImage("wP.png")
    loadImage("wR.png")
    loadImage("wN.png")
    loadImage("wB.png")
    loadImage("wQ.png")
    loadImage("wK.png")


def main():
    print(gs.board)
    loadImages()
    drawGameState(gs)

def drawGameState(gs):
    drawBoard()
    
    drawPieces()
    
def drawBoard():
    
    
def drawPieces():

if __name__ == "__main__":
    main()
    
