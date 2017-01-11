# -*- coding: utf-8 -*-
"""
Copyright: meowbowgrr@gmail.com
@author: Meow Bow Grr
This script can solve 'bridge crossing with torch' puzzles
examples of the puzzle:
1) http://www.mytechinterviews.com/four-people-on-a-rickety-bridge
2) https://www.youtube.com/watch?v=vF-OivyPcSs
3) https://www.youtube.com/watch?v=7yDmGnA8Hw0
"""

"""
sample change
"""

def crossbridge(times, folks_at_a_time):
    """ 
    Yo, this function will solve the 'bridge crossing with torch' puzzle. 
    Pass it the time taken by each person in a list and the number of folks who can cross at a time.
    """
    import sys # because i need this
    
    bside = times #list at the bad side
    box_size = folks_at_a_time #box size
    gside = [] #list at the good side
    ret = [] #return value
    side_select = 'bside' #to toggle between bad side and good side in loop
    total_time = 0 #total time taken to cross the bridge
    
    ret.append([bside.copy(),gside.copy(),total_time]) # keep dropping each step into the return value
    
    #ok, so the algo is to move the slowest walkers from bside to gside whenever possible. this is preffered
    #and move fastest walker from gside to bside with torch
    #when you are planning to move the slowest walker from bside to gside, check if the fastest walker from gside
    #in the next step will be equal to the fastest walker in this step. got it???
    #if yes, then move the slowest walkers in this step. 
    #thats it. amen
    while len(bside) > 0:
        if side_select == 'bside':
            bside.sort()
            send = []
            if len(gside) == 0 or min(bside[-2:]) <= min(gside, default = sys.maxsize):
                for i in range(0,box_size):
                    send.append(bside.pop(0))
            else:
                for i in range(0,box_size):
                    send.append(bside.pop(-1))
            total_time = total_time + max(send)
            gside.extend(send)
            ret.append([bside.copy(),gside.copy(),total_time])
            side_select = 'gside'
        elif side_select == 'gside':
            gside.sort()
            send = gside.pop(0)
            bside.append(send)
            total_time = total_time + send
            ret.append([bside.copy(),gside.copy(),total_time])
            side_select = 'bside'
    return ret

if __name__ == '__main__':
    #bside is the bad side, since in the puzzles something bad gonna happen to you if you remain on that side
    bside = input("Enter the time taken by each person (space separated): ")
    #box size is the number of people who cross at same time. since the time taken is equal the time
    #of the slowest guy, its like fitting smaller bozex into a big box
    box_size = input("Enter the number of folks who can cross the bridge at a time: ")
    print ()
    #convert bside to list because i like lists
    bside = list(map(int, bside.split()))
    #convert into int because whatever
    box_size = int(box_size) 
    #call the solver
    steps = crossbridge(bside, box_size)
    #print out the result, see the bridge i created |====|, awesome
    for i in range (0,len(steps)):
        print(steps[i][0],"  |=========|  ", steps[i][1], "\t total time taken = ", steps[i][2])