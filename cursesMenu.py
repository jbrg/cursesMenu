import curses

class MainMenu:
    def __init__(self, topic):
        """ Creates a handsome curses menu
        The constructor also sets up curses stuff, it's probably not a good idea to run this while running other curses stuff.
        Note that the terminal will enter a curses state when a object is created and it will not exit this state until destroy() is called.
        topic should be a string with a topic for the menu, a dashed line with the same lenght will be placed between the topic and the menu itself."""
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
    def getch(self):
        """ A little wrapper for curses.getch()"""
        return self.stdscr.getch()
    def destroy(self):
        """ This will the destroy the menu object and reset the terminal to it's previous state """
        curses.echo()
        curses.curs_set(0)
        self.stdscr.keypad(0)
        curses.endwin()
    def addItem(self, item):
        """ Add an item to the menu """
        self.mWin.addstr(self.numberOfItems,0, item)
        self.items.append(item)
        self.numberOfItems += 1
        self.mWin.refresh()
    def selectItem(self, direction):
        """ Cycle through the items. This also sets the id returned by getCurrentId """
        if direction == "up" and self.currentItem < (self.numberOfItems-1):
            if self.currentItem > -1:
                self.mWin.addstr(self.currentItem, 0, self.items[self.currentItem])
            self.currentItem += 1
            self.mWin.addstr(self.currentItem, 0, self.items[self.currentItem], curses.A_REVERSE)
        elif direction == "down" and self.currentItem > 0:
            self.mWin.addstr(self.currentItem, 0, self.items[self.currentItem])
            self.currentItem -= 1
            self.mWin.addstr(self.currentItem, 0, self.items[self.currentItem], curses.A_REVERSE)
        self.mWin.refresh()
    def getCurrentItemId(self):
        """ Returns a zero indexed id for the selected item or -1 if no item is selected """
        return self.currentItem
    def getItem(self, item="current"):
        """ Returns a string with the requested item or the current item if no id is given
        item should be a integer between 0 and self.numberOfItems """
        if item == "current":
            item = self.currentItem
        return self.items[item]
