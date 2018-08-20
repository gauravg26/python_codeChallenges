# Make Row of Bricks
def make_bricks(small, big, goal):
    if (goal//5 <= big) and ((goal -5*(goal//5))<= small):
        return True
    elif(goal//5 >= big) and ((goal -5*(goal//5))<=small):
        return True
    else:
        return False
print make_bricks(2,2,11)