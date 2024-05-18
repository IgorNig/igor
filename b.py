from math import factorial
def lies_inside(a, b):
    # checks wether b is inside a
    x0, y0, r0 = a
    x1, y1, r1 = b
    return ((x0 - x1) ** 2 - (y0 - y1) ** 2)**0.5 + r1 < r0

def choose(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)

def dfs(a, circles, rev_circles, k, depth=0, ancestors=set()):
    depth += 1

    ancestors.add(a)
    res = 0
    if depth >= k:
        res += choose(k - 1, depth - 1)


    for child in circles[a]:
        if rev_circles == ancestors:
            res += dfs(child, circles, depth)

    ancestors.remove(a)

    return res
    

def main():
    n, k = map(int, input().split())
    circles = {}
    rev_circles = {}
    for i in range(n):
        x, y, r = map(int, input().split())
        circles[(x, y, r)] = set()

    for a in circles:
        for b in circles:
            if lies_inside(a, b):
                circles[a].append(b)
                rev_circles[b].append(a)

    res = 0
    for c, backwards_edges in rev_circles.items():
        if not backwards_edges:
            res += dfs(c, circles, k, 0, set())
    print(res)


if __name__ == "__main__":
    main()

# не работает вот пример ввода
# 10 5
# 0 0 100
# 0 0 90
# 0 0 80
# 0 0 50
# 10 0 4
# 0 0 5
# 0 0 4
# 0 0 3
# 0 0 2
# 0 0 1
