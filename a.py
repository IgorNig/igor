
def final_distance(changes, time):
    a = 0

    change_list = sorted(changes)

    while change_list[-1] > time:
        changes_list.pop()

    if change_list[-1] != time:
        change_list.append(time)

    time = min(changes)
    v = 0
    a = 0
    dist = 0
    for change in change_list:
        v += a * (change - t)
        dist += a * (change -t) ** 2 / 2

        a += changes[change]

    return dist



def main():
    n = int(input())
    changes = {}

    thingies = []
    for _ in range(n):
        l, r, a = int(input())
        thingies.append((l, r, a))
        changes[l] = changes.get(l, 0) + a
        changes[r] = changes.get(r, 0) - a

    q = int(input())

    for i in range(q):
        to_invert, time = map(int, input().split())
        l, r, a = thingies[to_invert]

        changes[l] -= 2 * a
        changes[r] += 2 * a

        print(final_distance(changes, time))
        changes[l] += 2 * a
        changes[r] += 2 * a

    changes_list = sorted(changes)


if __name__ == "__main__":
    main()
