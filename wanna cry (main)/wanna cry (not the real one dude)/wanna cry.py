import tkinter as tk
import random, os, secrets, sys, webbrowser, playsound
#from pydub import AudioSegment       was used but now it is not
#from pydub.playback import play
from pygame import mixer



def encrypted():
    os.startfile(r"main\encrypted.txt")
    webbrowser.open_new_tab("tan-ailsun-38.tiiny.site")
    x= random.randint(1,2)
    if x==1:
        mixer.init()
        mixer.music.load("main\sound1.mp3")
        mixer.music.play(999)
    else:
        mixer.init()
        mixer.music.load("main\sound2.mp3")
        mixer.music.play(999)
        
def check_key():
    user_input = decryption_type.get()
    if user_input == key:
        print("you may close down now")
        mixer.init()
        mixer.music.load("main\minecraft-song.mp3")
        mixer.music.play(999)        
        sys.exit()
        exit()
        
    else:
        pass


def change():
    window.geometry("2x2+0+10000000000000")
    rand = random.choice(["left", "right", "top", "bottom"])
    new_window = tk.Toplevel(window)
    new_window.attributes("-topmost", False)
    new_window.overrideredirect(True)
    
    new_bg = tk.PhotoImage(file="main\$300 edit2.png")
    

    frame_top = tk.Frame(new_window, bg="#841011", highlightbackground="gray", highlightthickness=1)
    frame_top.pack(fill="both", expand=True)
    
    new_button = tk.Button(frame_top, text='X', font=("Arial", 12), bg="white", activebackground="red", command=change)
    encrypted_button = tk.Button(frame_top, text='files gone', font=("Arial", 12), bg="white", activebackground="red", command=encrypted)
    

    global decryption_type
    decryption_type = tk.Entry(frame_top)
    

    check_button = tk.Button(frame_top, text='Check Key', font=("Arial", 12), bg="white", activebackground="red", command=check_key)
    

    encrypted_button.grid(row=0, column=2, padx=5, pady=5)
    decryption_type.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    check_button.grid(row=0, column=1, padx=5, pady=5)
    new_button.grid(row=0, column=3, padx=5, pady=5)
    

    frame_top.columnconfigure(1, weight=1)
    
    new_label = tk.Label(frame_top, image=new_bg)
    new_label.image = new_bg
    new_label.grid(row=1, column=0, columnspan=4, sticky="nsew")
    
    height = window.winfo_screenheight() - 604
    width = window.winfo_screenwidth() - 811
    
    new_window.geometry(f"{813}x{606}+{random.randint(0, width)}+{random.randint(0, height)}")
    
    frame_top.bind('<ButtonPress-1>', lambda evt, win=new_window: on_mouse_press(evt, win))
    frame_top.bind('<B1-Motion>', lambda evt, win=new_window: on_mouse_drag(evt, win))

def on_mouse_press(evt, win):
    win.xp = evt.x
    win.yp = evt.y

def on_mouse_drag(evt, win):
    deltax = evt.x - win.xp
    deltay = evt.y - win.yp
    x = win.winfo_x() + deltax
    y = win.winfo_y() + deltay
    win.geometry(f"+{x}+{y}")


mixer.init()
mixer.music.load("main\main-song.mp3")
mixer.music.play(999)


window = tk.Tk()
window.attributes("-topmost", False)
window.overrideredirect(True)

window.bind('<ButtonPress-1>', lambda evt, win=window: on_mouse_press(evt, win))
window.bind('<B1-Motion>', lambda evt, win=window: on_mouse_drag(evt, win))


file = open("main\decrypt_key.txt", "r+")
data = file.readlines()
if data:
    data.pop(0)
global key
key = secrets.token_hex(8)
print(key)  # remove

file.seek(0)
file.truncate()
file.write(key)
file.close()
change()

window.mainloop()

# Note #
# This has not been made for malicious reasons but for learning and fun

# made by Neededwolf


