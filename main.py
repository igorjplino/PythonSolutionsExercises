from Chapter2.CreditCard import CreditCard
from Chapter2.Exercises.Reinforcement.r2_11 import Vector_radd
from Chapter2.Exercises.Reinforcement.r2_12 import Vector_mul
from Chapter2.Exercises.Reinforcement.r2_13 import Vector_rmul
from Chapter2.Exercises.Reinforcement.r2_6 import CreditCardWithPositiveAmount
from Chapter2.Exercises.Reinforcement.r2_5 import CreditCardValidateNumber
from Chapter2.Exercises.Reinforcement.r2_7 import CreditCardWithBalance
from Chapter2.Exercises.Reinforcement.r2_9 import Vector_sub
from Chapter2.Exercises.Reinforcement.r2_10 import Vector_neg

def r2_5():
    creditCard = CreditCardValidateNumber("Igor", "XPTO", "1234 5678 0987", 1000) # type: ignore

    creditCard.charge(200)
    print(f"Current balance: {creditCard.get_balance()}")

    creditCard.make_payment(100.00)
    print(f"Current balance: {creditCard.get_balance()}")

    creditCard.make_payment("50")
    print(f"Current balance: {creditCard.get_balance()}")

    creditCard.make_payment("xyz")
    print(f"Current balance: {creditCard.get_balance()}")

    # Output
    # Current balance: 200.0
    # Current balance: 100.0
    # Current balance: 50.0
    # ValueError: The amount must be a number
    
def r2_6():
    creditCard = CreditCardWithPositiveAmount("Igor", "XPTO", "1234 5678 0987", 1000)

    creditCard.charge(200)
    print(f"Current balance: {creditCard.get_balance()}")

    creditCard.make_payment(100.00)
    print(f"Current balance: {creditCard.get_balance()}")

    creditCard.make_payment("50")
    print(f"Current balance: {creditCard.get_balance()}")

    creditCard.make_payment(-20)
    print(f"Current balance: {creditCard.get_balance()}")

    # Output
    # Current balance: 200.0
    # Current balance: 100.0
    # Current balance: 50.0
    # ValueError: The amount must be a positive number

def r2_7():
    balance = 150
    creditCard = CreditCardWithBalance("Igor", "XPTO", "1234 5678 0987", 1000, balance)
    print(f"Current balance: {creditCard.get_balance()}")

    # Output
    # Current balance: 150

def r2_8():
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))

    for val in range(1, 5000):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print("Customer =", wallet[c].get_customer())
        print("Bank =", wallet[c].get_bank())
        print("Account =", wallet[c].get_account())
        print("Limit =", wallet[c].get_limit())
        print("Balance =", wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New balance =", wallet[c].get_balance())
        print()

def r2_9():
    len = 5
    u = Vector_sub(len)
    v = Vector_sub(len)
    result = u - v
    print(result)

    for i in range(len):
        u[i] = 2 + (i * 4)
        v[i] = 1 + (i * 2)

    result = u - v
    print(result)

    # Output
    # <0, 0, 0, 0, 0>
    # <1, 3, 5, 7, 9>

def r2_10():
    len = 5
    v = Vector_neg(len)

    for i in range(len):
        v[i] = 1 + i

    print(f"Original: {v}")
    print(f"Negative: {-v}")

    # Output
    # Original: <1, 2, 3, 4, 5>
    # Negative: <-1, -2, -3, -4, -5>

def r2_11():
    len = 5
    v = Vector_radd(len)

    for i in range(len):
        v[i] += i

    print(f"Original: {v}")

    result = [1, 2, 3, 4, 5] + v
    print(f"radd: {result}")

def r2_12():
    len = 5
    v = Vector_mul(len)

    for i in range(len):
        v[i] += i
    
    val = 4
    print(f"Original: {v}")
    print(f"Multiplied by {val}: {v*val}")

    # Output
    # Original: <0, 1, 2, 3, 4>
    # Multiplied by 4: <0, 4, 8, 12, 16>

def r2_13():
    len = 5
    v = Vector_rmul(len)

    for i in range(len):
        v[i] += i
    
    val = 4
    print(f"Original: {v}")
    print(f"Multiplied by {val}: {val*v}")

    # Output
    # Original: <0, 1, 2, 3, 4>
    # Multiplied by 4: <0, 4, 8, 12, 16>

r2_12()

