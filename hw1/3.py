orders: list[dict] = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

ret_sum = 0
ret_buyers = set()
n = 0
s = 0
for o in orders:
    if o["status"] == "returned":
        ret_sum += o["amount"]
        ret_buyers.add(o["buyer"])
    else:
        n += 1
        s += o["amount"]

print(ret_sum)
print(ret_buyers)
print(n)
print(s / n)
