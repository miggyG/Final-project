class bishop(object):
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        if team == "White":
            wbish = loadImage("WhiteBishop.png")
        else:
            wbish = loadImage("BlackBishop.png")
        image(wbish, x+13,y+12.5,100,100)
