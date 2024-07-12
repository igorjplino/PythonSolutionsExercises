def make_change(charged, given):
    monetary = {
        "100 reais": 10000,
        "50 reais": 5000,
        "20 reais": 2000,
        "10 reais": 1000,
        "5 reais": 500,
        "2 reais": 200,
        "1 real": 100,
        "0,50 centavos": 50,
        "0,25 centavos": 25,
        "0,10 centavos": 10,
        "0,05 centavos": 5,
        "0,01 centavos": 1,
    }

    change = int((given - charged) * 100)

    if change == 0:
        print("No change necessary")
        return
    elif change < 0:
        print(f"Amount given is missing {abs(change)}")
        return
    
    print(f"Change for :{change / 100}")
    result = {}
    
    for key, value in monetary.items():
        if change >= value:
            count = change // value
            result[key] = count
            change = change - (value * count)

    for key, value in result.items():
        print(f"{key}: {value}")

make_change(100, 353.13)