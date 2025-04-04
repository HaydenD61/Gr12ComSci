def f(base, expo):
    if expo == 0:
        return 1
    else:
        return base * f(base, expo - 1)

print(f(2, 9))