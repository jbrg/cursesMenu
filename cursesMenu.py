class cursesMenu:
    def __init__(self, topic):
        ## Screen setup ##
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.curs_set(0)
        self.stdscr.keypad(1)
        self.stdscr.addstr(0,0, topic)
        self.stdscr.addstr(1,0, ('-' * len(topic)))
        ## Main menu window ##
        self.mWin = curses.newwin(0,0,2,0)
        self.stdscr.refresh()
        ## Menu items and position markers ##
        self.items = []
        self.numberOfItems = 0
        self.currentItem = -1
    def addItem(self, item):
        self.mWin.addstr(self.numberOfItems,0, item)
        self.items.append(item)
        self.numberOfItems += 1
        self.mWin.refresh()
    def selectItem(self, direction):
        if direction == "up" and self.currentItem < (self.numberOfItems-1):
            if self.currentItem > -1:
                self.mWin.addstr(self.currentItem, 0, self.items[(self.currentItem)])
            self.currentItem += 1
            self.mWin.addstr(self.currentItem, 0, self.items[(self.currentItem)], curses.A_REVERSE)
        elif direction == "down" and self.currentItem > 0:
            self.mWin.addstr(self.currentItem, 0, self.items[(self.currentItem)])
            self.currentItem -= 1
            self.mWin.addstr(self.currentItem, 0, self.items[(self.currentItem)], curses.A_REVERSE)
        self.mWin.refresh()
