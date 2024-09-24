TYPELOAD=list()
POSITIONXLOAD=list()
POSITIONYLOAD=list()
ALIVELOAD=list()
AUX_AI0LOAD=list()
AUX_AI1LOAD=list()
AUX_AI2LOAD=list()
BARRIERLOAD=list()
SUCCESSLOAD=list()
FAILURELOAD=list()
HIDDENLOAD=list()
LOADRANGE=list()
LEVEL=[0xc]

def add(x, alive=1):
    global TYPELOAD, POSITIONXLOAD, POSITIONYLOAD, ALIVELOAD, AUX_AI0LOAD, AUX_AI1LOAD, AUX_AI2LOAD, BARRIERLOAD, SUCCESSLOAD, FAILURELOAD, HIDDENLOAD, LOADRANGE, LEVEL
    if x[0]=='level': # ['level', X, Y, barrier, success, failure, hidden]
        TYPELOAD+=     [0x0, 0x40, 0x40, 0x40, 0x80]
        POSITIONXLOAD+=[x[1], 0x0, 0x30, 0x40, 0x60] 
        POSITIONYLOAD+=[x[2], 0x0, 0x0, 0x0, 0x0]
        ALIVELOAD+=    [1, 1, 1, 1, 1]
        AUX_AI0LOAD+=  [0x0, 0x0, 0x0, 0x0, 0x0]
        AUX_AI1LOAD+=  [0x0, 0x0, 0x0, 0x0, 0x0]
        AUX_AI2LOAD+=  [0x0, 0x0, 0x0, 0x0, 0x0]
        BARRIERLOAD.append(x[3])
        SUCCESSLOAD.append(x[4])
        FAILURELOAD.append(x[5])
        HIDDENLOAD.append(x[6])
        if len(LOADRANGE)==0: LOADRANGE+=[0x0, 0x14]
        else: LOADRANGE+=[LOADRANGE[-2]+LOADRANGE[-1], 0x14]
    if x[0]=='char': # ['char', type, X, Y, AI0, AI1, AI2]
        TYPELOAD.append(x[1])
        POSITIONXLOAD.append(x[2])
        POSITIONYLOAD.append(x[3])
        ALIVELOAD.append(alive)
        AUX_AI0LOAD.append(x[4])
        AUX_AI1LOAD.append(x[5])
        AUX_AI2LOAD.append(x[6])
        LOADRANGE[-1]+=4
def word(ls): return '.word '+str(ls).replace('[', '').replace(']', '')
def variables():
    global TYPELOAD, POSITIONXLOAD, POSITIONYLOAD, ALIVELOAD, AUX_AI0LOAD, AUX_AI1LOAD, AUX_AI2LOAD, BARRIERLOAD, SUCCESSLOAD, FAILURELOAD, HIDDENLOAD, LOADRANGE, LEVEL
    print("TYPELOAD:	"+word(TYPELOAD))
    print("POSITIONXLOAD:	"+word(POSITIONXLOAD))
    print("POSITIONYLOAD:	"+word(POSITIONYLOAD))
    print("ALIVELOAD:	"+word(ALIVELOAD))
    print("AUX_AI0LOAD:	"+word(AUX_AI0LOAD))
    print("AUX_AI1LOAD:	"+word(AUX_AI1LOAD))
    print("AUX_AI2LOAD:	"+word(AUX_AI2LOAD))
    print("BARRIERLOAD:	"+word(BARRIERLOAD))
    print("SUCCESSLOAD:	"+word(SUCCESSLOAD))
    print("FAILURELOAD:	"+word(FAILURELOAD))
    print("HIDDENLOAD:	"+word(HIDDENLOAD))
    print("LOADRANGE:	"+word(LOADRANGE))
    print("LEVEL:	"+word(LEVEL))

# TODO change failure color

add(['level', 0x0, 320*40, 41, 0xF0, 248, 0xFF])
add(['char', 0x100, 0x0, 320*100, 3, 0, 0])
add(['char', 0x100, 0x10, 320*100, 3, 0, 0])
add(['char', 0x100, 0x50, 320*100, 3, 0, 0])
add(['char', 0x100, 0x60, 320*100, 3, 0, 0])
add(['char', 0x100, 0x100-32, 320*200, 3, 0, 0])
add(['char', 0x100, 0x110-32, 320*200, 3, 0, 0])
add(['char', 0x100, 0x100-32, 320*280, 3, 0, 0])
add(['char', 0x101, 0x110-32, 320*280, 3, 0, 0])
add(['char', 0x100, 0x100-60, 320*240, 3, 0, 0])
add(['char', 0x102, 0x100-60-16, 320*240, 3, 0, 0])

add(['char', 3, 0x30, 320*60, 3, 0, 0])
add(['char', 1, 0x70, 320*80, 10, 0, 0])
add(['char', 2, 0x100-40, 320*180, 10, 0, 0])
add(['char', 5, 0x100-40, 320*220, 10, 0, 0])
add(['char', 1, 0x100-40, 320*220, 10, 0, 0])


add(['level', 0x100, 320*40, 41, 0xF0, 248, 0xFF])
add(['char', 0x100, 0x100, 320*100, 0, 0, 0])
add(['char', 0x100, 0xf0, 320*100, 0, 0, 0])
add(['char', 0x100, 0xc0, 320*150, 0, 0, 0])
add(['char', 0x100, 0xb0, 320*150, 0, 0, 0])
add(['char', 0x100, 0x90, 320*200, 0, 0, 0])
add(['char', 0x100, 0x80, 320*200, 0, 0, 0])
add(['char', 0x100, 0x50, 320*220, 0, 0, 0])
add(['char', 0x100, 0x40, 320*220, 0, 0, 0])
add(['char', 0x100, 0x10, 320*240, 0, 0, 0])
add(['char', 0x101, 0x0, 320*240, 0, 0, 0])

add(['char', 6, 0x30, 320*60, 3, 0, 0])
add(['char', 7, 0xc0, 320*130, 10, 0, 0])
add(['char', 7, 0xe0, 320*130, 10, 0, 1])
add(['char', 8, 0x10, 320*220, 10, 0, 0])
add(['char', 8, 0x30, 320*220, 10, 0, 0])

add(['level', 0x100, 320*40, 41, 0xF0, 248, 0xFF])
add(['char', 0x100, 0x100, 320*100, 0, 0, 0])
add(['char', 0x100, 0xf0, 320*100, 0, 0, 0])
add(['char', 0x100, 0xc0, 320*150, 0, 0, 0])
add(['char', 0x100, 0xb0, 320*150, 0, 0, 0])
add(['char', 0x100, 0x100, 320*200, 0, 0, 0])
add(['char', 0x100, 0xf0, 320*200, 0, 0, 0])
add(['char', 0x100, 0xc0, 320*220, 0, 0, 0])
add(['char', 0x100, 0xb0, 320*220, 0, 0, 0])
add(['char', 0x101, 0x100, 320*240, 0, 0, 0])
add(['char', 0x100, 0xf0, 320*240, 0, 0, 0])

add(['char', 6, 0x30, 320*60, 3, 0, 0])
add(['char', 6, 0xc0, 320*130, 10, 0, 0])
add(['char', 9, 0xe0, 320*180, 10, 0, 1])
add(['char', 9, 0xc0, 320*200, 10, 0, 0])

add(['level', 0xc0, 320*100, 41, 0xF0, 248, 0xFF])
add(['char', 0x100, 0x100, 320*200, 0, 0, 0])
add(['char', 0x100, 0xf0, 320*200, 0, 0, 0])
add(['char', 0x100, 0xe0, 320*200, 0, 0, 0])
add(['char', 0x100, 0xd0, 320*200, 0, 0, 0])
add(['char', 0x100, 0xc0, 320*200, 0, 0, 0])
add(['char', 0x100, 0xb0, 320*200, 0, 0, 0])
add(['char', 0x100, 0xa0, 320*200, 0, 0, 0])
add(['char', 0x100, 0x90, 320*200, 0, 0, 0])
add(['char', 0x100, 0x80, 320*200, 0, 0, 0])
add(['char', 0x100, 0x70, 320*200, 0, 0, 0])

add(['char', 10, 0xe0, 320*180, 10, 0, 1])
add(['char', 12, 0x0, 320*100, 10, 0, 1], alive=0)
add(['char', 12, 0x0, 320*50, 10, 0, 1], alive=0)
add(['char', 12, 0x0, 320*10, 10, 0, 1], alive=0)
add(['char', 11, 0xe0, 320*180, 10, 0, 1], alive=0)
add(['char', 12, 0x100, 320*100, 10, 0, 1], alive=0)
add(['char', 12, 0x100, 320*50, 10, 0, 1], alive=0)
add(['char', 12, 0x100, 320*10, 10, 0, 1], alive=0)

variables()

