
# CreateTileSet.java
# Use separate class to create tile set
# May be able to replace with text file eventually
# Created: 13th February 2010 by Simon Schofield

class CreateTileSet:
    TILE_SET_SIZE = 256
    EDGE_SET_SIZE = 60
    PATTERN_TYPES = 22
    tileList = [] # Create list of tiles with index tilenumber and edges as 4 properties

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
       tileList.append((3,1,0,0))
       tileList.append((3,4,0,0))
       tileList.append((2,1,0,0))
       tileList.append((1,2,0,0))
       tileList.append((3,14,3,0))
       tileList.insert(6,(3,16,2,0))
       print(tileList[1])
       """
       tile[ 5 ] = new EternityTile( 5, 3, 14, 3, 0 );
       tile[ 6 ] = new EternityTile( 6, 3, 16, 2, 0 );
       tile[ 7 ] = new EternityTile( 7, 3, 17, 3, 0 );
       tile[ 8 ] = new EternityTile( 8, 3, 17, 5, 0 );
       tile[ 9 ] = new EternityTile( 9, 3, 10, 1, 0 );
       tile[ 10 ] = new EternityTile( 10, 3, 22, 4, 0 );
       tile[ 11 ] = new EternityTile( 11, 3, 18, 2, 0 );
       tile[ 12 ] = new EternityTile( 12, 3, 6 , 4, 0 );
       tile[ 13 ] = new EternityTile( 13, 3, 6 , 5, 0 );
       tile[ 14 ] = new EternityTile( 14, 3, 15, 4, 0 );
       tile[ 15 ] = new EternityTile( 15, 2, 16, 3, 0 );
       tile[ 16 ] = new EternityTile( 16, 2, 19, 1, 0 );
       tile[ 17 ] = new EternityTile( 17, 2, 11, 5, 0 );
       tile[ 18 ] = new EternityTile( 18, 2, 13, 5, 0 );
       tile[ 19 ] = new EternityTile( 19, 2, 22, 2, 0 );
       tile[ 20 ] = new EternityTile( 20, 2, 18, 2, 0 );
       tile[ 21 ] = new EternityTile( 21, 2, 21, 4, 0 );
       tile[ 22 ] = new EternityTile( 22, 2, 20, 3, 0 );
       tile[ 23 ] = new EternityTile( 23, 2, 20, 5, 0 );
       tile[ 24 ] = new EternityTile( 24, 2, 9 , 3, 0 );
       tile[ 25 ] = new EternityTile( 25, 2, 15, 3, 0 );
       tile[ 26 ] = new EternityTile( 26, 1, 14, 2, 0 );
       tile[ 27 ] = new EternityTile( 27, 1, 14, 1, 0 );
       tile[ 28 ] = new EternityTile( 28, 1, 16, 1, 0 );
       tile[ 29 ] = new EternityTile( 29, 1, 19, 1, 0 );
       tile[ 30 ] = new EternityTile( 30, 1, 22, 5, 0 );
       tile[ 31 ] = new EternityTile( 31, 1, 18, 2, 0 );
       tile[ 32 ] = new EternityTile( 32, 1, 9 , 1, 0 );
       tile[ 33 ] = new EternityTile( 33, 1, 6 , 2, 0 );
       tile[ 34 ] = new EternityTile( 34, 1, 6 , 4, 0 );
       tile[ 35 ] = new EternityTile( 35, 1, 8 , 5, 0 );
       tile[ 36 ] = new EternityTile( 36, 1, 7 , 4, 0 );
       tile[ 37 ] = new EternityTile( 37, 4, 19, 3, 0 );
       tile[ 38 ] = new EternityTile( 38, 4, 12, 5, 0 );
       tile[ 39 ] = new EternityTile( 39, 4, 10, 5, 0 );
       tile[ 40 ] = new EternityTile( 40, 4, 13, 2, 0 );
       tile[ 41 ] = new EternityTile( 41, 4, 13, 1, 0 );
       tile[ 42 ] = new EternityTile( 42, 4, 18, 3, 0 );
       tile[ 43 ] = new EternityTile( 43, 4, 18, 2, 0 );
       tile[ 44 ] = new EternityTile( 44, 4, 18, 1, 0 );
       tile[ 45 ] = new EternityTile( 45, 4, 21, 3, 0 );
       tile[ 46 ] = new EternityTile( 46, 4, 9 , 4, 0 );
       tile[ 47 ] = new EternityTile( 47, 4, 6 , 4, 0 );
       tile[ 48 ] = new EternityTile( 48, 4, 8 , 4, 0 );
       tile[ 49 ] = new EternityTile( 49, 5, 14, 5, 0 );
       tile[ 50 ] = new EternityTile( 50, 5, 16, 3, 0 );
       tile[ 51 ] = new EternityTile( 51, 5, 16, 2, 0 );
       tile[ 52 ] = new EternityTile( 52, 5, 17, 3, 0 );
       tile[ 53 ] = new EternityTile( 53, 5, 22, 4, 0 );
       tile[ 54 ] = new EternityTile( 54, 5, 21, 4, 0 );
       tile[ 55 ] = new EternityTile( 55, 5, 21, 5, 0 );
       tile[ 56 ] = new EternityTile( 56, 5, 6 , 1, 0 );
       tile[ 57 ] = new EternityTile( 57, 5, 8 , 3, 0 );
       tile[ 58 ] = new EternityTile( 58, 5, 8 , 5, 0 );
       tile[ 59 ] = new EternityTile( 59, 5, 15, 2, 0 );
       tile[ 60 ] = new EternityTile( 60, 5, 7 , 1, 0 );
       tile[ 61 ] = new EternityTile( 61, 17, 19, 14, 14 );
       tile[ 62 ] = new EternityTile( 62, 11, 22, 14, 14 );
       tile[ 63 ] = new EternityTile( 63, 16, 12, 14, 16 );
       tile[ 64 ] = new EternityTile( 64, 14, 6 , 14, 19 );
       tile[ 65 ] = new EternityTile( 65, 19, 7 , 14, 19 );
       tile[ 66 ] = new EternityTile( 66, 11, 11, 14, 19 );
       tile[ 67 ] = new EternityTile( 67, 10, 16, 14, 19 );
       tile[ 68 ] = new EternityTile( 68, 9 , 17, 14, 19 );
       tile[ 69 ] = new EternityTile( 69, 7 ,  6, 14, 19 );
       tile[ 70 ] = new EternityTile( 70, 12, 22, 14, 12 );
       tile[ 71 ] = new EternityTile( 71, 22, 20, 14, 12 );
       tile[ 72 ] = new EternityTile( 72, 11, 19, 14, 10 );
       tile[ 73 ] = new EternityTile( 73, 18, 21, 14, 10 );
       tile[ 74 ] = new EternityTile( 74, 9 , 18, 14, 10 );
       tile[ 75 ] = new EternityTile( 75, 6 , 12, 14, 10 );
       tile[ 76 ] = new EternityTile( 76, 11, 18, 14, 13 );
       tile[ 77 ] = new EternityTile( 77, 13, 18, 14, 13 );
       tile[ 78 ] = new EternityTile( 78, 12,  8, 14, 22 );
       tile[ 79 ] = new EternityTile( 79, 9 , 12, 14, 22 );
       tile[ 80 ] = new EternityTile( 80, 8 , 15, 14, 22 );
       tile[ 81 ] = new EternityTile( 81, 13, 19, 14, 18 );
       tile[ 82 ] = new EternityTile( 82, 19, 19, 14, 21 );
       tile[ 83 ] = new EternityTile( 83, 10, 21, 14, 21 ); 
       tile[ 84 ] = new EternityTile( 84, 19, 13, 14, 20 );
       tile[ 85 ] = new EternityTile( 85, 17, 11, 14, 20 );
       tile[ 86 ] = new EternityTile( 86, 6 , 20, 14, 20 );
       tile[ 87 ] = new EternityTile( 87, 8 , 9 , 14, 20 );
       tile[ 88 ] = new EternityTile( 88, 14, 15, 14,  9 );
       tile[ 89 ] = new EternityTile( 89, 17, 7 , 14,  9 );
       tile[ 90 ] = new EternityTile( 90, 21, 8 , 14,  9 );
       tile[ 91 ] = new EternityTile( 91, 10, 20, 14,  6 );
       tile[ 92 ] = new EternityTile( 92, 13, 18, 14,  6 );
       tile[ 93 ] = new EternityTile( 93, 13, 21, 14,  6 );
       tile[ 94 ] = new EternityTile( 94, 21, 15, 14,  6 );
       tile[ 95 ] = new EternityTile( 95, 20, 11, 14,  6 );
       tile[ 96 ] = new EternityTile( 96, 15, 12, 14, 15 );
       tile[ 97 ] = new EternityTile( 97, 21, 13, 14,  7 );
       tile[ 98 ] = new EternityTile( 98,  9,  6, 14,  7 );
       tile[ 99 ] = new EternityTile( 99, 15, 17, 14,  7 );
       tile[ 100 ] = new EternityTile( 100, 7, 15, 14, 7 );
       tile[ 101 ] = new EternityTile( 101, 20, 18, 16, 16 );
       tile[ 102 ] = new EternityTile( 102, 20,  8, 16, 16 );
       tile[ 103 ] = new EternityTile( 103,  8, 13, 16, 16 );
       tile[ 104 ] = new EternityTile( 104,  7, 17, 16, 16 );
       tile[ 105 ] = new EternityTile( 105, 21, 18, 16, 19 );
       tile[ 106 ] = new EternityTile( 106, 12,  6, 16, 17 );
       tile[ 107 ] = new EternityTile( 107, 13,  6, 16, 17 );
       tile[ 108 ] = new EternityTile( 108, 21, 18, 16, 17 );
       tile[ 109 ] = new EternityTile( 109,  8, 10, 16, 17 );
       tile[ 110 ] = new EternityTile( 110, 18, 20, 16, 11 );
       tile[ 111 ] = new EternityTile( 111, 20, 18, 16, 11 );
       tile[ 112 ] = new EternityTile( 112,  9, 13, 16, 12 );
       tile[ 113 ] = new EternityTile( 113,  9,  8, 16, 12 );
       tile[ 114 ] = new EternityTile( 114, 11, 21, 16, 10 );
       tile[ 115 ] = new EternityTile( 115, 22, 20, 16, 10 ); 
       tile[ 116 ] = new EternityTile( 116, 20, 10, 16, 10 );
       tile[ 117 ] = new EternityTile( 117,  7,  8, 16, 10 );
       tile[ 118 ] = new EternityTile( 118, 12, 15, 16, 13 );
       tile[ 119 ] = new EternityTile( 119,  8, 20, 16, 22 ); 
       tile[ 120 ] = new EternityTile( 120,  6,  7, 16, 18 );
       tile[ 121 ] = new EternityTile( 121, 11,  7, 16, 21 ); 
       tile[ 122 ] = new EternityTile( 122, 17,  8, 16,  9 );
       tile[ 123 ] = new EternityTile( 123, 11, 13, 16,  9 );
       tile[ 124 ] = new EternityTile( 124,  9, 18, 16,  9 );
       tile[ 125 ] = new EternityTile( 125, 20,  7, 16,  6 );
       tile[ 126 ] = new EternityTile( 126, 15, 18, 16,  6 );
       tile[ 127 ] = new EternityTile( 127, 11, 17, 16,  8 );
       tile[ 128 ] = new EternityTile( 128, 13, 15, 16,  8 );
       tile[ 129 ] = new EternityTile( 129, 21, 12, 16,  8 );
       tile[ 130 ] = new EternityTile( 130,  9,  6, 16,  8 );
       tile[ 131 ] = new EternityTile( 131, 17,  9, 16, 15 );
       tile[ 132 ] = new EternityTile( 132, 20, 11, 16, 15 );
       tile[ 133 ] = new EternityTile( 133, 11,  8, 16,  7 );
       tile[ 134 ] = new EternityTile( 134, 10, 21, 16,  7 );
       tile[ 135 ] = new EternityTile( 135, 21, 12, 16,  7 ); 
       tile[ 136 ] = new EternityTile( 136,  8,  9, 16,  7 );
       tile[ 137 ] = new EternityTile( 137,  9, 22, 19, 19 );
       tile[ 138 ] = new EternityTile( 138, 17, 12, 19, 17 );
       tile[ 139 ] = new EternityTile( 139, 19, 17, 17, 10 ); // centre tile with 19 top N in pos 120
       tile[ 140 ] = new EternityTile( 140, 17, 20, 19, 17 );
       tile[ 141 ] = new EternityTile( 141, 13, 15, 19, 17 );
       tile[ 142 ] = new EternityTile( 142, 18, 17, 19, 17 );
       tile[ 143 ] = new EternityTile( 143,  8, 20, 19, 17 ); 
       tile[ 144 ] = new EternityTile( 144, 15, 15, 19, 17 );
       tile[ 145 ] = new EternityTile( 145, 12, 21, 19, 11 );
       tile[ 146 ] = new EternityTile( 146, 19, 20, 19, 12 );
       tile[ 147 ] = new EternityTile( 147, 19,  7, 19, 12 );
       tile[ 148 ] = new EternityTile( 148, 12, 11, 19, 12 );
       tile[ 149 ] = new EternityTile( 149, 18, 20, 19, 12 );
       tile[ 150 ] = new EternityTile( 150, 17, 10, 19, 13 );
       tile[ 151 ] = new EternityTile( 151, 21,  7, 19, 13 );
       tile[ 152 ] = new EternityTile( 152, 10, 10, 19, 22 );
       tile[ 153 ] = new EternityTile( 153, 10, 13, 19, 22 );
       tile[ 154 ] = new EternityTile( 154,  7,  8, 19, 22 );
       tile[ 155 ] = new EternityTile( 155, 22, 22, 19, 21 );
       tile[ 156 ] = new EternityTile( 156, 22, 20, 19, 21 );
       tile[ 157 ] = new EternityTile( 157,  7, 22, 19, 21 );
       tile[ 158 ] = new EternityTile( 158, 22,  8, 19,  9 );
       tile[ 159 ] = new EternityTile( 159,  6, 17, 19,  9 );
       tile[ 160 ] = new EternityTile( 160, 15, 15, 19,  6 );
       tile[ 161 ] = new EternityTile( 161, 17,  9, 19,  8 );
       tile[ 162 ] = new EternityTile( 162, 11,  9, 19,  8 );
       tile[ 163 ] = new EternityTile( 163, 18, 10, 19,  7 );
       tile[ 164 ] = new EternityTile( 164, 21,  8, 19,  7 );
       tile[ 165 ] = new EternityTile( 165, 12, 21, 17, 11 );
       tile[ 166 ] = new EternityTile( 166, 21,  6, 17, 11 );
       tile[ 167 ] = new EternityTile( 167, 12, 12, 17, 10 );
       tile[ 168 ] = new EternityTile( 168, 10, 18, 17, 13 );
       tile[ 169 ] = new EternityTile( 169, 13, 15, 17, 13 );
       tile[ 170 ] = new EternityTile( 170, 21,  6, 17, 22 );
       tile[ 171 ] = new EternityTile( 171,  9,  8, 17, 22 );
       tile[ 172 ] = new EternityTile( 172, 15, 10, 17, 22 );
       tile[ 173 ] = new EternityTile( 173, 18, 18, 17, 18 );
       tile[ 174 ] = new EternityTile( 174, 20,  9, 17, 18 );
       tile[ 175 ] = new EternityTile( 175, 22, 15, 17, 21 ); 
       tile[ 176 ] = new EternityTile( 176, 22, 13, 17, 20 );
       tile[ 177 ] = new EternityTile( 177, 11, 21, 17,  9 );
       tile[ 178 ] = new EternityTile( 178, 20,  8, 17,  6 );
       tile[ 179 ] = new EternityTile( 179,  6, 18, 17,  6 );
       tile[ 180 ] = new EternityTile( 180, 22,  8, 17,  8 );
       tile[ 181 ] = new EternityTile( 181, 10,  8, 17, 15 ); //posn N3 (SW so 35) with 8 (diamond) N
       tile[ 182 ] = new EternityTile( 182, 22, 10, 17, 15 );
       tile[ 183 ] = new EternityTile( 183, 13,  6, 11, 11 );
       tile[ 184 ] = new EternityTile( 184,  7, 22, 11, 12 );
       tile[ 185 ] = new EternityTile( 185, 13, 20, 11, 10 );
       tile[ 186 ] = new EternityTile( 186,  6,  6, 11, 10 );
       tile[ 187 ] = new EternityTile( 187, 15, 22, 11, 13 );
       tile[ 188 ] = new EternityTile( 188, 11, 15, 11, 22 );
       tile[ 189 ] = new EternityTile( 189, 12, 13, 11, 22 );
       tile[ 190 ] = new EternityTile( 190,  8, 13, 11, 22 );
       tile[ 191 ] = new EternityTile( 191, 12, 12, 11, 18 );
       tile[ 192 ] = new EternityTile( 192, 18,  9, 11, 18 );
       tile[ 193 ] = new EternityTile( 193, 10, 22, 11, 21 );
       tile[ 194 ] = new EternityTile( 194, 15, 10, 11, 20 );
       tile[ 195 ] = new EternityTile( 195, 15,  7, 11, 20 );
       tile[ 196 ] = new EternityTile( 196,  7, 18, 11, 20 );
       tile[ 197 ] = new EternityTile( 197, 10,  7, 11,  9 );
       tile[ 198 ] = new EternityTile( 198, 13,  6, 11,  9 );
       tile[ 199 ] = new EternityTile( 199,  9,  9, 11,  9 );
       tile[ 200 ] = new EternityTile( 200, 13, 12, 11,  6 );
       tile[ 201 ] = new EternityTile( 201, 15,  6, 11,  8 );
       tile[ 202 ] = new EternityTile( 202,  7, 22, 11,  8 );
       tile[ 203 ] = new EternityTile( 203, 20, 13, 11, 15 );
       tile[ 204 ] = new EternityTile( 204, 20,  6, 11, 15 );
       tile[ 205 ] = new EternityTile( 205,  8, 12, 11, 15 );
       tile[ 206 ] = new EternityTile( 206,  7, 15, 11, 15 );
       tile[ 207 ] = new EternityTile( 207,  7, 22, 12, 12 );
       tile[ 208 ] = new EternityTile( 208, 13,  7, 12, 10 ); //posn C3 so 211 with 7 North
       tile[ 209 ] = new EternityTile( 209,  6, 18, 12, 10 );
       tile[ 210 ] = new EternityTile( 210, 10, 13, 12, 22 );
       tile[ 211 ] = new EternityTile( 211,  8, 18, 12, 22 );
       tile[ 212 ] = new EternityTile( 212, 12,  8, 12, 18 );
       tile[ 213 ] = new EternityTile( 213,  6,  6, 12, 21 );
       tile[ 214 ] = new EternityTile( 214, 12,  9, 12, 20 );
       tile[ 215 ] = new EternityTile( 215, 21,  7, 12, 20 );
       tile[ 216 ] = new EternityTile( 216,  7, 15, 12, 20 );
       tile[ 217 ] = new EternityTile( 217, 13, 18, 12,  9 );
       tile[ 218 ] = new EternityTile( 218, 21, 20, 12,  8 );
       tile[ 219 ] = new EternityTile( 219, 10, 21, 12, 15 );
       tile[ 220 ] = new EternityTile( 220, 10,  8, 12,  7 );
       tile[ 221 ] = new EternityTile( 221, 15, 15, 12,  7 );
       tile[ 222 ] = new EternityTile( 222, 15,  7, 12,  7 );
       tile[ 223 ] = new EternityTile( 223, 20,  7, 10, 10 );
       tile[ 224 ] = new EternityTile( 224,  9, 22, 10, 10 );
       tile[ 225 ] = new EternityTile( 225,  8, 18, 10, 10 );
       tile[ 226 ] = new EternityTile( 226, 13, 18, 10, 22 );
       tile[ 227 ] = new EternityTile( 227, 20, 20, 10, 22 );
       tile[ 228 ] = new EternityTile( 228, 13,  6, 10, 21 );
       tile[ 229 ] = new EternityTile( 229, 22,  7, 10,  9 );
       tile[ 230 ] = new EternityTile( 230,  8,  6, 10,  9 );
       tile[ 231 ] = new EternityTile( 231, 20,  9, 10,  6 );
       tile[ 232 ] = new EternityTile( 232, 20, 15, 10,  6 );
       tile[ 233 ] = new EternityTile( 233, 13,  9, 13, 13 );
       tile[ 234 ] = new EternityTile( 234,  8, 21, 13, 22 );
       tile[ 235 ] = new EternityTile( 235, 22, 21, 13, 21 );
       tile[ 236 ] = new EternityTile( 236, 22,  9, 13, 21 );
       tile[ 237 ] = new EternityTile( 237, 20, 18, 13, 21 );
       tile[ 238 ] = new EternityTile( 238, 21,  8, 13, 20 );
       tile[ 239 ] = new EternityTile( 239, 18,  7, 13,  9 );
       tile[ 240 ] = new EternityTile( 240, 15, 18, 13,  9 );
       tile[ 241 ] = new EternityTile( 241, 22, 15, 13,  6 );
       tile[ 242 ] = new EternityTile( 242, 21, 15, 13,  6 );
       tile[ 243 ] = new EternityTile( 243, 18, 20, 22, 18 );
       tile[ 244 ] = new EternityTile( 244,  9,  6, 22, 18 );
       tile[ 245 ] = new EternityTile( 245,  7,  9, 22, 21 );
       tile[ 246 ] = new EternityTile( 246,  8,  7, 22, 15 );
       tile[ 247 ] = new EternityTile( 247, 15,  7, 18, 18 );
       tile[ 248 ] = new EternityTile( 248, 20, 21, 18, 21 );
       tile[ 249 ] = new EternityTile( 249, 21, 15, 18, 20 ); // pon N14 so 46 and SE with 21 N side
       tile[ 250 ] = new EternityTile( 250,  8, 15, 18,  9 );
       tile[ 251 ] = new EternityTile( 251,  7,  6, 21, 21 );
       tile[ 252 ] = new EternityTile( 252,  6, 20, 21, 20 );
       tile[ 253 ] = new EternityTile( 253,  8,  9, 20,  6 );
       tile[ 254 ] = new EternityTile( 254, 15,  8,  9,  8 );
       tile[ 255 ] = new EternityTile( 255,  8,  7,  9,  7 ); //posn C14 (so 222 and NE) with 8 W side
       tile[ 256 ] = new EternityTile( 256, 15,  7,  6,  7 );
       """
