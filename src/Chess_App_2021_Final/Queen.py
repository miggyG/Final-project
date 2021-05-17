class queen:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        if team == "White":
            wbish = loadImage("WhiteQueen.png")
        else:
            wbish = loadImage("BlackQueen.png")
        image(wbish, x+13,y+12.5,100,100)
