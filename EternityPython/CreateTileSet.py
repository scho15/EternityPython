import time

TILE_SET_SIZE = 256
EDGE_SET_SIZE = 60
PATTERN_TYPES = 22
tileList = [] # Create list of tiles with index tilenumber and edges as 4 properties
usedTiles = [] # List of tiles used in current sequence
tilePatternList = [] # List of tiles with tile patterns
tilePatternSet = set()
consecutivePatterns = [] # List of tiles with two consecutive patterns
unexploredTiles = [] # List of tiles which have not been explored
exploredTiles = [] # List of tiles which have been explored

def createTile():
    # 0: Grey edge tile
    # 1: Pink/Light Blue - like swallow
    # 2: Dk Blue/Yellow - 4 pointed cross, club style
    # 3: Orange/Lt Blue - Cross style
    # 4: Green/Dk Blue - Hexagon
    # 5: Brown/Orange - Castle style
    # Middle Area Tiles
    # 6: Dk Blue/Orange - cross with club feet
    # 7: Dk Blue/Pink - dark blue cross in pink circle
    # 8: Dk Blue/Lt Blue - Diamond
    # 9: Orange/Purple - 6 pointed star
    # 10: Green/Orange - 4 pointed flared cross
    # 11: Green/Pink - 4 pointed cross club style
    # 12: Brown/Green - Brown cross in green circle
    # 13: Brown/Yellow - 6 pointed star
    # 14: Pink/Yellow - 4 pointed cross club style
    # 15: Pink/Yellow - 4 pointed castle style
    # 16: Purple/Lt Blue - 4 pointed flared cross
    # 17: Purple/Yellow - purple cross in yellow circle
    # 18: Yellow/Green - Diamond
    # 19: Yellow/Mid Blue - 6 pointed star
    # 20: Yellow/Blue - 4 pointed cross castle style
    # 21: Lt Blue/Pink - 4 pointed flared cross
    # 22: Lt Blue/Pink - 4 pointed cross castle style

    # Create set of Eternity tiles
    tileList.insert(0, [-1, -1, -1, -1])
    tileList.insert(1, [3, 1, 0, 0])
    tileList.insert(2, [3, 4, 0, 0])
    tileList.insert(3, [2, 1, 0, 0])
    tileList.insert(4, [1, 2, 0, 0])
    tileList.insert(5, [3, 14, 3, 0])
    tileList.insert(6, [3, 16, 2, 0])
    tileList.insert(7, [3, 17, 3, 0])
    tileList.insert(8, [3, 17, 5, 0 ])
    tileList.insert(9, [3, 10, 1, 0 ])
    tileList.insert(10, [3, 22, 4, 0 ])
    tileList.insert(11, [3, 18, 2, 0 ])
    tileList.insert(12, [3, 6 , 4, 0 ])
    tileList.insert(13, [3, 6 , 5, 0 ])
    tileList.insert(14, [3, 15, 4, 0 ])
    tileList.insert(15, [2, 16, 3, 0 ])
    tileList.insert(16, [2, 19, 1, 0 ])
    tileList.insert(17, [2, 11, 5, 0 ])
    tileList.insert(18, [2, 13, 5, 0 ])
    tileList.insert(19, [2, 22, 2, 0 ])
    tileList.insert(20, [2, 18, 2, 0 ])
    tileList.insert(21, [2, 21, 4, 0 ])
    tileList.insert(22, [2, 20, 3, 0 ])
    tileList.insert(23, [2, 20, 5, 0 ])
    tileList.insert(24, [2, 9 , 3, 0 ])
    tileList.insert(25, [2, 15, 3, 0 ])
    tileList.insert(26, [1, 14, 2, 0 ])
    tileList.insert(27, [1, 14, 1, 0 ])
    tileList.insert(28, [1, 16, 1, 0 ])
    tileList.insert(29, [1, 19, 1, 0 ])
    tileList.insert(30, [1, 22, 5, 0 ])
    tileList.insert(31, [1, 18, 2, 0 ])
    tileList.insert(32, [1, 9 , 1, 0 ])
    tileList.insert(33, [1, 6 , 2, 0 ])
    tileList.insert(34, [1, 6 , 4, 0 ])
    tileList.insert( 35,[1, 8 , 5, 0 ])
    tileList.insert( 36,[1, 7 , 4, 0 ])
    tileList.insert( 37, [4, 19, 3, 0 ])
    tileList.insert( 38, [4, 12, 5, 0 ])
    tileList.insert( 39, [4, 10, 5, 0 ])
    tileList.insert( 40, [4, 13, 2, 0 ])
    tileList.insert( 41, [4, 13, 1, 0 ])
    tileList.insert( 42, [4, 18, 3, 0 ])
    tileList.insert( 43, [4, 18, 2, 0 ])
    tileList.insert( 44, [4, 18, 1, 0 ])
    tileList.insert( 45, [4, 21, 3, 0 ])
    tileList.insert( 46, [4, 9 , 4, 0 ])
    tileList.insert( 47, [4, 6 , 4, 0 ])
    tileList.insert( 48, [4, 8 , 4, 0 ])
    tileList.insert( 49, [5, 14, 5, 0 ])
    tileList.insert( 50, [5, 16, 3, 0 ])
    tileList.insert( 51, [5, 16, 2, 0 ])
    tileList.insert( 52, [5, 17, 3, 0 ])
    tileList.insert( 53, [5, 22, 4, 0 ])
    tileList.insert( 54, [5, 21, 4, 0 ])
    tileList.insert( 55, [5, 21, 5, 0 ])
    tileList.insert( 56, [5, 6 , 1, 0 ])
    tileList.insert( 57, [5, 8 , 3, 0 ])
    tileList.insert( 58, [5, 8 , 5, 0 ])
    tileList.insert( 59, [5, 15, 2, 0 ])
    tileList.insert( 60, [5, 7 , 1, 0 ])
    tileList.insert( 61, [17, 19, 14, 14 ])
    tileList.insert( 62, [11, 22, 14, 14 ])
    tileList.insert( 63, [16, 12, 14, 16 ])
    tileList.insert( 64, [14, 6 , 14, 19 ])
    tileList.insert( 65, [19, 7 , 14, 19 ])
    tileList.insert( 66, [11, 11, 14, 19 ])
    tileList.insert( 67, [10, 16, 14, 19 ])
    tileList.insert( 68, [9 , 17, 14, 19 ])
    tileList.insert( 69, [7 ,  6, 14, 19 ])
    tileList.insert( 70, [12, 22, 14, 12 ])
    tileList.insert( 71, [22, 20, 14, 12 ])
    tileList.insert( 72, [11, 19, 14, 10 ])
    tileList.insert( 73, [18, 21, 14, 10 ])
    tileList.insert( 74, [9 , 18, 14, 10 ])
    tileList.insert( 75, [6 , 12, 14, 10 ])
    tileList.insert( 76, [11, 18, 14, 13 ])
    tileList.insert( 77, [13, 18, 14, 13 ])
    tileList.insert( 78, [12,  8, 14, 22 ])
    tileList.insert( 79, [9 , 12, 14, 22 ])
    tileList.insert( 80, [8 , 15, 14, 22 ])
    tileList.insert( 81, [13, 19, 14, 18 ])
    tileList.insert( 82, [19, 19, 14, 21 ])
    tileList.insert( 83, [10, 21, 14, 21 ]) 
    tileList.insert( 84, [19, 13, 14, 20 ])
    tileList.insert( 85, [17, 11, 14, 20 ])
    tileList.insert( 86, [6 , 20, 14, 20 ])
    tileList.insert( 87, [8 , 9 , 14, 20 ])
    tileList.insert( 88, [14, 15, 14,  9 ])
    tileList.insert( 89, [17, 7 , 14,  9 ])
    tileList.insert( 90, [21, 8 , 14,  9 ])
    tileList.insert( 91, [10, 20, 14,  6 ])
    tileList.insert( 92, [13, 18, 14,  6 ])
    tileList.insert( 93, [13, 21, 14,  6 ])
    tileList.insert( 94, [21, 15, 14,  6 ])
    tileList.insert( 95, [20, 11, 14,  6 ])
    tileList.insert( 96, [15, 12, 14, 15 ])
    tileList.insert( 97, [21, 13, 14,  7 ])
    tileList.insert( 98, [9,  6, 14,  7 ])
    tileList.insert( 99, [15, 17, 14,  7 ])
    tileList.insert( 100, [7, 15, 14, 7 ])
    tileList.insert( 101, [20, 18, 16, 16 ])
    tileList.insert( 102, [20,  8, 16, 16 ])
    tileList.insert( 103, [8, 13, 16, 16 ])
    tileList.insert( 104, [7, 17, 16, 16 ])
    tileList.insert( 105, [21, 18, 16, 19 ])
    tileList.insert( 106, [12,  6, 16, 17 ])
    tileList.insert( 107, [13,  6, 16, 17 ])
    tileList.insert( 108, [21, 18, 16, 17 ])
    tileList.insert( 109, [8, 10, 16, 17 ])
    tileList.insert( 110, [18, 20, 16, 11 ])
    tileList.insert( 111, [20, 18, 16, 11 ])
    tileList.insert( 112, [9, 13, 16, 12 ])
    tileList.insert( 113, [9,  8, 16, 12 ])
    tileList.insert( 114, [11, 21, 16, 10 ])
    tileList.insert( 115, [22, 20, 16, 10 ]) 
    tileList.insert( 116, [20, 10, 16, 10 ])
    tileList.insert( 117,  [7,  8, 16, 10 ])
    tileList.insert( 118, [12, 15, 16, 13 ])
    tileList.insert( 119,  [8, 20, 16, 22 ]) 
    tileList.insert( 120,  [6,  7, 16, 18 ])
    tileList.insert( 121, [11,  7, 16, 21 ]) 
    tileList.insert( 122, [17,  8, 16,  9 ])
    tileList.insert( 123, [11, 13, 16,  9 ])
    tileList.insert( 124,  [9, 18, 16,  9 ])
    tileList.insert( 125, [20,  7, 16,  6 ])
    tileList.insert( 126, [15, 18, 16,  6 ])
    tileList.insert( 127, [11, 17, 16,  8 ])
    tileList.insert( 128, [13, 15, 16,  8 ])
    tileList.insert( 129, [21, 12, 16,  8 ])
    tileList.insert( 130,  [9,  6, 16,  8 ])
    tileList.insert( 131, [17,  9, 16, 15 ])
    tileList.insert( 132, [20, 11, 16, 15 ])
    tileList.insert( 133, [11,  8, 16,  7 ])
    tileList.insert( 134, [10, 21, 16,  7 ])
    tileList.insert( 135, [21, 12, 16,  7 ]) 
    tileList.insert( 136,  [8,  9, 16,  7 ])
    tileList.insert( 137,  [9, 22, 19, 19 ])
    tileList.insert( 138, [17, 12, 19, 17 ])
    tileList.insert( 139, [19, 17, 17, 10 ]) # centre tile with 19 top N in pos 120
    tileList.insert( 140, [17, 20, 19, 17 ])
    tileList.insert( 141, [13, 15, 19, 17 ])
    tileList.insert( 142, [18, 17, 19, 17 ])
    tileList.insert( 143,  [8, 20, 19, 17 ]) 
    tileList.insert( 144, [15, 15, 19, 17 ])
    tileList.insert( 145, [12, 21, 19, 11 ])
    tileList.insert( 146, [19, 20, 19, 12 ])
    tileList.insert( 147, [19,  7, 19, 12 ])
    tileList.insert( 148, [12, 11, 19, 12 ])
    tileList.insert( 149, [18, 20, 19, 12 ])
    tileList.insert( 150, [17, 10, 19, 13 ])
    tileList.insert( 151, [21,  7, 19, 13 ])
    tileList.insert( 152, [10, 10, 19, 22 ])
    tileList.insert( 153, [10, 13, 19, 22 ])
    tileList.insert( 154,  [7,  8, 19, 22 ])
    tileList.insert( 155, [22, 22, 19, 21 ])
    tileList.insert( 156, [22, 20, 19, 21 ])
    tileList.insert( 157,  [7, 22, 19, 21 ])
    tileList.insert( 158, [22,  8, 19,  9 ])
    tileList.insert( 159,  [6, 17, 19,  9 ])
    tileList.insert( 160, [15, 15, 19,  6 ])
    tileList.insert( 161, [17,  9, 19,  8 ])
    tileList.insert( 162, [11,  9, 19,  8 ])
    tileList.insert( 163, [18, 10, 19,  7 ])
    tileList.insert( 164, [21,  8, 19,  7 ])
    tileList.insert( 165, [12, 21, 17, 11 ])
    tileList.insert( 166, [21,  6, 17, 11 ])
    tileList.insert( 167, [12, 12, 17, 10 ])
    tileList.insert( 168, [10, 18, 17, 13 ])
    tileList.insert( 169, [13, 15, 17, 13 ])
    tileList.insert( 170, [21,  6, 17, 22 ])
    tileList.insert( 171,  [9,  8, 17, 22 ])
    tileList.insert( 172, [15, 10, 17, 22 ])
    tileList.insert( 173, [18, 18, 17, 18 ])
    tileList.insert( 174, [20,  9, 17, 18 ])
    tileList.insert( 175, [22, 15, 17, 21 ]) 
    tileList.insert( 176, [22, 13, 17, 20 ])
    tileList.insert( 177, [11, 21, 17,  9 ])
    tileList.insert( 178, [20,  8, 17,  6 ])
    tileList.insert( 179,  [6, 18, 17,  6 ])
    tileList.insert( 180, [22,  8, 17,  8 ])
    tileList.insert( 181, [10,  8, 17, 15 ]) # posn N3 (SW so 35) with 8 [diamond) N
    tileList.insert( 182, [22, 10, 17, 15 ])
    tileList.insert( 183, [13,  6, 11, 11 ])
    tileList.insert( 184,  [7, 22, 11, 12 ])
    tileList.insert( 185, [13, 20, 11, 10 ])
    tileList.insert( 186,  [6,  6, 11, 10 ])
    tileList.insert( 187, [15, 22, 11, 13 ])
    tileList.insert( 188, [11, 15, 11, 22 ])
    tileList.insert( 189, [12, 13, 11, 22 ])
    tileList.insert( 190,  [8, 13, 11, 22 ])
    tileList.insert( 191, [12, 12, 11, 18 ])
    tileList.insert( 192, [18,  9, 11, 18 ])
    tileList.insert( 193, [10, 22, 11, 21 ])
    tileList.insert( 194, [15, 10, 11, 20 ])
    tileList.insert( 195, [15,  7, 11, 20 ])
    tileList.insert( 196,  [7, 18, 11, 20 ])
    tileList.insert( 197, [10,  7, 11,  9 ])
    tileList.insert( 198, [13,  6, 11,  9 ])
    tileList.insert( 199,  [9,  9, 11,  9 ])
    tileList.insert( 200, [13, 12, 11,  6 ])
    tileList.insert( 201, [15,  6, 11,  8 ])
    tileList.insert( 202,  [7, 22, 11,  8 ])
    tileList.insert( 203, [20, 13, 11, 15 ])
    tileList.insert( 204, [20,  6, 11, 15 ])
    tileList.insert( 205,  [8, 12, 11, 15 ])
    tileList.insert( 206,  [7, 15, 11, 15 ])
    tileList.insert( 207,  [7, 22, 12, 12 ])
    tileList.insert( 208, [13,  7, 12, 10 ]) # posn C3 so 211 with 7 North
    tileList.insert( 209,  [6, 18, 12, 10 ])
    tileList.insert( 210, [10, 13, 12, 22 ])
    tileList.insert( 211,  [8, 18, 12, 22 ])
    tileList.insert( 212, [12,  8, 12, 18 ])
    tileList.insert( 213,  [6,  6, 12, 21 ])
    tileList.insert( 214, [12,  9, 12, 20 ])
    tileList.insert( 215, [21,  7, 12, 20 ])
    tileList.insert( 216,  [7, 15, 12, 20 ])
    tileList.insert( 217, [13, 18, 12,  9 ])
    tileList.insert( 218, [21, 20, 12,  8 ])
    tileList.insert( 219, [10, 21, 12, 15 ])
    tileList.insert( 220, [10,  8, 12,  7 ])
    tileList.insert( 221, [15, 15, 12,  7 ])
    tileList.insert( 222, [15,  7, 12,  7 ])
    tileList.insert( 223, [20,  7, 10, 10 ])
    tileList.insert( 224,  [9, 22, 10, 10 ])
    tileList.insert( 225,  [8, 18, 10, 10 ])
    tileList.insert( 226, [13, 18, 10, 22 ])
    tileList.insert( 227, [20, 20, 10, 22 ])
    tileList.insert( 228, [13,  6, 10, 21 ])
    tileList.insert( 229, [22,  7, 10,  9 ])
    tileList.insert( 230,  [8,  6, 10,  9 ])
    tileList.insert( 231, [20,  9, 10,  6 ])
    tileList.insert( 232, [20, 15, 10,  6 ])
    tileList.insert( 233, [13,  9, 13, 13 ])
    tileList.insert( 234, [8, 21, 13, 22 ])
    tileList.insert( 235, [22, 21, 13, 21 ])
    tileList.insert( 236, [22,  9, 13, 21 ])
    tileList.insert( 237, [20, 18, 13, 21 ])
    tileList.insert( 238, [21,  8, 13, 20 ])
    tileList.insert( 239, [18,  7, 13,  9 ])
    tileList.insert( 240, [15, 18, 13,  9 ])
    tileList.insert( 241, [2, 15, 13,  6 ])
    tileList.insert( 242, [21, 15, 13,  6 ])
    tileList.insert( 243, [18, 20, 22, 18 ])
    tileList.insert( 244,  [9,  6, 22, 18 ])
    tileList.insert( 245,  [7,  9, 22, 21 ])
    tileList.insert( 246,  [8,  7, 22, 15 ])
    tileList.insert( 247, [15,  7, 18, 18 ])
    tileList.insert( 248, [20, 21, 18, 21 ])
    tileList.insert( 249, [21, 15, 18, 20 ]) # pon N14 so 46 and SE with 21 N side
    tileList.insert( 250,  [8, 15, 18,  9 ])
    tileList.insert( 251,  [7,  6, 21, 21 ])
    tileList.insert( 252,  [6, 20, 21, 20 ])
    tileList.insert( 253,  [8,  9, 20,  6 ])
    tileList.insert( 254, [15,  8,  9,  8 ])
    tileList.insert( 255,  [8,  7,  9,  7 ]) # posn C14 (so 222 and NE) with 8 W side
    tileList.insert( 256, [15,  7,  6,  7 ])

def findPatternMatches():
    for x in range(PATTERN_TYPES + 1):
        for y in range(TILE_SET_SIZE + 1):
            for z in range( 4 ):
                if(tileList[y][z] == x):
                    tilePatternSet.add(y)
        tilePatternList.append(tilePatternSet.copy())
        tilePatternSet.clear()
        # print(f"Set of tiles with tile pattern {x} is {tilePatternList[x]}")

def findConsecutivePatternMatches(x, y):
    # Return the tile number of matching patterns not the whole tile
        twoPatterns = []
        for a in range(TILE_SET_SIZE + 1):
            for b in range( 4 ):
                if(tileList[a][b] == x and tileList[a][(b+1)%4] == y):
                    twoPatterns.append(a)
        #print(f"Set of tiles with two consecutive tile patterns {x} and {y} is {twoPatterns}")
        return twoPatterns

## Tiles must be in clockwise order
def findThreeConsecutivePatternMatches(x, y, z):
        threePatterns = []
        for a in range(TILE_SET_SIZE + 1):
            for b in range( 4 ):
                if(tileList[a][b] == x and tileList[a][(b+1)%4] == y and tileList[a][(b+2)%4] == z):
                    threePatterns.append(a)
        #print(f"Set of tiles with three consecutive tile patterns {x} {y} and {z} is {threePatterns}")
        return threePatterns

def findTileMatches():
    for x in range(TILE_SET_SIZE):
        for y in range(x + 1, TILE_SET_SIZE + 1):
            for z in range(4):
                    # Match tiles which are not edges
                    if ((tileList[x][z] == tileList[y][0]) and (tileList[y][0] != 0)):
                        print(f"tile {x} matches tile {y} on side {z} with edge {tileList[x][z]}")

def rotateTile(x):
    temp = tileList[x][0]
    tileList[x][0] = tileList[x][3]
    tileList[x][3] = tileList[x][2]
    tileList[x][2] = tileList[x][1]
    tileList[x][1] = temp

def startMatching(cutoff):
    start = time.time()
    # Need 3 different elements - unexplored path, explored path and currentPath/usedtiles
    # If only the usedTiles/cuurenpath is used, previously ruled out sequences comes back in play creating repeating loops
    # Explored only adds used tiles when there are no further sequences so need to make sure they are added at the right place
    iteration = 1
    #print(f"Iteration {iteration}")
    # Find tiles with consecutive 0 and 0 patterns i.e. corners
    consecutivePatterns = findConsecutivePatternMatches(0,0)
    unexploredTiles.append(consecutivePatterns.copy())
    exploredTiles.append([])
    #print(f"Unexplored tiles at iteration {iteration} is {unexploredTiles}")
    # Choose first tile as match (random would be an alternative)
    matchTile = unexploredTiles[0][0]
    unexploredTiles[0].pop(0)
    # Rotate tile to ensure edges are correctly aligned
    while (tileList[matchTile][2] != 0 & tileList[matchTile][1] == 0):
        rotateTile(matchTile)
    #print(f"Match tile {matchTile} selected and appended to usedTiles")
    #print(f"Rotation to ensure S and W aligned so we have tile {matchTile} now at {tileList[matchTile]}")
    usedTiles.append(matchTile)
    #print(f"Used tiles list (also containing patterns in correct rotation) is now {usedTiles}")

    iteration = 2
    eastMatch = 0
    firstMatch = 0
    secondMatch = 0
    exploredTiles.append([])
    count = 0
    maxIteration = 1

    while (matchTile != 0 and iteration <= cutoff):
        # Next matches as a list
        count += 1
        if (iteration <= 16):
            consecutivePatterns = findConsecutivePatternMatches(0,tileList[usedTiles[iteration-2]][1])
            # Temporary - to avoid getting stuck on iteration 34 for first choice model
            if ((iteration == 6) and (16 in consecutivePatterns)):
                consecutivePatterns.remove(16)
                print(F"Temporary: Tile 16 has been removed at iteration 6 to avoid getting stuck")
        if (iteration == 16):
            consecutivePatterns = findThreeConsecutivePatternMatches(0, 0, tileList[usedTiles[iteration-2]][1])
            #print(f"Matching tile list at corner is {consecutivePatterns}") # Optional Line 1
        if (iteration > 16 and iteration%16 == 1):
            consecutivePatterns = findConsecutivePatternMatches(tileList[usedTiles[iteration-17]][0],0)
        if (iteration > 16 and iteration%16 != 0 and iteration%16 != 1):
            firstMatch = tileList[usedTiles[iteration - 17]][0]
            #print(f'Edge to match on the South is {firstMatch}') # Optional Line 2
            secondMatch = tileList[usedTiles[iteration - 2]][1]
            #print(f'Edge to match on the West is {secondMatch}') # Optional Line 3
            # Introducing constraints on hint on level lower. Arguable whether this is good for upper hint tiles
            if (iteration != 19 and iteration !=30 and iteration != 104 and iteration != 195 and iteration != 206):
                consecutivePatterns = findConsecutivePatternMatches(firstMatch,secondMatch)
            elif (iteration == 19):
                # ensuring iteration 19 has Northern tile of 15 as well as matching S and W
                consecutivePatterns = findThreeConsecutivePatternMatches(firstMatch, secondMatch, 15)
            elif (iteration == 30):
                # ensuring iteration 30 has Northern tile of 18 as well as matching S and W
                consecutivePatterns = findThreeConsecutivePatternMatches(firstMatch, secondMatch, 18)
            elif (iteration == 104):
                consecutivePatterns = findThreeConsecutivePatternMatches(firstMatch, secondMatch, 17)
            elif (iteration == 195):
                consecutivePatterns = findThreeConsecutivePatternMatches(firstMatch, secondMatch, 10)
            elif (iteration == 206):
                consecutivePatterns = findThreeConsecutivePatternMatches(firstMatch, secondMatch, 7)
            # Adding hints for centre tile
            if (iteration == 120):
                if (firstMatch != 17) and (secondMatch != 10):
                    consecutivePatterns.clear()
                elif (139 not in consecutivePatterns):
                    consecutivePatterns.clear()
                if (139 in consecutivePatterns):
                    consecutivePatterns = [139]
            if (139 in consecutivePatterns and iteration != 120):
                consecutivePatterns.remove(139)
            # Hint for SW tile
            if (iteration == 35):
                if (firstMatch != 15) and (secondMatch != 10):
                    consecutivePatterns.clear()
                # Does not automatically ensure that 181 is selected
                elif (181 not in consecutivePatterns):
                    consecutivePatterns.clear()
                if (181 in consecutivePatterns):
                    consecutivePatterns = [181]
            if (181 in consecutivePatterns and iteration != 35):
                consecutivePatterns.remove(181)
            # Hint for SE tile
            if (iteration == 46):
                if (firstMatch != 18) and (secondMatch != 20):
                    consecutivePatterns.clear()
                elif (249 not in consecutivePatterns):
                    consecutivePatterns.clear()
                if (249 in consecutivePatterns):
                    consecutivePatterns = [249]
            if (249 in consecutivePatterns and iteration != 46):
                consecutivePatterns.remove(249)
            # Hint for NW tile (partly academic!)
            if (iteration == 211):
                if (firstMatch != 10) and (secondMatch != 13):
                    consecutivePatterns.clear()
                elif (208 not in consecutivePatterns):
                    consecutivePatterns.clear()
                if (208 in consecutivePatterns):
                    consecutivePatterns = [208]
            if (208 in consecutivePatterns and iteration != 211):
                consecutivePatterns.remove(208)
            # Hint for NE tile (partly academic!)
            if (iteration == 222):
                if (firstMatch != 7) and (secondMatch != 8):
                    consecutivePatterns.clear()
                elif (255 not in consecutivePatterns):
                    consecutivePatterns.clear()
                if (255 in consecutivePatterns):
                    consecutivePatterns = [255]
            if (255 in consecutivePatterns and iteration != 222):
                consecutivePatterns.remove(255)
        if (iteration > 16 and iteration%16 == 0):
            firstMatch = tileList[usedTiles[iteration - 17]][0]
            #print(f'Edge to match on the South is {firstMatch}') # Optional Line 4
            secondMatch = tileList[usedTiles[iteration - 2]][1]
            #print(f'Edge to match on the West is {secondMatch}') # Optional Line 5
            thirdMatch = 0
            #print(f"Need to match outside edge {thirdMatch} as well") # Optional Line 6
            consecutivePatterns = findThreeConsecutivePatternMatches(0,firstMatch,secondMatch)
        # Remove items in usedTiles that have already been used
        for item in usedTiles:
            if item in consecutivePatterns[:]:
                consecutivePatterns.remove(item)
        # Remove items that are corner or edge tiles that won't fit
        for item in consecutivePatterns[:]:
                if (item <= 4 and iteration != 16):
                    consecutivePatterns.remove(item)
                elif (iteration == 16 and item > 4):
                    consecutivePatterns.remove(item)
                if (item <= 60 and iteration>16):
                    if (iteration%16 > 1):
                        consecutivePatterns.remove(item)
        #print(f"Matching tiles list after used tile purge is {consecutivePatterns}") # Optional Line 7
        if (len(exploredTiles) <= iteration - 1):
            exploredTiles.append([])
        #print(f"exploredTiles is\n {exploredTiles}")
        #if (len(exploredTiles[iteration-1]) == 0): - changed else below to if and negated expression
        #    print(f"Explored tiles for iteration {iteration} are nil so can be ignored")
        if (len(exploredTiles[iteration-1]) != 0):
            for item in exploredTiles[iteration-1]:
                if item in consecutivePatterns:
                    consecutivePatterns.remove(item)
            #print(f"Explored tiles for iteration is {exploredTiles[iteration-1]}")
        #print(f"Matching tiles list after explored tile purge is {consecutivePatterns}") # Optional Line 8
        # Take first eligible tile (for breadth first search would need to print them all out
        if (len(consecutivePatterns) != 0):
            matchTile = consecutivePatterns[0]
            consecutivePatterns.pop(0)
            unexploredTiles.append(consecutivePatterns.copy())
            matchConfiguration = tileList[matchTile]
            #print(f"Selecting tile {matchTile} which currently has NESW configuration of {matchConfiguration}") # Optional Line 9
            # Rotate tile to ensure edges are correctly aligned - originally screwed up as used AND rather than OR below
            if (iteration < 16):
                while (tileList[matchTile][2] != 0):
                    rotateTile(matchTile)
                    #print(f"Rotation to ensure edges aligned so we have tile {matchTile} now at {tileList[matchTile]}")
            if (iteration == 16):
                #print(f"\nConsidering the rotation of {matchTile} at iteration {iteration} which is currently {tileList[matchTile]}")
                while (tileList[matchTile][2] != 0 or tileList[matchTile][1] != 0):
                    rotateTile(matchTile)
                    #print(f"Rotation to ensure corners aligned so we have tile {matchTile} now at {tileList[matchTile]}")
            if (iteration > 16 and iteration%16 == 1):
                while (tileList[matchTile][3] != 0):
                    rotateTile(matchTile)
                    #print(f"Rotation to ensure edge aligned so we have tile {matchTile} now at {tileList[matchTile]}")
            elif (iteration > 16 and iteration%16 == 0):
                while (tileList[matchTile][1] != 0):
                    rotateTile(matchTile)
                    #print(f"Rotation to ensure edge aligned so we have tile {matchTile} now at {tileList[matchTile]}")
            # 31.5.20: Changed 1 to 3 below which is a big change
            elif (iteration > 16):
                while (tileList[matchTile][2] != firstMatch or tileList[matchTile][3] != secondMatch):
                    #print(f'Relevant match is at {tileList[matchTile][2]}')
                    rotateTile(matchTile)
                    #print(f"Rotation to ensure tiles aligned so we have tile {matchTile} now at {tileList[matchTile]}") #Optional Line 10
            # Adding to used tile list
            usedTiles.append(matchTile)
            if (iteration > maxIteration):
                maxIteration = iteration
                print(f"\nIteration is {iteration} and count is {count} with maximum iteration reached of {maxIteration}")
                maxCheck = True
            iteration +=1
        else:
            #print(f'Attempting backtracking!') # Optional Line 11
            #print(f"Length of last unexplored tiles is {len(unexploredTiles[-1])}") # Optional Line 12
            # First go back and remove the last used tile that led to no solution
            # attempting while rather than if
            while (len(unexploredTiles[-1]) == 0):
                #print(f'Removing the last iteration that was empty') # Optional Line 13
                usedTiles.pop()
                unexploredTiles.pop()
                exploredTiles.pop() # always reduces length by one - may also need to clear?
                exploredTiles[-1].clear() # yes results looking much better!!
                iteration -=1
                #print(f'The last unexploredTile is now {unexploredTiles[-1]}') # Optional Line 14
            if (len(unexploredTiles[-1])!=0):
                iteration -=1
                #print(f'The unexplored list is \n {unexploredTiles}') # Optional Line 15
                # iteration - 1 is right given the zero start for exploredTiles
                exploredTiles[iteration-1].append(usedTiles.pop()) # Only place where explored is appended
                #print(f'Last entry on used tile list popped and added to explored category:\n  {usedTiles}\n{exploredTiles}') #Opt Line 16
                #Consec tiles is re-determined for each level. Question whether to bypass this and use unexplored tiles instead
                #consecutivePatterns.extend(unexploredTiles[-1]) - deleted as consec re-determined at start of loop
                #print(f"Replacing empty option with unexplored options {consecutivePatterns}") # Optional Line 17
                unexploredTiles.pop() 
        end = time.time()
        if ((iteration == maxIteration and maxCheck == True) or count%5000000 == 0):
            print(f"\nUsed tiles list at count {count} is now \n{usedTiles}\n and iteration reached was {maxIteration}")
            print(f"Unexplored tiles at iteration {iteration} are \n{unexploredTiles}")
            print(f"Explored tiles at iteration {iteration} are \n{exploredTiles}")
            for i, val in enumerate(unexploredTiles):
                if i >= 0 and i <= 50:
                    print(f"{i+1}\t{usedTiles[i]} {val} {exploredTiles[i]}")
            print(f"Time taken in seconds was {end - start:.3f}")
            maxCheck = False # Optional Insert Line 18 to get all iterations
    end = time.time()
    
    print("FINAL RESULTS")
    print(f"Used tiles list is now \n{usedTiles}")
    print(f"Unexplored tiles at iteration {iteration - 1} are \n{unexploredTiles}")
    print(f"Explored tiles at iteration {iteration - 1} are \n{exploredTiles}")
    print(f"Time taken in seconds was {end - start:.3f}\n")


def eternityStart():
    # Input iteration at which cutoff should occur
    cut = 170
    createTile()
    findPatternMatches()
    startMatching(cut)

eternityStart()