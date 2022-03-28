import calci


def test_add():
    a = 10
    b=5
    r = calci.add(a,b)
    assert  a+b == r



def test_mul():
    a = 10
    b=5
    r = calci.mul(a,b)
    assert  a*b == r



def test_div():
    a = 10
    b=5
    r = calci.div(a,b)
    assert  a/b == r



def test_sub():
    a = 10
    b=5
    r = calci.sub(a,b)
    assert  a-b == r