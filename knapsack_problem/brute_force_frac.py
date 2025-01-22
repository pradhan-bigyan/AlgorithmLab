def brute_force_frac(p, w, m):
    assert len(p) == len(w), "p and w differ"

    n = len(p)
    max_profit = 0
    total_weight = m
    for i in range(2**n):
        s = bin(i)[2:].rjust(n, '0')
        profit = 0
        weight = 0
        for j in range(n):
            if s[j] == '1':
                profit += p[j]
                weight += w[j]
            elif s[j] == '0':
                pass
        
        if weight > total_weight:
            continue
        fraction = (total_weight - weight) / sum(w[j] for j in range(n) if s[j] == '0')
        profit += fraction * sum(p[j] for j in range(n) if s[j] == '0')
        weight += fraction * sum(w[j] for j in range(n) if s[j] == '0')
        
        
        if profit > max_profit:
            max_profit = profit

    return int(max_profit)