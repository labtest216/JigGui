from tkinter import *
from tkinter.ttk import Frame, Label
from Gui.gui import *

from mats import Test, TestSequence

_light_green = '#66ff66'
_light_red = '#ff6666'
_light_yellow = '#ffff99'
_relief = 'sunken'
_label_padding = 5
_green = '#49c447'
_red = '#f02e2e'
_yellow = '#f2e311'
_black = '#000000'
_gray = '#A09795'


# Create a frame to hold all the tests for each socket.
class TkMatsFrame(Frame):
    # Create an instance of a frame for each socket.
    def __init__(self, parent, sequence: TestSequence,
                 vertical=False, start_btn=True, socket_id=1,
                 loglevel=logging.INFO):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(loglevel)
        self.socket_id = socket_id
        self._start = 0

        self._parent = parent
        super().__init__(self._parent)

        self._sequence = sequence

        # Changing the style from aqua to classic
        style = ttk.Style()
        style.theme_use('classic')

        arrow = '\u2b9e' if not vertical else '\u2b9f'

        row = 0
        col = 0

        # Define a start button function to start the sequence when it is pressed and then disable it after its pressed.
        def start_button():
            self._start += 1
            # Starting the test sequence.
            self._sequence.start()

            # Reconfiguring the start and stop buttons so they are ready for use after this button is pressed.
            tk.Button(self, text='Stop', command=stop_button).grid(row=1, column=col, sticky='news')
            tk.Button(self, text='Start').grid(row=0, column=col, sticky='news')

        # Create a start button and display it if specified in the init function.
        if start_btn:
            tk.Button(self, text='Start', command=start_button).grid(row=row, column=col, sticky='news')

        # Creating a function that does something as the stop button is being pressed.
        def function_while_stopping():
            print(self.socket_id)

        # Creating the stop button function.
        def stop_button():
            # Function that stops and aborts the program
            self._sequence.abort()

            # Function that executes an action as the program is stopped.
            function_while_stopping()

            # Reconfiguring the start and stop buttons so they are ready for use after this button is pressed.
            tk.Button(self, text='Start', command=start_button).grid(row=0, column=col, sticky='news')
            tk.Button(self, text='Stop').grid(row=1, column=col, sticky='news')

        # Displaying an initial stop button on the screen.
        tk.Button(self, text='Stop').grid(row=row+1, column=col, sticky='news')

        # If the frame is not specified as vertical, present it nicely.
        if not vertical:
            col += 1 if not vertical else 0
            row += 1 if vertical else 0
            Label(self, text=arrow, justify='center', anchor='center').grid(row=row, column=col, sticky='news')

        col += 1 if not vertical else 0
        row += 1 if vertical else 0

        # Create a test label for each test in each socket by using _TestLabel class.
        self._test_status_frames = []
        for test in self._sequence.tests:
            self._test_status_frames.append(
                _TestLabel(self, test, vertical=vertical)
            )

        # Display each test label in the same column as the socket.
        for i, tl in enumerate(self._test_status_frames):
            col += 1 if not vertical else 0
            row += 1 if vertical else 0

            tl.grid(row=row+1, column=col, sticky='news')

            if not vertical:
                col += 1 if not vertical else 0
                row += 1 if vertical else 0

                Label(self, text=arrow, justify='center', anchor='center').grid(row=row, column=col, sticky='news')

        col += 1 if not vertical else 0
        row += 1 if vertical else 0

        # Create and display the label for the status of the test.
        self._complete_label = Label(self, text='-', anchor='center', justify='center')
        self._complete_label.grid(row=2, column=col, sticky='news')
        self._complete_label.config(relief=_relief, padding=_label_padding)

        # Update the tests.
        self._update()

    # A function in order to update the status of the tests over time as the program is run.
    def _update(self):
        # Update the status of the tests depending on if the tests passed or failed.
        if self._sequence.in_progress:
            self._complete_label.config(text='in progress', background=_yellow, foreground=_black)
        elif self._sequence.is_aborted:
            self._complete_label.config(text='aborted', background=_red, foreground=_black)
        elif self._sequence.ready and self._start == 0:
            self._complete_label.config(text='None', background=_gray, foreground=_black)
        elif self._sequence.is_passing:
            self._complete_label.config(text='pass', background=_green, foreground=_black)
        else:
            self._complete_label.config(text='fail', background=_red, foreground=_black)

        self.after(100, self._update)


# Create a test label class in order to create a label for each test.
class _TestLabel(Label):
    # A single instance of a test label frame.
    def __init__(self, parent, test: Test, vertical: bool, loglevel=logging.INFO):
        self._logger = logging.getLogger(self.__class__.__name__)
        self._logger.setLevel(loglevel)

        self._parent = parent
        super().__init__(self._parent)

        self._test = test

        # Changing the style from aqua to classic
        style = ttk.Style()
        style.theme_use('classic')

        if not vertical:
            self._label_text = self._test.moniker.replace(' ', '\n')
        else:
            self._label_text = self._test.moniker
        self.config(text=self._label_text, relief=_relief, padding=_label_padding)

        self._label_bg_color = self.cget('background')

        self._update()

    # Updates the test label display based on the status of the Test
    def _update(self):
        color = self._label_bg_color

        if self._test.status == 'waiting':
            color = self._label_bg_color
        elif self._test.status == 'running':
            color = _yellow
        elif self._test.status == 'aborted':
            color = _red
        elif not self._test.is_passing:
            color = _red
        elif self._test.is_passing:
            color = _green

        value = self._test.value
        if isinstance(value, float):
            value_str = f'{value: .03f}'
        else:
            try:
                value_str = f'{value.magnitude: .03f}'
            except AttributeError:
                value_str = f'{value}'

        if value_str and len(value_str) < 12:
            label_text = f'{self._label_text}\n({value_str})'
        else:
            label_text = self._label_text

        # Change the color of the background and text of the test label depending on its status.
        self.config(background=color, text=label_text, foreground=_black)

        self.after(100, self._update)
