# class definition
class Browser:

    isheadless = True

    # constructor
    # overloading not allowed, it will override
    def __init__(self):
        print('Inside constructor')

    def __init__(self,msg):
        print(msg)

    # Destructor
    def __del__(self):
        print('End of object life')

    # methods
    # def launch(self):
    #     print('browser is launched')

    def launch(self,browsername):
        print(f"{browsername} browser is launched")

    def close(self):
        print('browser is closed')

# object creation

browser2 = Browser("Chrome")
# browser1 = Browser()

browser2.launch("Chrome")
browser2.close()
print(browser2.isheadless)


# def add(*args):
#     print('add')
#
# add(1)
# add(1,2)
# add(1,2,3)
# add(1,2,3,4)
