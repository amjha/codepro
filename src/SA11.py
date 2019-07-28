import sys

class Uniq:
    def __init__(self, str):
        self.str = str

    def checkUniq(self):
        k = self.str
        for i, item in enumerate(self.str):
            if i == len(self.str) - 1:
                return True
            if item in k[i+1:len(self.str)]:
                return False
        return True

a = Uniq(sys.argv[1])
print(a.checkUniq())
