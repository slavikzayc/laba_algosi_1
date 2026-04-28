import sys
import random

sys.setrecursionlimit(10**7)

class Node:
    def __init__(self, key):
        self.key = key
        self.pr = random.randint(1, 10**9)
        self.l = None
        self.r = None


def split(t, x):
    if not t:
        return (None, None)
    if x < t.key:
        l, t.l = split(t.l, x)
        return (l, t)
    else:
        t.r, r = split(t.r, x)
        return (t, r)


def merge(a, b):
    if not a or not b:
        return a or b
    if a.pr > b.pr:
        a.r = merge(a.r, b)
        return a
    else:
        b.l = merge(a, b.l)
        return b


def insert(t, x):
    if exists(t, x):
        return t
    new = Node(x)
    l, r = split(t, x)
    return merge(merge(l, new), r)


def delete(t, x):
    if not t:
        return None
    if t.key == x:
        return merge(t.l, t.r)
    if x < t.key:
        t.l = delete(t.l, x)
    else:
        t.r = delete(t.r, x)
    return t


def exists(t, x):
    while t:
        if t.key == x:
            return True
        if x < t.key:
            t = t.l
        else:
            t = t.r
    return False


def next_val(t, x):
    res = None
    while t:
        if t.key > x:
            res = t.key
            t = t.l
        else:
            t = t.r
    return res


def prev_val(t, x):
    res = None
    while t:
        if t.key < x:
            res = t.key
            t = t.r
        else:
            t = t.l
    return res


# --- main ---

root = None
ans = []

for line in sys.stdin:
    if not line.strip():
        continue
    cmd, x = line.split()
    x = int(x)

    if cmd == "insert":
        root = insert(root, x)

    elif cmd == "delete":
        root = delete(root, x)

    elif cmd == "exists":
        ans.append("true" if exists(root, x) else "false")

    elif cmd == "next":
        r = next_val(root, x)
        ans.append(str(r) if r is not None else "none")

    elif cmd == "prev":
        r = prev_val(root, x)
        ans.append(str(r) if r is not None else "none")

print("\n".join(ans))