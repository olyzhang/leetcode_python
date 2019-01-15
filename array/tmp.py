from scipy.special import comb
from decimal import Decimal


def p(n, x):
    pnx = Decimal.from_float(comb(n, x) * pow(0.1, x) * pow(0.9, n - x))
    return pnx


if __name__ == "__main__":
    total = 120
    using = 20
    result = Decimal(1)
    for i in range(using + 1):
        print(i, ": ", p(total, i))
        result -= p(total, i)
    print(result)
    print(1 - result)
