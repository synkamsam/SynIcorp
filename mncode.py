import ttkbootstrap as ttb
from widgets import *

wnd = ttb.Window(themename='darkly')
wnd.title('Syntaxik Finance')

"""Create menu"""
create_menu(wnd)
create_button(wnd)
create_date(wnd)
create_tree(wnd)
accgridder(wnd)

















wnd.mainloop()