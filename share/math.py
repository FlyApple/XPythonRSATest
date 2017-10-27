# encoding: utf-8


# math gcd function:
def gcd(a, b):
    if b == 0 : return a;
    return gcd(b, a % b);