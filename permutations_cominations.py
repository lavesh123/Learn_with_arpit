from sys import argv
script, n, r = argv


def fac(n):
    if n == 0:
        return 1
    else:
        fact = n*fac(n-1)
    return fact


def permut(n, r, opt):
    if opt == 1:
        return (fac(n)/fac(n-r))
    else:
        return (fac(n)/(fac(n-r)*fac(r)))


opt = input("Press 1 for Permutations.\nPress 2 for no. of Combinations.\n")
if opt == 1:
    print(
        f"The value of {n} permutations taking {r} at a time: {permut(int(n),int(r),int(opt))}")
else:
    print(
        f"The value of {n} combinations taking {r} at a time: {permut(int(n),int(r),int(opt))}")
