class chessboard:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def piece(self, x, y):
        fill(120,120,0)
        rect(x, y, 55, 55)
        
