from Gui.tkmats.frames import TkMatsFrame
from Cycles.atp_pcb_cycle import ts_dict
from Gui.gui import *
import os
import sys
import webbrowser
from global_config import sockets


# Create an instance of a main window class to hold the main window.
class MainWindow:
    # Create the windows, frames, and buttons that will go into the main window.
    def __init__(self):
        # Create the main window and adjust position and size.
        self.window = tk.Tk()
        self.window.geometry("400x700+150+50")
        self.window.title("Testing Program")

        # Create a main frame
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        # Create a Canvas
        self.my_canvas = tk.Canvas(self.main_frame)
        self.my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add a Scrollbar to the Canvas
        my_scrollbar = ttk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the Canvas
        self.my_canvas.configure(yscrollcommand=my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Create a frame for the tests of socket 1.
        self.test1 = TkMatsFrame(self.my_canvas, ts_dict["ts1"], vertical=True, start_btn=sockets[0], socket_id=1)
        self.my_canvas.create_window((30, 198), window=self.test1, anchor="nw")

        # Create a frame for the tests of socket 2.
        self.test2 = TkMatsFrame(self.my_canvas, ts_dict["ts2"], vertical=True, start_btn=sockets[1], socket_id=2)
        self.my_canvas.create_window((143, 198), window=self.test2, anchor="nw")

        # Create a frame for the tests of socket 3.
        self.test3 = TkMatsFrame(self.my_canvas, ts_dict["ts3"], vertical=True, start_btn=sockets[2], socket_id=3)
        self.my_canvas.create_window((256, 198), window=self.test3, anchor="nw")

        # Create an exit button function to exit out of the program.
        def exit_button():
            sys.exit()

        # Create a reset button function  to reset all the tests and the entire program.
        def reset_button():
            # If you need to save the data before it is reset use the archive manager.save() function.
            python = sys.executable
            os.execl(python, python, *sys.argv)

        # Create a grafana button function to open grafana on chrome.
        def grafana_button():
            webbrowser.open("https://grafana.com/auth/sign-in")

        # Create the Valerann image and put it in a label and put the label on the canvas.
        photo = tk.PhotoImage(file=r"/Users/omrisokol/PycharmProjects/JigGui/Setup/AnyConv.com__valerannicon.gif")
        photoimage = photo.subsample(3, 3)
        label = tk.Label(self.my_canvas, text="", image=photoimage, compound=tk.LEFT)
        self.my_canvas.create_window((165, 0), window=label, anchor="nw")

        # Create a label for the nfc sticker reminder.
        nfc_label = tk.Label(self.my_canvas, text="""
        1. Put NFC Sticker\n     2. Connect PCBE\n            3. Connect Solar Panel\n
        """)
        nfc_label.config(font=("Courier", 18), foreground='red')
        self.my_canvas.create_window((-50, 60), window=nfc_label, anchor="nw")

        # Create the reset, grafana, and exit buttons and put them on the canvas.
        reset_btn = tk.Button(self.my_canvas, text='Reset', command=reset_button, width=17)
        exit_btn = tk.Button(self.my_canvas, text="Exit From Program", command=exit_button, width=39)
        grafana_btn = tk.Button(self.my_canvas, text="Open Grafana", command=grafana_button, width=18)
        self.my_canvas.create_window((30, 144), window=reset_btn, anchor="nw")
        self.my_canvas.create_window((30, 171), window=exit_btn, anchor="nw")
        self.my_canvas.create_window((197, 144), window=grafana_btn, anchor="nw")

        # Run the main() method from gui.py which opens the logging window and outputs the results on the window.
        main()

        # Run the mainloop of the window to open it when the program is run.
        self.window.mainloop()


MainWindow()
