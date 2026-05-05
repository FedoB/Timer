image_dict = {
    't_reset.png': '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',
    't_pp.png': 'iVBORw0KGgoAAAANSUhEUgAAAeoAAAHqCAYAAADLbQ06AAAZHUlEQVR4nO3deYxV9dnA8XMYQEBHRBRaq9YFqE1rbGwjVkyhxaaJSqpSxSUUtCoibmFVC3XBXakiWlwRLSJaxG00NUALKaTQaqKJRsW1boi0Yqm1ijLn/eP1bXxbQYG59/eccz+f5EmM/8wzP+7Md85hLifPsqzIAICQ2qVeAADYMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAmufegGAjdlll12ynXbaKevUqVPdPuaaNWuylStXZqtXr67bx0zNOcdWGGNMlPnyl79cjBkzpvjDH/5QFEWRpZ65c+cWRx55ZPJzcc4NPckXMMaYonPnzsWkSZNCRGNDc/DBByc/J+fceJN/8h8Nq0uXLlmfPn2yrl27Zln2v7di3njjjexvf/tb4s2gcfTu3TtbsWJFnnqPL+LXv/51ceKJJ2br1q1Lvcomc87llfynhXrP7rvv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f4izZ88udtllF5GGLMteeuml7MQTTwz/dbsxvXr1Cr+/c66GogrTtWvXoiiKLOp897vfTX5GxkSciy66KPTX7oZm3333TX52zrlhJvkCbTZHHXVUuBfi8OHDi09u2RhjNjATJ04M97W7sdl7772Tn5lzbqhJvkCbzu233x7ihXjppZcWzc3Nyc/DmLLM0KFDQ3ztbmzmz59f9O7dO/lZOeeGm+QLtPmkfIHde++9xa677pr8DIwp65xwwgnFo48+Giom119/ffHNb34z+dk458acyvzW96d17do1e/fdd+v+W44/+MEPit///vf1/rBQSc3NzdkBBxyQ9ezZM9t5552zDh061O1jr1mzJlu5cmX2l7/8JfvTn/5Ut4+bgnMuh+Q/LdRiunTpUsyfP78uPy2eeuqpRVNTU/LP2RhjTCUn+QI1m6ampmLGjBk1i/W1115bdOvWLfnnaYwxptKTfIGaz5AhQ9o01o8++mjx9a9/PfnnZYwxpiEm+QJ1mx/96EfFggULtijaAwYMSP55GGOMaZyp5C+TfZ4+ffpkJ598cjZmzJjP/YWz5cuXF48++mg2b948/yY3AHXXkKH+tObm5qxPnz7ZNtts8//+/3vvvZc9/vjjibYCgP/V8KEGgMgq81AOAKgioQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAiqY8eOWZ5lWZF6EQDgs7miBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMCEGgACE2oACEyoASAwoQaAwIQaAAITagAITKgBIDChBoDAhBoAAhNqAAhMqAEgMKEGgMD+B3w49mxlR9hIAAAAAElFTkSuQmCC'}


import tkinter as tk
import time
from PIL import ImageTk, Image
import random, threading
import base64
from io import BytesIO
import winsound


TIME_START_DEF = "03:00"


image_cache = {}

def preload_images():        
    image_cache["t_pp"] = ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(image_dict["t_pp.png"]))).resize((50, 50), Image.LANCZOS))
    image_cache["t_reset"] = ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(image_dict["t_reset.png"]))).resize((50, 50), Image.LANCZOS))

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



def playpause(root, d):
    if d["time"] == "00:00":
        reset(root, d)
        playpause(root, d)
        return

    if root.nametowidget(".c2").thread == None:
        root.nametowidget(".c2")["bg"] = "green"
        t = play(root, d)
        t.daemon = True
        t.start()
        root.nametowidget(".c2").thread = t
    else:
        root.nametowidget(".c2")["bg"] = "red"
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


def add_menu(root):
    c1 = tk.Canvas(root, width=400, height=400, name="c1", borderwidth=0, bg="white", highlightthickness=0)
    c1.place(x=0, y=0)
    
    photo_pp = image_cache["t_pp"]
    c2 = tk.Canvas(root, width=50, height=50, name="c2", borderwidth=0, bg="red", highlightthickness=0)
    c2.image = photo_pp
    c2.image_id = c2.create_image(0, 0, image = photo_pp, anchor = tk.NW)
    c2.place(x=100, y=300)
    c2.thread = None

    photo_reset = image_cache["t_reset"]
    c3 = tk.Canvas(root, width=50, height=50, name="c3", borderwidth=0, bg="gold", highlightthickness=0)
    c3.image = photo_reset
    c3.image_id = c3.create_image(0, 0, image = photo_reset, anchor = tk.NW)
    c3.place(x=250, y=300)

    coord_x = 40
    coord_y = 90

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
    coord_y = 127
    wxyz0 = c1.create_oval(coord_x, coord_y, coord_x+20, coord_y+20, outline="black", fill="white", width=2)
    wxyz1 = c1.create_oval(coord_x, coord_y+50, coord_x+20, coord_y+50+20, outline="black", fill="white", width=2)

    #otto triangoli
    tri0 = c1.create_polygon([40,70, 65,50, 90,70], outline="black", fill="white", width=2)
    tri1 = c1.create_polygon([40+80,70, 65+80,50, 90+80,70], outline="black", fill="white", width=2)
    tri2 = c1.create_polygon([40+190,70, 65+190,50, 90+190,70], outline="black", fill="white", width=2)
    tri3 = c1.create_polygon([40+270,70, 65+270,50, 90+270,70], outline="black", fill="white", width=2)
    tri4 = c1.create_polygon([40,256, 65,276, 90,256], outline="black", fill="white", width=2)
    tri5 = c1.create_polygon([40+80,256, 65+80,276, 90+80,256], outline="black", fill="white", width=2)
    tri6 = c1.create_polygon([40+190,256, 65+190,276, 90+190,256], outline="black", fill="white", width=2)
    tri7 = c1.create_polygon([40+270,256, 65+270,276, 90+270,256], outline="black", fill="white", width=2)
    
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

    root.title(TIME_START_DEF)
    

    


def main():
    root = tk.Tk()
    preload_images()
    root.geometry(f"{400}x{400}")
    root.configure(bg="white")
    root.resizable(False, False)
    add_menu(root)
    root.mainloop()
    
    
if __name__=="__main__":
    main()