class student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print("may")
        print(self.name)
    def __len__(self):
        return len(self.name)
p = student("hiououou")
p()
print(len(p))

class Test():
    def __len__(self):
        return 0
    print(bool(Test()))
