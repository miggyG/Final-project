class king:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        if team == "White":
            wbish = loadImage("WhiteKing.png")
        else:
            wbish = loadImage("BlackKing.png")
        image(wbish, x+13,y+12.5,100,100)
