def strings(n):
    return [bin(x)[2:].rjust(n, '0') for x in range(2**n)]

def brute_force_01(P, wt, W):
    assert len(P) == len(wt)

    n= len(P)
    bit_strings = strings(n)

    max_profit = 0

    for s in bit_strings:
        weight = sum([int(s[i]) * wt[i] for i in range(n)])

        if weight <= W:
            profit = sum([int(s[i]) * P[i] for i in range(n)])
            if max_profit < profit:
                max_profit = profit

    return max_profit