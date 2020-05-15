from tkinter import *
from winsound import *
import time

root = Tk()
root.title('Timer')
root.iconbitmap('icons/clock_hour_minute_second_time_timer_watch_icon_123193.ico')


# sound function
def play(sound):
    print(sound.get())
    sound_dict = {
                  1: 'sounds/A-Tone-His_Self-1266414414.wav',
                  2: 'sounds/Rooster Crow-SoundBible.com-1802551702.wav',
                  3: 'sounds/Cuckoo Clock-SoundBible.com-1776874523.wav'
                  }
    PlaySound(str(sound_dict[sound.get()]), SND_FILENAME)


# Time conversion functions
def convert_sec_to_time(time_left):
    hh = int(time_left / 3600)
    mm = int(((time_left / 3600) - hh) * 60)
    ss = round(((((time_left / 3600) - hh) * 60) - mm) * 60)

    return hh, mm, ss


def con_time_to_sec(h, m, s):
    sec = h * 3600 + m * 60 + s
    return sec


# main clock countdown function
def countdown(h, m, s):
    sec = int(con_time_to_sec(h, m, s))

    if time.perf_counter() < time.perf_counter() + sec and clock_running:

        global clock_h
        global clock_m
        global clock_s
        clock_h, clock_m, clock_s = convert_sec_to_time(sec)

        time_l = '{}:{}:{}'.format(clock_h, clock_m, clock_s)

        lbl_time.config(text=time_l)

        hh, mm, ss = convert_sec_to_time(sec - 1)
        lbl_time.after(1000, lambda: countdown(hh, mm, ss))

    elif clock_running and sound_onoff.get() == 0:
        play(sound_choice)
    else:
        pass


# buttons functions
def start_func():
    global clock_running
    clock_running = True

    countdown(Hours.get(), Minutes.get(), Seconds.get())


def pause_clock():
    global clock_running
    clock_running = False


def continue_clock():
    global clock_running
    clock_running = True
    global clock_h
    global clock_m
    global clock_s
    countdown(clock_h, clock_m, clock_s)


def clear_func():
    Hours.delete(0, END)
    Minutes.delete(0, END)
    Seconds.delete(0, END)

    Hours.insert(0, '00')
    Minutes.insert(0, '00')
    Seconds.insert(0, '00')


# create objects
Hours = Entry(root, width=4, borderwidth=5, justify='center', font=12)
Minutes = Entry(root, width=4, borderwidth=5, justify='center', font=12)
Seconds = Entry(root, width=4, borderwidth=5, justify='center', font=12)

dots = Label(root, text=':', width=2, justify='center')
Dots = Label(root, text=':', width=2, justify='center')
lbl_time = Label(root, font=('calibri', 30, 'bold'), background='purple', foreground='white')
lbl_empty = Label(root, text=' ', width=2)
lbl_empty1 = Label(root, text=' ', width=2)

start_button = Button(root, text='Start!', command=start_func)
clear_button = Button(root, text='Clear', command=clear_func)
pause_button = Button(root, text='Pause', command=pause_clock)
continue_button = Button(root, text='Continue', command=continue_clock)

sound_choice = IntVar(None, 1)

sound_button_Tone = Radiobutton(root, text='Tone', variable=sound_choice, value=1)
sound_button_Rooster = Radiobutton(root, text='Rooster', variable=sound_choice, value=2)
sound_button_CuckooClock = Radiobutton(root, text='CuckooClock', variable=sound_choice, value=3)

sound_onoff = IntVar()

Mute_checkbox = Checkbutton(root, text='Mute:', variable=sound_onoff)

# Pack
lbl_empty1.grid(row=0, column=0)
Hours.grid(row=0, column=1)
dots.grid(row=0, column=2)
Minutes.grid(row=0, column=3)
Dots.grid(row=0, column=4)
Seconds.grid(row=0, column=5)
lbl_empty.grid(row=0, column=6)

start_button.grid(row=0, column=7, sticky='wens',  columnspan=2)
clear_button.grid(row=1, column=7, sticky='wens',  columnspan=2)
pause_button.grid(row=2, column=7, sticky='wens',  columnspan=2)
continue_button.grid(row=3, column=7, sticky='wens',  columnspan=2)

lbl_time.grid(row=1, rowspan=3,  column=0, columnspan=7, sticky='wens')

sound_button_Tone.grid(row=4, column=1,  columnspan=1)
sound_button_Rooster.grid(row=4, column=2, columnspan=2)
sound_button_CuckooClock.grid(row=4, column=4, columnspan=3)

Mute_checkbox.grid(row=4, column=7)

Hours.insert(0, '00')
Minutes.insert(0, '00')
Seconds.insert(0, '00')

mainloop()
