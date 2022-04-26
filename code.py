from tracemalloc import start
import numpy as np

xrange=range(135,155)
yrange=range(-102,-78)
starting_position=(0,0)

#assuming you can reach landing zone with vx=0, 
#and with the fact that every upward trajectory goes to y=0,
#the largest y velocity value would allow you to reach the bottom
#of the y range in one step from y=0. Thus max y velocity = lowest
# range of y-1
# n(n+1)/2 gives us:
# 
max_y=int(yrange[1])+(int(yrange[1])-1)/2

#pt2


