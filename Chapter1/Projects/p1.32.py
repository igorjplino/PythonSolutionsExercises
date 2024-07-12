def calculate(d1, d2, op):
    r = None

    if op == "+":
        r = d1 + d2
    elif op == "-":
        r = d1 - d2
    elif op == "*":
        r = d1 * d2
    elif op == "/":
        r = d1 // d2
    else:
        raise ValueError(f"Operator '{op}' not found")

    print(f"{d1} {op} {d2} = {r}")

calculate(15, 20, "+")
calculate(15, 20, "-")
calculate(15, 20, "*")
calculate(15, 20, "/")

# Output
# 15 + 20 = 35
# 15 - 20 = -5
# 15 * 20 = 300
# 15 / 20 = 0