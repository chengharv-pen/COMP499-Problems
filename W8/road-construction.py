class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.components = n
        self.max_size = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.size[b] = 0
        self.components -= 1
        self.max_size = max(self.max_size, self.size[a])

def main():
    n, m = map(int, input().split())
    dsu = DSU(n)

    for _ in range(m):
        a, b = map(int, input().split())
        dsu.union(a, b)
        print(dsu.components, dsu.max_size)

if __name__ == "__main__":
    main()