def gen1(x):
    yield x + 10
    return x + 20


def gen2(x):
    return (yield (x + 10))

def gen3():
    yield 1
    yield 2

def trace(x):
    print(f'trace: {x}')
    return x

def coroutine():
    for i in range(1, 4):
        # print("From generator {}".format((yield (trace(i))))) # same as below
        sent = yield trace(i)
        print("From generator {}".format(sent))



if __name__ == '__main__':
    # print('--g1_1--')
    # g1_1 = gen1(1)
    # print(next(g1_1))  # prints 11
    # try:
    #     nxt = next(g1_1)
    # except StopIteration as e:
    #     print(e.value)  # prints 21
    #
    # print('--g1_2--')
    # g1_2 = gen1(1)
    # print(next(g1_2))  # prints 11
    # try:
    #     g1_2.send(2)
    #     nxt = next(g1_2)
    # except StopIteration as e:
    #     print(e.value)  # prints 21
    #
    # print('--g2_1--')
    # g2_1 = gen2(1)
    # print(next(g2_1))
    # value = g2_1.send(3)  # print(next(g2_1))


    c = coroutine()
    vNone = c.send(None)
    print(f'vNone = {vNone}')
    try:
        while True:
            print("From user {}".format(c.send(1)))
    except StopIteration: pass
    # From generator 1
    # From user 2
    # From generator 1
    # From user 3
    # From generator 1

    print('************')
    c2 = coroutine()
    print(next(c2))
    print(next(c2))
    # trace: 1
    # 1
    # From generator None
    # trace: 2
    # 2
