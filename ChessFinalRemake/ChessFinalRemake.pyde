import ChessBoard
gs = ChessBoard.GameState()
DIMENSION = 8
SQ_SIZE = 100
IMAGES = {}
        
def setup():
    size(850,850)
    

    
def loadImages():
    pieces = ["wP","wR","wN","wB","wQ","wK","bP","wR","wN","wB","wQ","wK"]
    for piece in pieces:
        IMAGES[piece] = loadImage(piece+".png")



def main():
    print(gs.board)
    loadImages()
    #drawGameState(gs)


    
if __name__ == "__main__":
    main()
    
