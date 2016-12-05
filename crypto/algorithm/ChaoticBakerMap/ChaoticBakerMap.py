import math

class ChaoticBakerMap:

    def __init__(self, no):
        self.no = no
        self.factors = [2**e for e in range(1, int(math.log(self.no, 2)))]

    def __str__(self):
        return '(' + str(self.no) + ',' + str(self.factors) + ')'