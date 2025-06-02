"""

计算组合数C(m,n)

"""

m = int(input('m =  '))
n = int(input('n =  '))
fa = 1
for a in range(1, m + 1):
    fa *= a
fb = 1
for b in range(1, n + 1):
    fb *= b
fc = 1
for c in range(1, m - n + 1):
    fc *= c
f = fa // (fb * fc)
print(fa)
print(fb)
print(fc)
print(f'C({m},{n}) = {f}')
