days: list[dict] = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

total = 0
for d in days:
    total += d["revenue"]
print(total)

best = days[0]
for d in days:
    if d["revenue"] > best["revenue"]:
        best = d
print(best["day"])

for d in days:
    print(d["day"], d["revenue"] / d["orders"])

for d in days:
    if d["returns"] > d["orders"] * 0.2:
        print(d["day"])
