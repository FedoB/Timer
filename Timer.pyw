TIME_START_DEF = "05:00"

try:
    if int(TIME_START_DEF[0]) in range(10) and int(TIME_START_DEF[1]) in range(10) and TIME_START_DEF[2] == ":" and int(TIME_START_DEF[3]) in range(10) and int(TIME_START_DEF[4]) in range(10):
        pass
    else:
        raise Exception()
except:
    TIME_START_DEF = "05:00"
    
import tkinter as tk
import time
import random, threading
import winsound
import math


def show_triangoli(d, boo):
    c1 = d["c1"]
    if boo:
    	c1.itemconfig(d["tri0"], state="normal")
    	c1.itemconfig(d["tri1"], state="normal")
    	c1.itemconfig(d["tri2"], state="normal")
    	c1.itemconfig(d["tri3"], state="normal")
    	c1.itemconfig(d["tri4"], state="normal")
    	c1.itemconfig(d["tri5"], state="normal")
    	c1.itemconfig(d["tri6"], state="normal")
    	c1.itemconfig(d["tri7"], state="normal")
    else:
    	c1.itemconfig(d["tri0"], state="hidden")
    	c1.itemconfig(d["tri1"], state="hidden")
    	c1.itemconfig(d["tri2"], state="hidden")
    	c1.itemconfig(d["tri3"], state="hidden")
    	c1.itemconfig(d["tri4"], state="hidden")
    	c1.itemconfig(d["tri5"], state="hidden")
    	c1.itemconfig(d["tri6"], state="hidden")
    	c1.itemconfig(d["tri7"], state="hidden")

class play(threading.Thread):
    def __init__(self, root, d):
        threading.Thread.__init__(self)
        self.root = root
        self.d = d
        self.event = threading.Event()
        
    def run(self):
        d = self.d
        minuti, secondi = d["time"].split(":")
        show_triangoli(d, False)
        while int(minuti) > 0 or int(secondi) > 0:
            time.sleep(1)
            minuti, secondi = d["time"].split(":")
            if self.event.is_set():
                break
            if int(secondi)>0:
                new_secondi = str(int(secondi)-1) if int(secondi)>10 else "0"+str(int(secondi)-1)
                new_minuti = minuti
            else:
                new_secondi = "59"
                new_minuti = str(int(minuti)-1) if int(minuti)>10 else "0"+str(int(minuti)-1)
            new_time = f"{new_minuti}:{new_secondi}"
            change_time(new_time, d)
            d["time"] = new_time
            minuti, secondi = new_time.split(":")
            if self.event.is_set():
                break
        else:
            self.root.nametowidget(".c2").thread = None
            self.root.nametowidget(".c2")["bg"] = "red"
            change_background(d)
            winsound.Beep(245, 200)
            time.sleep(0.01)
            winsound.Beep(500, 300)
            time.sleep(0.01)
            winsound.Beep(245, 200)
            time.sleep(0.01)
            winsound.Beep(500, 300)

def add_thirty(d):
    minuti, secondi = d["time"].split(":")
    new_secondi = int(secondi) + 30
    if new_secondi >= 60:
        new_secondi = new_secondi - 60
        new_minuti = int(minuti) + 1
    else:
        new_minuti = int(minuti)
    new_minuti = str(new_minuti) if len(str(new_minuti)) > 1 else "0"+str(new_minuti)
    new_secondi = str(new_secondi) if len(str(new_secondi)) > 1 else "0"+str(new_secondi)
    new_time = f"{new_minuti}:{new_secondi}"
    change_time(new_time, d)
    d["time"] = new_time

def playpause(root, d):
    if d["time"] == "00:00":
        reset(root, d)
        playpause(root, d)
        return

    if root.nametowidget(".c2").thread == None:
        root.nametowidget(".c2").itemconfig("playpause", fill="green", outline="green")
        t = play(root, d)
        t.daemon = True
        t.start()
        root.nametowidget(".c2").thread = t
    else:
        root.nametowidget(".c2").itemconfig("playpause", fill="red", outline="red")
        root.update()
        try:
            root.nametowidget(".c2").thread.event.set()
            root.nametowidget(".c2").thread.join()
            root.nametowidget(".c2").thread = None
        except:
            root.nametowidget(".c2").thread = None





def reset(root, d):
    if root.nametowidget(".c2").thread != None:
        root.nametowidget(".c2").thread.event.set()
        root.nametowidget(".c2").thread = None
    root.nametowidget(".c2")["bg"] = "red"
    
    default = root.title()
    d["time"] = default
    change_time(default, d)
    show_triangoli(d, True)


def change_background(d):
    c1 = d["c1"]
    '''
    bgs = ["#4c3056", "#0af5ad", "#42f515", "#a4effb", "#f2f943", "#80acce", "#0c6d69", "#38f652", "#731359", "#de2b06", "#b098ea", "#fb3a93", "#2403f3", "#9feecb", "#0d6c21", "#b2e40f", "#393656", "#4a0d21", "#75fad6"]
    try:
        bgs.remove(c1["bg"])
    except:
        pass
    c1["bg"] = random.choice(bgs)
    '''
    color = "#" + "".join(random.choices(list("0123456789abcdef"), k=6))
    c1["bg"] = color
    d["s_l"]["bg"] = color
    d["s_l"]["activebackground"] = color
    change_time(d["time"], d)

def opposite_color(c):
    s="#"
    for elem in c:
        s+="0" if elem == "f" else "1" if elem == "e" else "2" if elem == "d" else "3" if elem == "c" else "4" if elem == "b" else "5" if elem == "a" else "6" if elem == "9" else "7" if elem == "8" else "8" if elem == "7" else "9" if elem == "6" else "a" if elem =="5" else "b" if elem == "4" else "c" if elem == "3" else "d" if elem == "2" else "e" if elem == "1" else "f" if elem == "0" else ""
    return s

def change_number(boo, pos, d, root):
    times = list(d["time"])
    new_time = ""
    if boo and pos == "w":
        time0 = str(int(times[0])+1) if int(times[0])<9 else "0"
        new_time = time0 + times[1] + times[2] + times[3] + times[4]
    elif not boo and pos == "w":
        time0 = str(int(times[0])-1) if int(times[0])>0 else "9"
        new_time = time0 + times[1] + times[2] + times[3] + times[4]
    elif boo and pos == "x":
        time1 = str(int(times[1])+1) if int(times[1])<9 else "0"
        new_time = times[0] + time1 + times[2] + times[3] + times[4]
    elif not boo and pos == "x":
        time1 = str(int(times[1])-1) if int(times[1])>0 else "9"
        new_time = times[0] + time1 + times[2] + times[3] + times[4]
    elif boo and pos == "y":
        time3 = str(int(times[3])+1) if int(times[3])<5 else "0"
        new_time = times[0] + times[1] + times[2] + time3 + times[4]
    elif not boo and pos == "y":
        time3 = str(int(times[3])-1) if int(times[3])>0 else "5"
        new_time = times[0] + times[1] + times[2] + time3 + times[4]
    if boo and pos == "z":
        time4 = str(int(times[4])+1) if int(times[4])<9 else "0"
        new_time = times[0] + times[1] + times[2] + times[3] + time4
    elif not boo and pos == "z":
        time4 = str(int(times[4])-1) if int(times[4])>0 else "9"
        new_time = times[0] + times[1] + times[2] + times[3] + time4
    root.title(new_time)
    d["time"]=new_time
    change_time(new_time, d)

def change_time(str_time, d):
    times = list(str_time)
    set_time(times[0], "w", d)
    set_time(times[1], "x", d)
    set_time(times[3], "y", d)
    set_time(times[4], "z", d)

#n è una unità dell orario (mm:ss), pos indica quale canvas colorare (w,x,y,z), d è il dizionario che contiene i canvas
def set_time(n, pos, d):
    c1 = d["c1"]
    if n=="0":
        c1.itemconfig(d[pos+"0"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"1"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"2"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"3"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"4"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"5"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"6"], fill=opposite_color(c1["bg"]), outline="black")
    elif n=="1":
        c1.itemconfig(d[pos+"0"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"1"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"2"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"3"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"4"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"5"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"6"], fill=opposite_color(c1["bg"]), outline="black")
    elif n=="2":
        c1.itemconfig(d[pos+"0"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"1"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"2"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"3"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"4"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"5"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"6"], fill=c1["bg"], outline=c1["bg"])
    elif n=="3":
        c1.itemconfig(d[pos+"0"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"1"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"2"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"3"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"4"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"5"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"6"], fill=opposite_color(c1["bg"]), outline="black")
    elif n=="4":
        c1.itemconfig(d[pos+"0"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"1"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"2"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"3"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"4"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"5"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"6"], fill=opposite_color(c1["bg"]), outline="black")
    elif n=="5":
        c1.itemconfig(d[pos+"0"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"1"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"2"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"3"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"4"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"5"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"6"], fill=opposite_color(c1["bg"]), outline="black")
    elif n=="6":
        c1.itemconfig(d[pos+"0"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"1"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"2"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"3"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"4"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"5"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"6"], fill=opposite_color(c1["bg"]), outline="black")
    elif n=="7":
        c1.itemconfig(d[pos+"0"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"1"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"2"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"3"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"4"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"5"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"6"], fill=opposite_color(c1["bg"]), outline="black")
    elif n=="8":
        c1.itemconfig(d[pos+"0"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"1"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"2"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"3"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"4"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"5"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"6"], fill=opposite_color(c1["bg"]), outline="black")
    elif n=="9":
        c1.itemconfig(d[pos+"0"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"1"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"2"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"3"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"4"], fill=opposite_color(c1["bg"]), outline="black")
        c1.itemconfig(d[pos+"5"], fill=c1["bg"], outline=c1["bg"])
        c1.itemconfig(d[pos+"6"], fill=opposite_color(c1["bg"]), outline="black")

    c1.itemconfig(d["wxyz0"], fill=opposite_color(c1["bg"]))
    c1.itemconfig(d["wxyz1"], fill=opposite_color(c1["bg"]))
    
   
def cambia_lift(root, v):
    if v.get():
        root.attributes('-topmost', True)
        root.overrideredirect(True)
    else:
        root.attributes('-topmost', False)
        root.overrideredirect(False)

def draw_reset_icon(canvas):
    SIZE = 50           
    MARGIN = 8    
    COLOR = "gold"  
    LINE_WIDTH = 6
    CENTER = SIZE / 2
    RADIUS = (SIZE - 2 * MARGIN) / 2
    START_ANGLE = 200
    EXTENT = 240
    x0, y0 = CENTER - RADIUS, CENTER - RADIUS
    x1, y1 = CENTER + RADIUS, CENTER + RADIUS

    canvas.create_arc(
        x0, y0, x1, y1,
        start=START_ANGLE,
        extent=EXTENT,
        style="arc",
        outline=COLOR,
        width=LINE_WIDTH,
    )


    arrow_len = 10
    arrow_width = 7

    def draw_arrowhead(angle_deg, direction): 
        angle_rad = math.radians(angle_deg) 
        tip_x = CENTER + RADIUS * math.cos(angle_rad) 
        tip_y = CENTER - RADIUS * math.sin(angle_rad) 
        tangent_angle = angle_rad + direction * math.pi / 2 
        p_tip_x = tip_x + arrow_len * math.cos(tangent_angle) * 0.7 
        p_tip_y = tip_y - arrow_len * math.sin(tangent_angle) * 0.7 
        base_angle1 = tangent_angle + math.radians(140) 
        base_angle2 = tangent_angle - math.radians(140) 
        p1_x = tip_x + arrow_width * math.cos(base_angle1) + (-3 if direction > 0 else -4)
        p1_y = tip_y - arrow_width * math.sin(base_angle1) + (3 if direction > 0 else 1)
        p2_x = tip_x + arrow_width * math.cos(base_angle2) + (3 if direction < 0 else 3)
        p2_y = tip_y - arrow_width * math.sin(base_angle2) + (-3 if direction < 0 else -2)
        canvas.create_polygon( p_tip_x, p_tip_y, p1_x, p1_y, tip_x, tip_y, p2_x, p2_y, fill=COLOR, outline=COLOR, ) 
    
    draw_arrowhead(START_ANGLE, -1) 
    draw_arrowhead(START_ANGLE + EXTENT, 1)
    
    fill_pixel1_x = 29
    fill_pixel1_y = 12
    canvas.create_rectangle(fill_pixel1_x, fill_pixel1_y, fill_pixel1_x+1, fill_pixel1_y+1, fill="gold", width=0)

    fill_pixel2_x = 7
    fill_pixel2_y = 34
    canvas.create_rectangle(fill_pixel2_x, fill_pixel2_y, fill_pixel2_x+1, fill_pixel2_y+1, fill="gold", width=0)


def draw_play_pause_icon(canvas):
    
    def create_rounded_rect(canvas, x0, y0, x1, y1, radius, **kwargs):
        r = radius
        canvas.create_rectangle(x0 + r, y0, x1 - r, y1, outline="", **kwargs)
        canvas.create_rectangle(x0, y0 + r, x1, y1 - r, outline="", **kwargs)
        canvas.create_arc(x0, y0, x0 + 2 * r, y0 + 2 * r,
                           start=90, extent=90, style="pieslice",
                           outline="", **kwargs)
        canvas.create_arc(x1 - 2 * r, y0, x1, y0 + 2 * r,
                           start=0, extent=90, style="pieslice",
                           outline="", **kwargs)
        canvas.create_arc(x0, y1 - 2 * r, x0 + 2 * r, y1,
                           start=180, extent=90, style="pieslice",
                           outline="", **kwargs)
        canvas.create_arc(x1 - 2 * r, y1 - 2 * r, x1, y1,
                           start=270, extent=90, style="pieslice",
                           outline="", **kwargs)
    
    SIZE = 50                 
    BG_COLOR = "#000000"       
    FG_COLOR = "#ff0000"      
    CORNER_RADIUS = 0          
    PADDING = 8
    
    create_rounded_rect(
        canvas, 0, 0, SIZE, SIZE, CORNER_RADIUS,
        fill=BG_COLOR,
    )

    x0, y0 = PADDING, PADDING
    x1, y1 = SIZE - PADDING, SIZE - PADDING
    usable_w = x1 - x0

    gap = usable_w * 0.10
    half_w = (usable_w - gap) / 2

    play_x0 = x0
    play_x1 = x0 + half_w
    
    canvas.create_polygon(
        play_x0, y0,   
        play_x1, (y0 + y1) / 2, 
        play_x0, y1,
        fill=FG_COLOR,
        outline=FG_COLOR,
        joinstyle="round",
        tags = "playpause"
    )


    pause_x0 = play_x1 + gap
    bar_gap = half_w * 0.28
    bar_w = (half_w - bar_gap) / 2

    canvas.create_rectangle(
        pause_x0, y0,
        pause_x0 + bar_w, y1,
        fill=FG_COLOR, outline=FG_COLOR,
        tags = "playpause"
    )
    canvas.create_rectangle(
        pause_x0 + bar_w + bar_gap, y0,
        pause_x0 + bar_w + bar_gap + bar_w, y1,
        fill=FG_COLOR, outline=FG_COLOR,
        tags = "playpause"
    )

def add_menu(root):
    c1 = tk.Canvas(root, width=400, height=400, name="c1", borderwidth=0, bg="white", highlightthickness=0)
    c1.place(x=0, y=0)
    
    
    c2 = tk.Canvas(root, width=50, height=50, name="c2", borderwidth=0, bg="red", highlightthickness=0)
    draw_play_pause_icon(c2)
    c2.place(x=100, y=200)
    c2.thread = None


    c3 = tk.Canvas(root, width=50, height=50, name="c3", borderwidth=0, bg="black", highlightthickness=0)
    draw_reset_icon(c3)
    c3.place(x=250, y=200)

    coord_x = 40
    coord_y = 25

    #orizzontale: x0, y0, x0+50, y0+15
    w0 = c1.create_oval(coord_x, coord_y, coord_x+50, coord_y+15, outline="black", fill="white", width=2)
    w1 = c1.create_oval(coord_x, coord_y+65, coord_x+50, coord_y+65+15, outline="black", fill="white", width=2)
    w2 = c1.create_oval(coord_x, coord_y+130, coord_x+50, coord_y+130+15, outline="black", fill="white", width=2)
    
    #verticale: x0, y0, x0+15, y0+50
    w3 = c1.create_oval(coord_x-10, coord_y+15, coord_x-10+15, coord_y+15+50, outline="black", fill="white", width=2)
    w4 = c1.create_oval(coord_x+45, coord_y+15, coord_x+45+15, coord_y+15+50, outline="black", fill="white", width=2)
    w5 = c1.create_oval(coord_x-10, coord_y+80, coord_x-10+15, coord_y+80+50, outline="black", fill="white", width=2)
    w6 = c1.create_oval(coord_x+45, coord_y+80, coord_x+45+15, coord_y+80+50, outline="black", fill="white", width=2)

    coord_x += 80

    #orizzontale: x0, y0, x0+50, y0+15
    x0 = c1.create_oval(coord_x, coord_y, coord_x+50, coord_y+15, outline="black", fill="white", width=2)
    x1 = c1.create_oval(coord_x, coord_y+65, coord_x+50, coord_y+65+15, outline="black", fill="white", width=2)
    x2 = c1.create_oval(coord_x, coord_y+130, coord_x+50, coord_y+130+15, outline="black", fill="white", width=2)
    
    #verticale: x0, y0, x0+15, y0+50
    x3 = c1.create_oval(coord_x-10, coord_y+15, coord_x-10+15, coord_y+15+50, outline="black", fill="white", width=2)
    x4 = c1.create_oval(coord_x+45, coord_y+15, coord_x+45+15, coord_y+15+50, outline="black", fill="white", width=2)
    x5 = c1.create_oval(coord_x-10, coord_y+80, coord_x-10+15, coord_y+80+50, outline="black", fill="white", width=2)
    x6 = c1.create_oval(coord_x+45, coord_y+80, coord_x+45+15, coord_y+80+50, outline="black", fill="white", width=2)

    coord_x += 110

    #orizzontale: x0, y0, x0+50, y0+15
    y0 = c1.create_oval(coord_x, coord_y, coord_x+50, coord_y+15, outline="black", fill="white", width=2)
    y1 = c1.create_oval(coord_x, coord_y+65, coord_x+50, coord_y+65+15, outline="black", fill="white", width=2)
    y2 = c1.create_oval(coord_x, coord_y+130, coord_x+50, coord_y+130+15, outline="black", fill="white", width=2)
    
    #verticale: x0, y0, x0+15, y0+50
    y3 = c1.create_oval(coord_x-10, coord_y+15, coord_x-10+15, coord_y+15+50, outline="black", fill="white", width=2)
    y4 = c1.create_oval(coord_x+45, coord_y+15, coord_x+45+15, coord_y+15+50, outline="black", fill="white", width=2)
    y5 = c1.create_oval(coord_x-10, coord_y+80, coord_x-10+15, coord_y+80+50, outline="black", fill="white", width=2)
    y6 = c1.create_oval(coord_x+45, coord_y+80, coord_x+45+15, coord_y+80+50, outline="black", fill="white", width=2)

    coord_x += 80

    #orizzontale: x0, y0, x0+50, y0+15
    z0 = c1.create_oval(coord_x, coord_y, coord_x+50, coord_y+15, outline="black", fill="white", width=2)
    z1 = c1.create_oval(coord_x, coord_y+65, coord_x+50, coord_y+65+15, outline="black", fill="white", width=2)
    z2 = c1.create_oval(coord_x, coord_y+130, coord_x+50, coord_y+130+15, outline="black", fill="white", width=2)
    
    #verticale: x0, y0, x0+15, y0+50
    z3 = c1.create_oval(coord_x-10, coord_y+15, coord_x-10+15, coord_y+15+50, outline="black", fill="white", width=2)
    z4 = c1.create_oval(coord_x+45, coord_y+15, coord_x+45+15, coord_y+15+50, outline="black", fill="white", width=2)
    z5 = c1.create_oval(coord_x-10, coord_y+80, coord_x-10+15, coord_y+80+50, outline="black", fill="white", width=2)
    z6 = c1.create_oval(coord_x+45, coord_y+80, coord_x+45+15, coord_y+80+50, outline="black", fill="white", width=2)

    #due punti
    coord_x = 190
    coord_y = 127-65
    wxyz0 = c1.create_oval(coord_x, coord_y, coord_x+20, coord_y+20, outline="black", fill="white", width=2)
    wxyz1 = c1.create_oval(coord_x, coord_y+50, coord_x+20, coord_y+50+20, outline="black", fill="white", width=2)

    #otto triangoli
    tri0 = c1.create_polygon([40, 20, 65, 5, 90, 20], outline="black", fill="white", width=2)
    tri1 = c1.create_polygon([120, 20, 145, 5, 170, 20], outline="black", fill="white", width=2)
    tri2 = c1.create_polygon([230, 20, 255, 5, 280, 20], outline="black", fill="white", width=2)
    tri3 = c1.create_polygon([310, 20, 335, 5, 360, 20], outline="black", fill="white", width=2)
    tri4 = c1.create_polygon([40, 176, 65, 191, 90, 176], outline="black", fill="white", width=2)
    tri5 = c1.create_polygon([120, 176, 145, 191, 170, 176], outline="black", fill="white", width=2)
    tri6 = c1.create_polygon([230, 176, 255, 191, 280, 176], outline="black", fill="white", width=2)
    tri7 = c1.create_polygon([310, 176, 335, 191, 360, 176], outline="black", fill="white", width=2)
    
    # Checkbox root.attributes('-topmost', True)
    topCB = tk.IntVar()
    stay_lifted = tk.Checkbutton(root, variable = topCB, highlightthickness=0, command=lambda: cambia_lift(root, topCB))
    stay_lifted.place(x=5, y=5, width=20, height=15)
    topCB.set(0)

    dizionario = { "w0": w0, "w1": w1, "w2": w2, "w3": w3, "w4": w4, "w5": w5, "w6": w6, "x0": x0, "x1": x1, "x2": x2, "x3": x3, "x4": x4, "x5": x5, "x6": x6, "y0": y0, "y1": y1, "y2": y2, "y3": y3, "y4": y4, "y5": y5, "y6": y6, "z0": z0, "z1": z1, "z2": z2, "z3": z3, "z4": z4, "z5": z5, "z6": z6, "wxyz0": wxyz0, "wxyz1": wxyz1, "c1": c1, "time": TIME_START_DEF, "tri0": tri0, "tri1": tri1, "tri2": tri2, "tri3": tri3, "tri4": tri4, "tri5": tri5, "tri6": tri6, "tri7": tri7, "s_l": stay_lifted}

    change_background(dizionario)

    change_time(TIME_START_DEF, dizionario)

    c2.bind("<Button-1>", lambda event : playpause(root, dizionario))

    c3.bind("<Button-1>", lambda event : reset(root, dizionario))

    c1.tag_bind(tri0, "<Button-1>", lambda event: change_number(True, "w", dizionario, root))
    c1.tag_bind(tri1, "<Button-1>", lambda event: change_number(True, "x", dizionario, root))
    c1.tag_bind(tri2, "<Button-1>", lambda event: change_number(True, "y", dizionario, root))
    c1.tag_bind(tri3, "<Button-1>", lambda event: change_number(True, "z", dizionario, root))
    c1.tag_bind(tri4, "<Button-1>", lambda event: change_number(False, "w", dizionario, root))
    c1.tag_bind(tri5, "<Button-1>", lambda event: change_number(False, "x", dizionario, root))
    c1.tag_bind(tri6, "<Button-1>", lambda event: change_number(False, "y", dizionario, root))
    c1.tag_bind(tri7, "<Button-1>", lambda event: change_number(False, "z", dizionario, root))

    root.bind("<BackSpace>", lambda event: change_background(dizionario))

    root.bind("<space>", lambda event: playpause(root, dizionario))

    root.bind("<plus>", lambda event: add_thirty(dizionario))

    root.title(TIME_START_DEF)
    

    


def main():
    root = tk.Tk()
    root.geometry(f"{400}x{252}+{0}+{0}")
    root.configure(bg="white")
    root.resizable(False, False)
    add_menu(root)
    root.mainloop()
    
    
if __name__=="__main__":
    main()
