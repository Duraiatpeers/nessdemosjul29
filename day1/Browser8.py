class Browser:

    isheadless = True

    def __init__(self):
        print(self.isheadless)

    def checkheadless(self):
        print(self.isheadless)

    @classmethod
    def launch(cls):
        cls.isheadless = False
        print(cls.isheadless)

    @classmethod
    def close(cls):
        print('closed')
        print(cls.isheadless)

br = Browser()
br.checkheadless()
Browser.launch()
br.checkheadless()
