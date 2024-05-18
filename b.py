from math import factorial
def lies_inside(a, b):
    # checks wether b is inside a
    x0, y0, r0 = a
    x1, y1, r1 = b
    return sqrt((x0 - x1) ** 2 - (y0 - y1) ** 2) + r1 < r0

def choose(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)
def dfs(a, circles, k, depth=0):
    depth += 1

    res = 0
    if depth >= k:
        res += choose(k - 1, depth - 1)

    for child in circles[a]:
        res += dfs(child, circles, depth)

    return res
    

def main():
    n, k = map(int, input().split())
    circles = {}
    rev_circles = {}
    for i in range(n):
        x, y, r = map(int, input().split())
        circles[(x, y, r)] = []

    for a in circles:
        for b in circles:
            if lies_inside(a, b):
                circles[a].append(b)
                rev_circles[b].append(a)

    res = 0
    for c, backwards_edges in rev_circles:
        if not backwards_edges:
            res += dfs(c, circles, k)
    print(res)


if __name__ == "__main__":
    main()