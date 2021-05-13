class chessboard:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def piece(self, x, y):
        rectMode(CORNER)
        noFill()
        strokeWeight(2)
        rect(x, y, 128, 125)
        
        
