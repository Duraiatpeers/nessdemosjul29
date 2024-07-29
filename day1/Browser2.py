class Browser:

    # private variable
    # __isheadless = True

    # protected variable
    _isheadless = True

    def check_headless(self):
        if(self._isheadless):
            print('headless browser')
        else:
            print('Regular browser')


browser = Browser()
print(browser._isheadless)



