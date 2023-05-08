class RecursivityDegree2:
    def __init__(self, i1=0, i2=1):
        self.memo = {0: i1, 1: i2}

    def __call__(self, n):
        if n not in self.memo:
            self.memo[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.memo[n]


if __name__ == '__main__':
    fib = RecursivityDegree2()
    print(fib(10))
    print(fib(11))