print("aini jiajia")
#浅拷贝
def test():
    import copy

    a = [10,20,[5,6]]
    b = copy.copy(a)

    print("a:",a)
    print("b:",b)

    b.append(30)
    b[2].append(7)
    print("拷贝.......")
    print("a:",a)
    print("b:",b)


def testjiajia():
    import copy

    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)

    print("a:", a)
    print("b:", b)

    b.append(30)
    b[2].append(7)
    print("拷贝.......")
    print("a:", a)
    print("b:", b)

testjiajia()
test()