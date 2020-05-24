from tkinter import *
from winsound import *
import time


class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title('Timer')
        self.root.iconbitmap('icons/clock_hour_minute_second_time_timer_watch_icon_123193.ico')

        # create objects
        self.hours = Entry(self.root, width=4, borderwidth=5, justify='center', font=12)
        self.minutes = Entry(self.root, width=4, borderwidth=5, justify='center', font=12)
        self.seconds = Entry(self.root, width=4, borderwidth=5, justify='center', font=12)

        self.dots = Label(self.root, text=':', width=2, justify='center')
        self.Dots = Label(self.root, text=':', width=2, justify='center')
        self.lbl_time = Label(self.root, font=('calibri', 30, 'bold'), background='purple', foreground='white')
        self.lbl_empty = Label(self.root, text=' ', width=2)
        self.lbl_empty1 = Label(self.root, text=' ', width=2)

        self.start_button = Button(self.root, text='Start!', command=self.start_func)
        self.clear_button = Button(self.root, text='Clear', command=self.clear_func)
        self.pause_button = Button(self.root, text='Pause', command=self.pause_clock)
        self.continue_button = Button(self.root, text='Continue', command=self.continue_clock)

        self.sound_choice = IntVar(None, 1)

        self.sound_button_tone = Radiobutton(root, text='Tone', variable=self.sound_choice, value=1)
        self.sound_button_rooster = Radiobutton(root, text='Rooster', variable=self.sound_choice, value=2)
        self.sound_button_cuckoo_clock = Radiobutton(root, text='CuckooClock', variable=self.sound_choice, value=3)

        self.sound_onoff = IntVar()

        self.mute_checkbox = Checkbutton(self.root, text='Mute:', variable=self.sound_onoff)

        # Pack
        self.lbl_empty1.grid(row=0, column=0)
        self.hours.grid(row=0, column=1)
        self.dots.grid(row=0, column=2)
        self.minutes.grid(row=0, column=3)
        self.Dots.grid(row=0, column=4)
        self.seconds.grid(row=0, column=5)
        self.lbl_empty.grid(row=0, column=6)

        self.start_button.grid(row=0, column=7, sticky='wens', columnspan=2)
        self.clear_button.grid(row=1, column=7, sticky='wens', columnspan=2)
        self.pause_button.grid(row=2, column=7, sticky='wens', columnspan=2)
        self.continue_button.grid(row=3, column=7, sticky='wens', columnspan=2)

        self.lbl_time.grid(row=1, rowspan=3, column=0, columnspan=7, sticky='wens')

        self.sound_button_tone.grid(row=4, column=1, columnspan=1)
        self.sound_button_rooster.grid(row=4, column=2, columnspan=2)
        self.sound_button_cuckoo_clock.grid(row=4, column=4, columnspan=3)

        self.mute_checkbox.grid(row=4, column=7)

        self.hours.insert(0, '00')
        self.minutes.insert(0, '00')
        self.seconds.insert(0, '00')

    # buttons functions
    @staticmethod
    def pause_clock():
        global clock_running
        clock_running = False

    def start_func(self):
        global clock_running
        clock_running = True
        self.countdown(self.hours.get(), self.minutes.get(), self.seconds.get())

    def continue_clock(self):
        global clock_running
        clock_running = True

        self.countdown(clock_h, clock_m, clock_s)

    def clear_func(self):
        self.hours.delete(0, END)
        self.minutes.delete(0, END)
        self.seconds.delete(0, END)

        self.hours.insert(0, '00')
        self.minutes.insert(0, '00')
        self.seconds.insert(0, '00')

    # Time conversion help functions
    @staticmethod
    def convert_sec_to_time(time_left):
        hh = int(time_left / 3600)
        mm = int(((time_left / 3600) - hh) * 60)
        ss = round(((((time_left / 3600) - hh) * 60) - mm) * 60)

        return hh, mm, ss

    @staticmethod
    def con_time_to_sec(h, m, s):
        sec = (int(h) * 3600) + (int(m) * 60) + int(s)
        return sec

    # sound function
    @staticmethod
    def play(sound):
        print(sound.get())
        sound_dict = {
                      1: 'sounds/A-Tone-His_Self-1266414414.wav',
                      2: 'sounds/Rooster Crow-SoundBible.com-1802551702.wav',
                      3: 'sounds/Cuckoo Clock-SoundBible.com-1776874523.wav'
                      }

        PlaySound(str(sound_dict[sound.get()]), SND_FILENAME)

    # main clock countdown function
    def countdown(self, h, m, s):
        sec = int(self.con_time_to_sec(h, m, s))

        if time.perf_counter() < time.perf_counter() + sec and clock_running:

            global clock_h
            global clock_m
            global clock_s
            clock_h, clock_m, clock_s = self.convert_sec_to_time(sec)

            time_l = '{}:{}:{}'.format(clock_h, clock_m, clock_s)

            self.lbl_time.config(text=time_l)

            hh, mm, ss = self.convert_sec_to_time(sec - 1)
            self.lbl_time.after(1000, lambda: self.countdown(hh, mm, ss))

        elif clock_running and self.sound_onoff.get() == 0:
            self.play(self.sound_choice)
        else:
            pass


root = Tk()
my_timer1 = Clock(root)

mainloop()
