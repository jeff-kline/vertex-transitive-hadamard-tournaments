# Census of the orders v = 3 (mod 4), 3 <= v < 10^5.
# Each v is assigned to the first rule that applies; "open" means no rule applies.
from collections import Counter
def fac(n):
    f, q = {}, 2
    while n > 1:
        if q * q > n: q = n
        while n % q == 0: f[q] = f.get(q, 0) + 1; n //= q
        q += 1
    return f
def gl(n, r):                              # the order of GL(n, r)
    g = 1
    for i in range(n): g *= r ** n - r ** i
    return g
def witness(v, p, r, k):                   # is there a gate witness (j, n, N)?
    for j in range(1, k + 1):
        w = v // r ** (2 * j)
        for N in range(p, w + 1, p):       # p | N
            if w % N or N <= r ** (2 * j): continue
            if j == 1 and N != r * r + r + 1: continue
            for n in range(2 * j + 1, 4 * j):
                if gl(n, r) % N == 0 and N * (r ** (n - 2 * j) - 1) >= r ** n - 1:
                    return True
    return False
def test(v):
    f = fac(v)
    if len(f) == 1: return "1 prime power"
    odd = [q for q in f if f[q] % 2]
    if len(odd) != 1: return "2 Ito"
    p = odd[0]; e = f[p]; a = (e - 1) // 2
    rs = sorted(q for q in f if q != p); r = rs[0]
    if max(f.values()) <= 3: return "3 Theorem B"
    if all(f[q] == 2 for q in rs):         # Theorem C: squarefree cofactor
        if a <= 3 or (a == 4 and p != 3) or p > 4 * a - 5: return "4 Theorem C"
    m = p ** e
    for q in rs:                           # prefix bound
        if q * q + q + 1 > m: return "5 prefix bound"
        m *= q ** f[q]
    if e <= 3 and all(f[q] == 2 or not witness(v, p, q, f[q] // 2) for q in rs):
        return "6 gate"
    if len(rs) == 1 and e == 1 and f[r] == 4 and p < r ** 4: return "7 p r^4"
    return "open"
R = {v: test(v) for v in range(3, 10 ** 5, 4)}
print("open:", [v for v in R if R[v] == "open"])
print("orders:", len(R))
for rule, c in sorted(Counter(R.values()).items()):
    print("  ", rule, c, [v for v in R if R[v] == rule] if c < 10 else "")
