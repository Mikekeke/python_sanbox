def gen1(x):
    x = yield  # equivalent to "x = yield None" - will return None
    yield x + 20


if __name__ == '__main__':

    print('--g1_2--')
    g1_2 = gen1(1)
    print(next(g1_2))  # None
    v1 = g1_2.send(2)
    print(f'v: {v1}')  # 22
    v2 = g1_2.send(3)  # StopIteration
    print(f'v: {v2}')
