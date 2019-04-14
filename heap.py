import heapq
class A:
    def __init__(self,f,s):
        self.s = s
        self.f = f

    def __eq__(self, other):
        return self.f == other.f

    def __lt__(self, other):
        return self.f < other.f

    def __str__(self):
       return f'A(f={self.f}, s={self.s})'

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    # ls = []
    # heapq.heappush(ls, 7)
    # heapq.heappush(ls, 10)
    # heapq.heappush(ls, 9)
    # x = heapq.heappop(ls)
    # print(x) # 7
    # x = heapq.heappop(ls)
    # print(x) # 9
    # heapq.heappush(ls, 1)
    # heapq.heappush(ls, 2)
    # x = heapq.heappop(ls)
    # print(x) # 1

    ls2 = []
    heapq.heappush(ls2, A(3,"C"))
    heapq.heappush(ls2, A(1,"A"))
    heapq.heappush(ls2, A(2,"B"))
    a = heapq.heappop(ls2)
    print(a)
    print(ls2)
    heapq.heappush(ls2, A(1,"A"))
    heapq.heappush(ls2, A(1,"A"))
    print(ls2)
    a = heapq.heappop(ls2)
    print(a)
    a = heapq.heappop(ls2)
    print(a)
    # A(f=1, s=A)
    # [A(f=2, s=B), A(f=3, s=C)]
    # [A(f=1, s=A), A(f=1, s=A), A(f=2, s=B), A(f=3, s=C)]
    # A(f=1, s=A)
    # A(f=1, s=A)

