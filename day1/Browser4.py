class Browser:

    def launch(self,browsertype):
        print(browsertype)

class ChromeBrowser:

    def __init__(self):
        print("Inside chrome browser")

    def __str__(self):
        print('Chrome Browser')

    def getType(self):
        return "chrome"

class EdgeBrowser:

    def __init__(self):
        print("Inside Edge browser")

    def __str__(self):
        print('Edge Browser')

    def getType(self):
        return "edge"

browser = Browser()

cbrowser = ChromeBrowser()
ebrowser = EdgeBrowser()

browser.launch(cbrowser.getType())
browser.launch(ebrowser.getType())

