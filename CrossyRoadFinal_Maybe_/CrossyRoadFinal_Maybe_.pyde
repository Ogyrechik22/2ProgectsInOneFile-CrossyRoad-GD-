def col(x,y,w,h,x2,y2,w2,h2):
   if (x + w >= x2) and (x <= x2 + w2) and (y + h >= y2) and (y <= y2 + h2):
       return True
   else:
       return False
x = 475
y = 750
rand = 0
fir = -150
sec = -150
thir = -150
four = -150
five = -150
visota = 400
rand2 = 0
rand3 = 0
vod1 = -200
vod2 = -200
fir2 = 0
sec2 = 0
thir2 = 0
four2 = 0
five2 = 0
fir3 = 0
sec3 = 0
thir3 = 0
four3 = 0
five3 = 0
def setup():
    size(1000,1000)
def draw():
    global x,y,rand,fir,sec,thir,four,five,visota,rand2,rand3,vod1,vod2,fir2,sec2,thir2,four2,five2,fir3,sec3,thir3,four3,five3
    background(0,255,78)
    fill(1)
    rect(0,visota,1000,70)
    fill(255)
    rect(fir,visota,150,70)
    if col(fir,visota + 1,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 250,1000,70)
    fill(255)
    rect(sec,visota - 250,150,70)
    if col(sec,visota - 249,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 500,1000,70)
    fill(255)
    rect(thir,visota - 500,150,70)
    if col(thir,visota - 499,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 750,1000,70)
    fill(255)
    rect(four,visota - 750,150,70)
    if col(four,visota - 749,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 1000,1000,70)
    fill(255)
    rect(five,visota - 1000,150,70)
    if col(five,visota - 999,150,70,x,y,50,50):
        noLoop()
    fill(0,244,255)
    rect(0,visota - 1300,1000,200,100)
    fill(95,54,0)
    rect(vod1,visota - 1200,200,100)
    if col(vod1 - 10,visota - 1195,200,85,x,y,50,50):
        loop()
        x += 10
    vod1 += 5
    rect(vod2,visota - 1300,200,100)
    if col(vod2 - 10,visota - 1295,90,85,x,y,50,50):
        loop()
        x += 14
    vod2 += 7
    fill(1)
    rect(0,visota - 1800,1000,70)
    fill(255)
    rect(sec,visota - 1800,150,70)
    if col(sec,visota - 1799,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 2050,1000,70)
    fill(255)
    rect(thir,visota - 2050,150,70)
    if col(thir,visota - 2049,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 2400,1000,70)
    fill(255)
    rect(four,visota - 2400,150,70)
    if col(four,visota - 2399,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 2650,1000,70)
    fill(255)
    rect(five,visota - 2650,150,70)
    if col(five,visota - 2649,150,70,x,y,50,50):
        noLoop()
    fill(0,244,255)
    rect(0,visota - 2950,1000,200,100)
    fill(95,54,0)
    rect(vod1,visota - 2850,200,100)
    fill(1)
    rect(0,visota - 1550,1000,70)
    fill(255)
    rect(fir2,visota - 1550,250,70)
    if col(fir2,visota - 1549,250,70,x,y,50,50):
        noLoop()
    fill(255)
    rect(sec2,visota - 1800,150,70)
    if col(sec2,visota - 1799,150,70,x,y,50,50):
        noLoop()
    rect(thir2,visota - 2050,150,70)
    if col(thir2,visota - 2049,150,70,x,y,50,50):
        noLoop()
    rect(four2,visota - 2400,250,70)
    if col(four2,visota - 2399,250,70,x,y,50,50):
        noLoop()
    rect(five2,visota - 2650,300,70)
    if col(five2,visota - 2649,300,70,x,y,50,50):
        noLoop()
    fill(0,244,255)
    fill(95,54,0)
    rect(vod1,visota - 2850,200,100)
    if col(vod1 + 10,visota - 2845,200,85,x,y,50,50):
        loop()
        x += 10
    vod1 += 5
    rect(vod2,visota - 2950,200,100)
    if col(vod2 + 10,visota - 2945,200,85,x,y,50,50):
        loop()
        x += 14
    vod2 += 7
    fill(1)
    rect(0,visota - 3150,1000,70)
    fill(255)
    rect(sec,visota - 3150,150,70)
    if col(sec,visota - 3149,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 3400,1000,70)
    fill(255)
    rect(thir,visota - 3400,150,70)
    if col(thir,visota - 3399,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 3650,1000,70)
    fill(255)
    rect(four,visota - 3650,150,70)
    if col(four,visota - 3649,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 3900,1000,70)
    fill(255)
    rect(five,visota - 3900,150,70)
    if col(five,visota - 3899,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 4150,1000,70)
    fill(255)
    rect(fir2,visota - 4150,250,70)
    if col(fir2,visota - 4149,250,70,x,y,50,50):
        noLoop()
    rect(sec2,visota - 3150,150,70)
    if col(sec2,visota - 3149,150,70,x,y,50,50):
        noLoop()
    rect(thir2,visota - 3400,150,70)
    if col(thir2,visota - 3399,150,70,x,y,50,50):
        noLoop()
    rect(four2,visota - 3650,250,70)
    if col(four2,visota - 3649,250,70,x,y,50,50):
        noLoop()
    rect(five2,visota - 3900,300,70)
    if col(five2,visota - 3899,300,70,x,y,50,50):
        noLoop()
    rect(fir3,visota - 4150,300,70)
    if col(fir3,visota - 4149,300,70,x,y,50,50):
        noLoop()
    rect(sec3,visota - 3150,200,70)
    if col(sec3,visota - 3149,200,70,x,y,50,50):
        noLoop()
    rect(thir3,visota - 3400,250,70)
    if col(thir3,visota - 3399,250,70,x,y,50,50):
        noLoop()
    rect(four3,visota - 3650,250,70)
    if col(four3,visota - 3649,250,70,x,y,50,50):
        noLoop()
    rect(five3,visota - 3900,300,70)
    if col(five3,visota - 3899,300,70,x,y,50,50):
        noLoop()
    fill(255)
    rect(x,y,50,50)
    rand = random(26,28)
    rand = round(rand)
    rand2 = random(5,16)
    rand3 = random(16,35)
    fir += 5
    if rand == 27:
        sec += 8
    if rand == 27:
        thir += rand2
    if rand == 26:
        four += rand3
    five += rand2
    if fir > 1200:
        fir = -150
    if sec > 1200:
        sec = -150
    if thir > 1200:
        thir = -150
    if four > 1200:
        four = -150
    if five > 1200:
        five = -150
    if vod1 > 1200:
        vod1 = -200
    if vod2 > 1200:
        vod2 = -200
    if x > 1050:
        x = -200
    if fir2 > 1300:
        fir2 = -300
    if sec2 > 1200:
        sec2 = -200
    if thir2 > 1200:
        thir2 = -200
    if four2 > 1300:
        four2 = -300
    if five2 > 1350:
        five2 = -350
    if fir3 > 1300:
        fir3 = -300
    if sec3 > 1300:
        sec3 = -300
    if thir3 > 1300:
        thir3 = -300
    if four3 > 1300:
        four3 = -300
    if five3 > 1350:
        five3 = -350
    fir2 += 15
    sec2 += 15
    thir2 += 7
    four2 += 5
    five2 += 20
    fir3 += 25
    sec3 += 20
    thir3 += 17
    four3 += 14
    five3 += 30
def keyTyped():
    global x,y,rand,fir,sec,thie,four,five,visota
    if key == 'w' or key == 'W':
        visota += 50
    if key == 'a' or key == 'A':
        x -= 50
    if key == 'd' or key == 'D':
        x += 50
