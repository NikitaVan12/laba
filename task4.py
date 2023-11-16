class RealString:

    def __init__(self, word_one, word_two):
        self.word_one = word_one


    def __eq__(self, other):
        return len(self.word_one) == len(other.word_one)

    def __lt__(self, other):
        return len(self.word_one) < len(other.word_one)


x = RealString('asdas', 'фыв')
x1 = RealString('asdas', 'фыв')

print(x == x1)
