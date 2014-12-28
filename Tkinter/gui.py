import sys
import os
from Tkinter import *
import tkMessageBox

CWD = os.getcwd()

BASE = os.path.basename(CWD)

sys.path.append(CWD.replace(BASE, ''))

from l2python.pickle_test.pickle_test import Animal

# TEXT = ''

# # functions
# def reply():
    # tkMessageBox.showinfo('popup title', 'oh this is just the message box')

# prints all the entry box items
def print_items():
    print 'Animal: %s' % entry1.get()
    print 'Noise: %s' % entry2.get()
    print 'Color: %s' % entry3.get()
    print '\n'
# # end function


# # instances
window = Tk()

# # end instances


# objects

# PANES
top = PanedWindow()
top.pack()

mid = PanedWindow()
mid.pack()

bot = PanedWindow()
bot.pack()

# button = Button(window, text='press me!', command=reply)
label1 = Label(top, text='Animal')
top.add(label1)
# label1.pack(fill=X, side=LEFT)
# label1.pack()

entry1 = Entry(top)
# entry1.pack()
# entry1.pack(fill=X, side=RIGHT)
top.add(entry1)

label2 = Label(mid, text='Noise')
mid.add(label2)
# label2.pack(side=LEFT)

entry2 = Entry(mid)
# entry2.pack(side=LEFT)
mid.add(entry2)

label3 = Label(bot, text='Color')
# label3.pack(side=LEFT)
bot.add(label3)

entry3 = Entry(bot)
# entry3.pack(side=LEFT)
bot.add(entry3)

submit = Button(window, text='Create Animal', command=print_items)
# submit.pack()
submit.pack(side=BOTTOM)

# end objects


# packings
# button.pack()

window.mainloop()
