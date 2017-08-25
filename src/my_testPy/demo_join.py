
class Demo:
    def __init__(self, data, name):
        self.data = [12]
        self.name = "dai"
    def print_test(self):
        print self.data
        print self.name

d = Demo([33],"jitao")
d.print_test()

class car():
    def call(self):
        print "car parent"
class mycar(car):
    def call(self):
        print "car zub"

my = mycar()
my.call()