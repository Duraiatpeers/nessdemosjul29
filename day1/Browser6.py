class DemoA:
    def demomethod(self):
        print('DemoA')

class DemoB:
    def demomethod(self):
        print('DemoB')

class Demo:
    def demo(self,Obj):
        Obj.demomethod()

d = Demo()
d.demo(DemoB())