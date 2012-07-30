import curses
import cursesMenu

mainMenu = cursesMenu.MainMenu("Example menu")

exampleList = ["Example 1", "Example 2", "Example 3", "Example 4"]

for x in exampleList:
    mainMenu.addItem(x)

while True:
    c = mainMenu.getch()
    if c == ord('q'):
        mainMenu.destroy()
        break
    elif c == curses.KEY_DOWN: mainMenu.selectItem("up")
    elif c == curses.KEY_UP: mainMenu.selectItem("down")
    elif c == curses.KEY_RIGHT:
        mainMenu.destroy()
        print("You chose: " + mainMenu.getItem())
        break

