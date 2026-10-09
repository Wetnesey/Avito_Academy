queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

print(len(queries))

cnt: dict[str, int] = {}
for q in queries:
    cnt[q] = cnt.get(q, 0) + 1
print(cnt)

top = max(cnt, key=lambda q: cnt[q])
print(top)
print(cnt[top] / len(queries))

once = []
for q in cnt:
    if cnt[q] == 1:
        once.append(q)
print(once)
