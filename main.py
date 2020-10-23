from tkinter import *
from tkinter import font
import sys
from winsound import *
import hanoi

counter = 3
no_of_ring = ""
move_counter = ""


class Solution_window:
    def __init__(self):
        self.soln = Tk()
        self.soln.iconbitmap("Images\\tower_of_hanoi.ico")
        bold = font.Font(size=20)
        self.soln.title("Tower of Hanoi")
        self.soln.geometry('1000x650')
        self.soln.configure(bg="black")

        def close():
            PlaySound("Sounds\\Click.wav", SND_FILENAME)
            self.soln.destroy()                         # Closes solution window
            Start_window_class()                        # Opens start window

        self.menu_button = Button(self.soln, text = "MENU", borderwidth = 0, bg = "blue", font = bold, command = close).place(x= 450, y= 500)
        self.soln_screen = Label(self.soln, bg="white", height = 25, width = 100).place(x = 150, y =50)

        self.soln.mainloop()

class Main_window:

    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap("Images\\tower_of_hanoi.ico")
        bold = font.Font(size=20)
        self.root.title("Tower of Hanoi")
        self.root.geometry('1000x750')
        self.root.configure(bg= "black")
        self.moves_played = 0
        self.min_moves = 0

        global min_moves

        self.towers = PhotoImage(file="Images\\towers.png")
        self.ring_1 = PhotoImage(file="Images\\Blue.png")
        self.ring_2 = PhotoImage(file="Images\\FRed.png")  # Images for rings and towers
        self.ring_5 = PhotoImage(file="Images\\Green.png")
        self.ring_3 = PhotoImage(file="Images\\Orange.png")
        self.ring_4 = PhotoImage(file="Images\\Yellow.png")

        # self.invalid_move = lambda: PlaySound('Sounds\\Wrong.wav', SND_FILENAME)

        self.display = Canvas(height=400, width=950)  # Canvas to post images
        self.display.pack()

        self.xr1 = 160  # Location of blue ring in first tower
        self.yr1 = 325

        self.xr2 = 160  # Location of red ring in first tower
        self.yr2 = 325

        self.xr3 = 160  # Location of orange ring in first tower
        self.yr3 = 325
        # Distance between two towers 320px
        self.xr4 = 160  # Location of yellow ring in first tower
        self.yr4 = 325

        self.xr5 = 160  # Location of green ring in first tower
        self.yr5 = 325

        self.display.create_image(480, 160, image=self.towers)
        if counter == 3:
            disp_ring_1 = self.display.create_image(self.xr1, self.yr1 - 30, image=self.ring_1)
            disp_ring_2 = self.display.create_image(self.xr2, self.yr2 - 15, image=self.ring_2)  # Displaying images of rings
            disp_ring_3 = self.display.create_image(self.xr3, self.yr3, image=self.ring_3)
            self.min_moves = 7
            ring_dict = {1: [disp_ring_1, self.xr1, self.yr1, self.ring_1], 2: [disp_ring_2, self.xr2, self.yr2, self.ring_2],
                         3: [disp_ring_3, self.xr3, self.yr3, self.ring_3]}
        elif counter == 4:
            disp_ring_1 = self.display.create_image(self.xr1, self.yr1 - 45, image=self.ring_1)
            disp_ring_2 = self.display.create_image(self.xr2, self.yr2 - 30, image=self.ring_2)  # Displaying images of rings
            disp_ring_3 = self.display.create_image(self.xr3, self.yr3 - 15, image=self.ring_3)
            disp_ring_4 = self.display.create_image(self.xr4, self.yr4, image=self.ring_4)
            self.min_moves = 15
            ring_dict = {1: [disp_ring_1, self.xr1, self.yr1, self.ring_1], 2: [disp_ring_2, self.xr2, self.yr2, self.ring_2],
                         3: [disp_ring_3, self.xr3, self.yr3, self.ring_3], 4: [disp_ring_4, self.xr4, self.yr4, self.ring_4]}
        elif counter == 5:
            disp_ring_1 = self.display.create_image(self.xr1, self.yr1 - 60, image=self.ring_1)
            disp_ring_2 = self.display.create_image(self.xr2, self.yr2 - 45, image=self.ring_2)  # Displaying images of rings
            disp_ring_3 = self.display.create_image(self.xr3, self.yr3 - 30, image=self.ring_3)
            disp_ring_4 = self.display.create_image(self.xr4, self.yr4 - 15, image=self.ring_4)
            disp_ring_5 = self.display.create_image(self.xr5, self.yr5, image=self.ring_5)
            self.min_moves = 31
            ring_dict = {1: [disp_ring_1, self.xr1, self.yr1, self.ring_1], 2: [disp_ring_2, self.xr2, self.yr2, self.ring_2],
                         3: [disp_ring_3, self.xr3, self.yr3, self.ring_3], 4: [disp_ring_4, self.xr4, self.yr4, self.ring_4],
                         5: [disp_ring_5, self.xr5, self.yr5, self.ring_5]}

        Hanoi = hanoi.Hanoi(counter)

        def getsoln(self):
            PlaySound("Sounds\\Click.wav", SND_FILENAME)
            self.root.destroy()  # Closes main window
            Solution_window()  # Opens solution window




        def changes(self, src, dest):
            try:
                src, dest, rings_in_tow, ring_no = Hanoi.move(src, dest)
            except:
                PlaySound('Sounds\\Wrong.wav', SND_FILENAME)
                return

            PlaySound('Sounds\\Button_press.wav', SND_FILENAME)
            rings_in_tow -= 1
            self.moves_played += 1
            self.display.delete(self.move_counter)
            self.move_counter = self.display.create_text(920, 380, text=self.moves_played, font=font.Font(size=20, weight="bold"))
            if dest == "Tower 1":
                self.display.delete(ring_dict[ring_no][0])
                ring_dict[ring_no][0] = self.display.create_image(ring_dict[ring_no][1], ring_dict[ring_no][2] - (rings_in_tow * 15), image = ring_dict[ring_no][3])
            elif dest == "Tower 2":
                self.display.delete(ring_dict[ring_no][0])
                ring_dict[ring_no][0] = self.display.create_image(ring_dict[ring_no][1]+320, ring_dict[ring_no][2] - (rings_in_tow * 15), image = ring_dict[ring_no][3])
            elif dest == "Tower 3":
                self.display.delete(ring_dict[ring_no][0])
                ring_dict[ring_no][0] = self.display.create_image(ring_dict[ring_no][1]+640, ring_dict[ring_no][2] - (rings_in_tow * 15), image = ring_dict[ring_no][3])

            if Hanoi.won() == True:
                self.display.create_text(480, 100, text="You Won!", font=font.Font(size=50, weight="bold"),
                                         fill="green")
                self.one_to_two = Button(self.root, text='1 ➡ 2', width=5, borderwidth=0, bg="red", font=bold,
                                         command=lambda: changes(self, 1, 2), state = DISABLED).place(x=130, y=550)
                self.one_to_three = Button(self.root, text='1 ➡ 3', width=5, borderwidth=0, bg="red", font=bold,
                                           command=lambda: changes(self, 1, 3), state = DISABLED).place(x=130, y=650)
                self.two_to_one = Button(self.root, text='2 ➡ 1', width=5, borderwidth=0, bg="red", font=bold,
                                         command=lambda: changes(self, 2, 1), state = DISABLED).place(x=460, y=550)
                self.two_to_three = Button(self.root, text='2 ➡ 3', width=5, borderwidth=0, bg="red", font=bold,
                                           command=lambda: changes(self, 2, 3), state = DISABLED).place(x=460, y=650)
                self.three_to_two = Button(self.root, text='3 ➡ 1', width=5, borderwidth=0, bg="red", font=bold,
                                           command=lambda: changes(self, 3, 1), state = DISABLED).place(x=770, y=550)
                self.three_to_one = Button(self.root, text='3 ➡ 2 ', width=5, borderwidth=0, bg="red", font=bold,
                                           command=lambda: changes(self, 3, 2), state = DISABLED).place(x=770, y=650)

        def exit():
            PlaySound('Sounds\\Click.wav', SND_FILENAME)
            sys.exit()

        def reset(self):
            PlaySound("Sounds\\Click.wav", SND_FILENAME)
            self.root.destroy()
            Main_window()

        def menu(self):
            PlaySound("Sounds\\Click.wav", SND_FILENAME)
            self.root.destroy()
            Start_window_class()


        self.display.create_text(100, 380, text="Min. Move: ", font=font.Font(size=20, weight="bold"))
        self.display.create_text(180, 380, text=self.min_moves, font=font.Font(size=20, weight="bold"))
        self.display.create_text(800, 380, text="Moves Played: ", font=font.Font(size=20, weight="bold"))
        self.move_counter = self.display.create_text(900, 380, text=self.moves_played, font=font.Font(size=20, weight="bold"))
        self.display.create_text(160, 30, text="1", font=font.Font(size=20, weight="bold"))
        self.display.create_text(480, 30, text="2", font=font.Font(size=20, weight="bold"))
        self.display.create_text(800, 30, text="3", font=font.Font(size=20, weight="bold"))


        self.one_to_two = Button(self.root, text='1 ➡ 2', width = 5, borderwidth=0, bg="red", font=bold, command = lambda: changes(self, 1, 2)).place(x=130, y=550)
        self.one_to_three = Button(self.root, text='1 ➡ 3', width = 5, borderwidth=0, bg="red", font=bold, command = lambda: changes(self, 1, 3)).place(x=130, y=650)
        self.two_to_one = Button(self.root, text='2 ➡ 1', width = 5, borderwidth=0, bg="red", font=bold, command = lambda: changes(self, 2, 1)).place(x=460, y=550)
        self.two_to_three = Button(self.root, text='2 ➡ 3', width = 5,borderwidth=0, bg="red", font=bold, command = lambda: changes(self, 2, 3)).place(x=460, y=650)
        self.three_to_two = Button(self.root, text='3 ➡ 1', width = 5, borderwidth=0, bg="red", font=bold, command = lambda: changes(self, 3, 1)).place(x=770, y=550)
        self.three_to_one = Button(self.root, text='3 ➡ 2 ', width = 5, borderwidth=0, bg="red", font=bold, command = lambda: changes(self, 3, 2)).place(x=770, y=650)
        self.solution = Button(self.root, text='Solution', borderwidth=0, bg="green", font=bold, command =lambda : getsoln(self)).place(x=860, y=0)
        self.exit = Button(self.root, text='X', borderwidth=0, bg="red", font=bold, command=exit).place(x=0, y=0)
        self.reset = Button(self.root, text = "RESET", borderwidth=0, width = 6, bg="blue", font=bold, command = lambda: reset(self)).place(x=282, y=450)
        self.menu = Button(self.root, text = "MENU", borderwidth=0, width = 6, bg="blue", font=bold, command = lambda: menu(self)).place(x=612, y=450)
        self.root.mainloop()



class Start_window_class:
    def __init__(self):
        self.start = Tk()
        self.start.iconbitmap("Images\\tower_of_hanoi.ico")
        global counter          # Holds the number of rings
        global no_of_ring       # Displays the number of rings

        def gotoMain():
            PlaySound('Sounds\\Click.wav', SND_FILENAME)
            self.start.destroy()
            Main_window()

        def increment():
            global counter
            global no_of_ring

            PlaySound("Sounds\\Click.wav", SND_FILENAME)

            counter += 1
            start_window.delete(no_of_ring)         # Deletes the number of ring (integer) from page and creates new on the line below
            no_of_ring = start_window.create_text(170, 335, text=counter, font=font.Font(size=30, weight="bold"))
            if counter < 5:                                                             # Enable disable button according to condition that 3 <= number of rings <= 5
                self.increment_button = Button(self.start, text="+", height=1, width=1, borderwidth=0, font=bold, bg="#352029", fg="white", command=increment).place(x=190, y=310)
            else:
                self.increment_button = Button(self.start, text="+", height=1, width=1, borderwidth=0, font=bold, bg="#352029", fg="white", state=DISABLED, command=increment).place(x=190, y=310)
            if counter > 3:
                self.decrement_button = Button(self.start, text="-", height=1, width=1, borderwidth=0, font=bold, bg="#352029", fg="white", command=decrement).place(x=120, y=310)
            else:
                self.decrement_button = Button(self.start, text="-", height=1, width=1, borderwidth=0, font=bold, state=DISABLED, bg="#352029", fg="white", command=decrement).place(x=120, y=310)

        def decrement():
            global counter
            global no_of_ring

            PlaySound("Sounds\\Click.wav", SND_FILENAME)

            counter -= 1
            start_window.delete(no_of_ring)
            no_of_ring = start_window.create_text(170, 335, text=counter, font=font.Font(size=30, weight="bold"))
            if counter < 5:
                self.increment_button = Button(self.start, text="+", height=1, width=1, borderwidth=0, font=bold, bg="#352029", fg="white", command=increment).place(x=190, y=310)
            else:
                self.increment_button = Button(self.start, text="+", height=1, width=1, borderwidth=0, font=bold, bg="#352029", fg="white", state=DISABLED, command=increment).place(x=190, y=310)
            if counter > 3:
                self.decrement_button = Button(self.start, text="-", height=1, width=1, borderwidth=0, font=bold, bg="#352029", fg="white", command=decrement).place(x=120, y=310)
            else:
                self.decrement_button = Button(self.start, text="-", height=1, width=1, borderwidth=0, font=bold, state=DISABLED, bg="#352029", fg="white", command=decrement).place(x=120, y=310)

        def exit():
            PlaySound('Sounds\\Click.wav', SND_FILENAME)
            sys.exit()

        bold = font.Font(size=20)
        start_bg = PhotoImage(file="Images\\start_bg_image.png")
        self.start.title("Tower of Hanoi")
        self.start.geometry('1000x650')
        start_window = Canvas(height=650, width=1000)
        start_window.pack()
        start_window.create_image(480, 350, image=start_bg)                 #421E1B
        start_window.create_text(200, 250, text="NUMBER OF RINGS", font = font.Font(size = 30, weight = "bold"))

        if counter < 5:
            self.increment_button = Button(self.start, text = "+", height = 1, width = 1, borderwidth = 0, font = bold, bg = "#352029", fg = "white", command = increment).place(x = 190, y = 310)
        else:
            self.increment_button = Button(self.start, text="+", height=1, width=1, borderwidth=0, font=bold, bg="#352029", fg="white", state = DISABLED, command=increment).place(x=190, y=310)
        if counter > 3:
            self.decrement_button = Button(self.start, text = "-", height = 1, width = 1, borderwidth = 0, font = bold, bg = "#352029", fg = "white", command = decrement).place(x = 120, y = 310)
        else:
            self.decrement_button = Button(self.start, text="-", height=1, width=1, borderwidth=0, font=bold, state = DISABLED,  bg="#352029", fg="white", command=decrement).place(x=120, y=310)


        no_of_ring = start_window.create_text(170, 335, text=counter, font=font.Font(size=30, weight="bold"))

        self.start_button = Button(self.start, text = "START", borderwidth = 0, font = bold, bg = "green", command = gotoMain).place(x=350, y=500)
        self.exit_button = Button(self.start, text = "EXIT", borderwidth = 0, font =  bold, bg = "red", command = exit).place(x = 550, y = 500)  # Exits the program
        self.start.mainloop()

q = Start_window_class()
