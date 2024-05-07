class MaxHeap:
    def __init__(self):
        self.xs = [None]

    def __len__(self):
        return len(self.xs) - 1

    def par(self, i):
        return i // 2

    def leftchild(self, i):
        return 2 * i

    def rightchild(self, i):
        return 2 * i + 1

    def swim(self, i):
        p = self.par(i)
        while p > 0 and self.xs[i] > self.xs[p]:
            self.xs[p], self.xs[i] = self.xs[i], self.xs[p]
            i, p = p, self.par(p)

    def sink(self, i):
        left, right = self.leftchild(i), self.rightchild(i)
        while left < len(self.xs):
            if right >= len(self.xs):
                if self.xs[left] > self.xs[i]:
                    self.xs[left], self.xs[i] = self.xs[i], self.xs[left]
                    i = left
                else:
                    break
            else:
                maxval = max(self.xs[left], self.xs[right], self.xs[i])
                if maxval == self.xs[left]:
                    self.xs[left], self.xs[i] = self.xs[i], self.xs[left]
                    i = left
                elif maxval == self.xs[right]:
                    self.xs[right], self.xs[i] = self.xs[i], self.xs[right]
                    i = right
                else:
                    break
            left, right = self.leftchild(i), self.rightchild(i)

    def peek(self):
        if len(self) == 0:
            return None
        return self.xs[1]

    def push(self, x):
        self.xs.append(x)
        self.swim(len(self))

    def pop(self):
        if len(self) == 0:
            return None
        self.xs[1], self.xs[len(self)] = self.xs[len(self)], self.xs[1]
        ret = self.xs.pop()
        self.sink(1)
        return ret
