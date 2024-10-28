def binom(n, m):
    memo = {}
    if n == m or m == 0:
        return 1
    if (n, m) in memo:
        return memo[(n, m)]
    res = binom(n-1, m-1) + binom(n-1, m)
    memo[(n, m)] = res
    return res

def editDist(s1, s2):
    memo = {}
    def ed(s1, s2):
        if len(s1) == 0:
            return len(s2)
        if len(s2) == 0:
            return len(s1)
        if s2[0] == s1[0]:
            memo[(s1, s2)] =  editDist(s1[1:], s2[1:])
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        delete = editDist(s1[1:], s2)
        change = editDist(s1[1:], s2[1:])
        insert = editDist(s1, s2[1:])
        memo[(s1, s2)] = 1 + min(delete, change, insert)
        return memo[(s1, s2)]
    return ed(s1, s2)
