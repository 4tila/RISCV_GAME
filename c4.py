from numpy import array
with open('re_map_leo.data', 'r') as f: s=f.read()
s=s.split('.byte ')[1]
ls = s.split(',')
ls = [e for e in ls if e!='\n' and e!='']
ls = list(map(int, ls))
#print(list(set(ls))) # 0, 1, 2, 3, 8, 9, 10, 11, 12, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 44, 45, 46, 47, 54, 55, 72, 73, 80, 81, 82, 83, 84, 85, 88, 89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 106, 107, 108, 109, 110, 111, 115, 116, 117, 118, 119, 127, 144, 152, 153, 154, 160, 161, 162, 163, 164, 168, 169, 170, 171, 172, 173, 176, 177, 178, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 191, 233, 234, 240, 241, 242, 243, 244, 247, 249, 250, 251, 252, 253, 255]

w = 320
h = int(len(ls)/320)
print(h)
data = array(ls).reshape(h, w)
square=[[4*(12)+2, 4*(6)+2, 6, 112], [4*(12)+2, 4*(44)+2, 6, 136], [4*(25)+2, 4*(7)+2, 6, 66], [4*25+2, 4*22+2, 50, 2], [36*4+2, 4*22+2, 6, 16],\
        [4*(25)+2, 4*(7)+2, 170, 2], [4*66+2, 4*7+2, 40, 8], [48*4+2, 4*26+2, 4, 20], [50*4+2, 4*19+2, 4, 34], [50*4+2, 4*19+2, 66, 6],\
        [66*4+2, 4*18+2, 10, 6], [85*4+2, 4*18+2, 6, 60], [96*4+2, 1*4+2, 6, 70], [85*4+2, 18*4+2, 50, 2], [78*4+2, 1*4+2, 74, 2], [82*4+2, 32*4+2, 18, 8],\
        [82*4+2, 44*4+2, 18, 8], [85*4+2, 44*4+2, 6, 120], [29*4+2, 71*4+2, 194, 6], [35*4+2, 45*4+2, 10, 28],[46*4+2, 46*4+2, 20, 20], [39*4+2, 42*4+2, 28, 10],\
        [39*4+2, 52*4+2, 28, 10],[39*4+2, 54*4+2, 19, 10], [22*4+2, 56*4+2, 80, 5], [50*4+2, 56*4+2, 68, 6],\
        [66*4+2, 56*4+2, 6, 60], [82*4+2, 73*4+2, 20, 20]]

#square = [[e[0], e[1]-((e[1]+e[3])&3), e[2]-(e[2]&3), e[3]-(e[3]&3)] for e in square]

color = 43
#for s in square: 
#    for i in range(s[2]): data[s[0]+i][s[1]]=color
#    for i in range(s[3]): data[s[0]][s[1]+i]=color
#    for i in range(s[2]): data[s[0]+i][s[1]+s[3]]=color
#    for i in range(s[3]): data[s[0]+s[2]][s[1]+i]=color
for s in square: 
    for i in range(s[2]):
        for j in range(s[3]):
            data[s[0]+i][s[1]+j]=color
#432
for i in range(10):
    for j in range(10):
        data[370+i][20+j]=13
for i in range(320): data[398][i]=248
ls = data.reshape(h*w).tolist()
with open('re_map_leo_mod.data','w+') as f:
    f.write('re_map_leo: .byte ')
    f.write(str(ls)[1:-1])
