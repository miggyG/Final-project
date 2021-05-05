class ChessBoard:

    def _init_(self, letterRow, numCol):
        self.x = letterRow
        self.y = numCol
    def display(self, x, y):
        fill(120,120,0)
        rect(x, y, 55, 55)
