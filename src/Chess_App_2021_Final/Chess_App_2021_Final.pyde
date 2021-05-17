#pieces
import King
import Queen
import Rook
import Bishop
import Knight
import Pawn
king = King.king
queen = Queen.queen
rook = Rook.rook
bishop = Bishop.bishop
knight = Knight.knight
pawn = Pawn.pawn
#Teams
tW = "White"
tB = "Black"
#square is w=128 h=125
#letters are x
#numbers are y 
#cords
a = 87
b = 215
c = 343
d = 471
e = 599
f = 727
g = 855
h = 983
r8 = 100
r7 = 225
r6 = 350
r5 = 475
r4 = 600
r3 = 725
r2 = 850
r1 = 975

def setup():
    size(1200,1226)
    backimg = loadImage("ChessBack.png")
    background(backimg)
    king(e,r8,tB)
    king(e,r1,tW)
    queen(d,r8,tB)
    queen(d,r1,tW)
    rook(a,r8,tB)
    rook(h,r8,tB)
    rook(a,r1,tW)
    rook(h,r1,tW)
    bishop(c,r8,tB)
    bishop(f,r8,tB)
    bishop(c,r1,tW)
    bishop(f,r1,tW)
    knight(b,r8,tB)
    knight(g,r8,tB)
    knight(b,r1,tW)
    knight(g,r1,tW)
    pawn(a,r7,tB)
    pawn(b,r7,tB)
    pawn(c,r7,tB)
    pawn(d,r7,tB)
    pawn(e,r7,tB)
    pawn(f,r7,tB)
    pawn(g,r7,tB)
    pawn(h,r7,tB)
    pawn(a,r2,tW)
    pawn(b,r2,tW)
    pawn(c,r2,tW)
    pawn(d,r2,tW)
    pawn(e,r2,tW)
    pawn(f,r2,tW)
    pawn(g,r2,tW)
    pawn(h,r2,tW)
    
    
    
    

    
