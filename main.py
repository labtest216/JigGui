from tkmats import TkMatsFrame
import tkinter as tk
from Cycles.atp_pcb_cycle import ts1

window = tk.Tk()
tkate_frame = TkMatsFrame(window, ts1, vertical=True)
tkate_frame.grid()
window.mainloop()