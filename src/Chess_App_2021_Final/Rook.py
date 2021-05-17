class rook:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        if team == "White":
            wbish = loadImage("WhiteRook.png")
        else:
            wbish = loadImage("BlackRook.png")
        image(wbish, x+13,y+12.5,100,100)
