class Browser:

    def __init__(self):
        print('Inside browser constructor')

    def launch(self):
        print('browser launched')

class ChromiumBrowser:

    def __init__(self):
        print('Inside ChromiumBrowser constructor')

    def launch(self):
        print('ChromiumBrowser launched')

class ChromeBrowser(ChromiumBrowser,Browser):
    def __init__(self):
        # to call super class
        super().__init__()
        print('Inside chrome browser constructor')
    #
    # def launch(self):
    #     print('chrome browser launched')

cbrowser = ChromeBrowser()
cbrowser.launch()
