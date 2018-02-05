"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Rachel Wood.
"""  # DONE 1.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()
    # ------------------------------------------------------------------
    # DONE 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(root, padding=20)
    frame1.grid()
    # ------------------------------------------------------------------
    # DONE 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    aaahhhh_button = ttk.Button(frame1, text='AAAHHHH')
    aaahhhh_button.grid()
    # ------------------------------------------------------------------
    # DONE 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    aaahhhh_button['command'] = (lambda: print('hello'))
    # You can also do that via a function but meh
    # ------------------------------------------------------------------
    # DONE 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -----------------------------------------------------------------

    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    print_entry_button = ttk.Button(frame1, text='Print entry')
    print_entry_button['command'] = (lambda:
                                     print_contents(my_entry_box))
    print_entry_button.grid()


    # ------------------------------------------------------------------
    # TODO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    my_num_box = ttk.Entry(frame1)
    my_num_box.grid()

    print_entry_button = ttk.Button(frame1, text='Print number')

    num_box = my_num_box.get()
    num = int(num_box)

    for k in range(num):
        print_entry_button['command'] = (lambda:
                                     (print_contents(my_entry_box)))
    print_entry_button.grid()

    root.mainloop()


    # ------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------


def print_contents(entry_box):
    """
    Prints onto the Console the contents of the given ttk.Entry.

    In this example, it is used as the function that is "CALLED BACK"
    when an event (namely, the pressing of a certain Button) occurs.

    Type hints:
      :type entry_box: ttk.Entry
    """
    contents_of_entry_box = entry_box.get()
    print(contents_of_entry_box)

def print_contents_muti(entry_box, num):
    """
    Prints onto the Console the contents of the given ttk.Entry.

    In this example, it is used as the function that is "CALLED BACK"
    when an event (namely, the pressing of a certain Button) occurs.

    Type hints:
      :type entry_box: ttk.Entry
    """
    contents_of_entry_box = entry_box.get()
    for k in range (num):
        print(contents_of_entry_box)
# -----------------------------------------
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
