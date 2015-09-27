__author__ = 'KevinMortonMacPro'

def eval(x, poly):
    """
    :param x: Argument at which to evaluate
    :param poly: The polynomial coefficients, lowest order to highest
    :return: The result of evaluating the polynomial at x
    """
    n, tmp = 0, 0

    for i in poly:
        tmp += i * pow(x, n)
        n += 1

    return tmp

def bisection(a, b, poly, tol):
    if eval(a, poly) > 0:
        raise Exception('Poly a must be < 0: ', a,eval(a, poly))

    if eval(b, poly) < 0:
        raise Exception('Poly b must be > 0:', b,eval(b, poly))
    
    while (abs(b-a)> tol):
        c = (a+b)/2
        theValue = eval(c, poly)
        
        if theValue <= 0:
            a = c
        else:
            b = c
            
    return (a+b)/2

if __name__ == "__main__":
 
    toler = 1e-14
    poly1 = [-945, 1689, -950, 230, -25, 1]
    # roots are 1, 3, 5, 7, 9
    x1 = bisection(0, 2, poly1, 1e-15)
    print(x1, eval(x1,poly1))
    x2 = bisection(4,2,poly1,toler)
    print(x2, eval(x2,poly1))
    x3 = bisection(4,6,poly1, toler)
    print(x3, eval(x3,poly1))
    x4 = bisection(8,6,poly1, toler)
    print(x4, eval(x4,poly1))
    x5 = bisection(8,100,poly1, toler)
    print(x5, eval(x5,poly1))

    # compare the roots to the expected values
    print('-'*50)
    print(x1-1, x2-3, x3-5, x4-7, x5-9)
    