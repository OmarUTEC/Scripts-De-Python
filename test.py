class Cat:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "我是小猫[%s]" % self.name
    def __del__(self):
        print("%s 我去了..." % self.name)

tom = Cat("Tom")
print(tom)
