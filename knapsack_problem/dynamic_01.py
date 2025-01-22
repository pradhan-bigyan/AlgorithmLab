def dynamic_01(P, Wt, n, cap):

    K = [[0 for _ in range(cap + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(cap + 1):
            if i == 0 or j == 0:
                K[i][j] = 0

            elif Wt[i] <= j:
                K[i][j] = max(P[i] + K[i - 1][j - Wt[i]], K[i - 1][j])

            else:
                K[i][j] = K[i - 1][j]

    return K[n][cap]