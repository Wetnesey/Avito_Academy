reviews: list[dict] = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]

stars: dict[str, list[int]] = {}
for r in reviews:
    name = r["product"].lower()
    if name not in stars:
        stars[name] = []
    stars[name].append(r["stars"])

avg: dict[str, float] = {}
for name in stars:
    avg[name] = sum(stars[name]) / len(stars[name])
print(avg)

worst = None
for name in avg:
    if len(stars[name]) >= 2:
        if worst is None or avg[name] < avg[worst]:
            worst = name
print(worst)

bad = 0
for r in reviews:
    if r["stars"] <= 2:
        bad += 1
print(bad)
print(bad / len(reviews))
