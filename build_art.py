from PIL import Image, ImageDraw, ImageFilter
import math, random

W = H = 1024
rng = random.Random(271828)
im = Image.new('RGB', (W, H), (7, 11, 35))
p = im.load()
for y in range(H):
    t = y / H
    for x in range(W):
        horizon = math.exp(-((y - 410) / 260) ** 2)
        glow = math.exp(-(((x - 610) / 500) ** 2 + ((y - 355) / 260) ** 2))
        p[x, y] = (int(8 + 18*glow + 14*t), int(12 + 30*glow + 12*t), int(40 + 55*glow + 45*t))
d = ImageDraw.Draw(im, 'RGBA')
# stars
for _ in range(260):
    x, y = rng.randrange(W), rng.randrange(570)
    a = rng.randrange(70, 220); r = rng.choice([1,1,1,2,3])
    d.ellipse((x-r,y-r,x+r,y+r), fill=(145,210,255,a))
# moon portal behind whale
for r in range(190, 20, -8):
    a = int(3 + (190-r)*0.35)
    d.ellipse((610-r,330-r,610+r,330+r), fill=(70,220,255,a))
d.ellipse((500,220,720,440), fill=(157,245,255,210), outline=(230,255,255,240), width=5)
# portal beam and crown flare: a second diagonal motion cue behind the whale
for width, alpha in [(120, 18), (76, 28), (38, 55)]:
    d.polygon([(580-width//2,225),(580+width//2,225),(750+width,700),(650-width,700)], fill=(70,220,255,alpha))
for i in range(12):
    ang = i * math.pi / 6
    x2, y2 = 610 + math.cos(ang)*155, 330 + math.sin(ang)*155
    d.line((610,330,x2,y2), fill=(198,255,255,170), width=3)
# storm clouds
for _ in range(85):
    x = rng.randrange(-80, 1080); y = rng.randrange(390, 690)
    rx, ry = rng.randrange(30,110), rng.randrange(16,55)
    d.ellipse((x-rx,y-ry,x+rx,y+ry), fill=(10,26,69,rng.randrange(100,220)))
# whale silhouette: sweeping body and tail
body = [(178,395),(235,330),(350,282),(500,286),(638,340),(734,407),(770,478),(700,516),(575,524),(452,500),(340,465),(248,450)]
d.polygon(body, fill=(20,33,72,255), outline=(104,236,255,255), width=9)
# luminous rib plates
for i in range(9):
    x = 295 + i*46
    d.arc((x-54,300+i*3,x+88,505-i*1), 205, 340, fill=(55,205,244,210), width=7)
# head crown and eye
d.polygon([(170,394),(110,370),(132,430),(205,449),(254,425)], fill=(19,40,82,255), outline=(170,255,255,255), width=6)
d.ellipse((154,382,184,412), fill=(255,245,133,255)); d.ellipse((163,389,178,404), fill=(255,103,44,255))
# fins
d.polygon([(420,470),(535,610),(570,490)], fill=(18,39,82,255), outline=(74,225,247,230), width=7)
d.polygon([(640,440),(790,555),(700,430)], fill=(18,39,82,255), outline=(74,225,247,230), width=7)
# tail flukes
d.polygon([(735,465),(860,390),(815,474),(902,535),(790,518)], fill=(18,38,78,255), outline=(102,240,255,240), width=8)
# engine sparks and wake
for _ in range(55):
    x = rng.randrange(230, 800); y = rng.randrange(460, 690)
    length = rng.randrange(10,60)
    d.line((x,y,x+rng.randrange(-15,16),y+length), fill=(68,226,255,rng.randrange(80,220)), width=rng.choice([2,3,5]))
# impossible terraces below
for level in range(5):
    y = 640 + level*58
    left = 110 - level*18; right = 930 + level*16
    d.polygon([(left,y),(right,y),(right-35,y+38),(left+35,y+38)], fill=(18,29+level*5,69+level*8,255), outline=(76,190,245,230), width=5)
    for x in range(left+35, right-20, 48):
        if rng.random() > .18:
            d.rectangle((x,y+8,x+12,y+24), fill=(255,194,77,230))
# tiny human silhouette at crown
hx, hy = 522, 624
d.ellipse((hx-7,hy-28,hx+7,hy-14), fill=(255,224,150,255))
d.line((hx,hy-14,hx,hy+18), fill=(255,224,150,255), width=5)
d.line((hx,hy-3,hx-15,hy+8), fill=(255,224,150,255), width=4)
d.line((hx,hy-3,hx+17,hy-12), fill=(255,224,150,255), width=4)
d.line((hx,hy+18,hx-12,hy+36), fill=(255,224,150,255), width=4)
d.line((hx,hy+18,hx+13,hy+33), fill=(255,224,150,255), width=4)
# foreground ocean lightning
for x in [90, 250, 890, 965]:
    pts=[(x,930),(x+18,875),(x-6,842),(x+30,780)]
    d.line(pts, fill=(94,238,255,210), width=4)
# title mark as visual glyph, not explanatory text
d.line((72,90,260,90), fill=(255,190,70,220), width=8)
d.line((72,90,72,138), fill=(255,190,70,220), width=8)
d.line((72,138,260,138), fill=(255,190,70,220), width=8)
d.text((82,100), 'STAR FORGE', fill=(220,250,255,230), stroke_width=1)
im.save('/home/ubuntu/makefun-remaining/excited-fresh/entry.png', optimize=True)
