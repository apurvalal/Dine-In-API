class Menu(object):
    def __init__(self):
        self.indian = {}
        self.chinese = {}
        self.continental = {}

    def setIndian(self, indian):
        self.indian = indian

    def getIndian(self):
        return self.indian

    def setChinese(self, chinese):
        self.chinese = chinese

    def getChinese(self):
        return self.chinese

    def setContinental(self, continental):
        self.continental = continental

    def getContinental(self):
        return self.continental
    