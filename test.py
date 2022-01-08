import time
import curses
import locale

locale.setlocale(locale.LC_ALL, '')
code = locale.getpreferredencoding()

def pbar(window):
    for i in range(10):
        window.addstr(10, 10, "[" + ("=" * i) + ">" + (" " * (10 - i )) + "]")
        window.refresh()
        time.sleep(0.5)

curses.wrapper(pbar)