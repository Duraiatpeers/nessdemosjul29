from abc import ABC,abstractmethod

class AbstractBrowser(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def closed(self):
        pass


class BrowserImpl(AbstractBrowser):

    def open(self):
        print('Browser launched')

    def closed(self):
        print('Browser closed')

# AbstractBrowser()
newbrowser = BrowserImpl()
newbrowser.open()
newbrowser.closed()

