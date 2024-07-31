import math
from ArithmeticProgression import ArithmeticProgression
from Exercises.Creativy.c2_32 import SqrtProgression
from Exercises.Creativy.c2_31 import AbsDiffProgression
from Exercises.Creativy.c2_30 import PredatoryCreditCard_c2_30
from Exercises.Creativy.c2_27 import Range_Contains
from Exercises.Reinforcement.r2_23 import Sequence_lt
from Exercises.Reinforcement.r2_22 import Sequence_eq
from CreditCard import CreditCard
from Exercises.Reinforcement.r2_11 import Vector_radd
from Exercises.Reinforcement.r2_12 import Vector_mul
from Exercises.Reinforcement.r2_13 import Vector_rmul
from Exercises.Reinforcement.r2_15 import Vector_SenqInit
from Exercises.Reinforcement.r2_18 import FibonacciProgression_FindPosition
from Exercises.Reinforcement.r2_6 import CreditCardWithPositiveAmount
from Exercises.Reinforcement.r2_5 import CreditCardValidateNumber
from Exercises.Reinforcement.r2_7 import CreditCardWithBalance
from Exercises.Reinforcement.r2_9 import Vector_sub
from Exercises.Reinforcement.r2_10 import Vector_neg

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

def r2_15():
    list_vector = Vector_SenqInit([4, 7, 5])
    print(list_vector)

    empty_vector = Vector_SenqInit(3)
    print(empty_vector)

    # Output
    # <4, 7, 5>
    # <0, 0, 0>

def r2_18():
    f = FibonacciProgression_FindPosition()

    f.find_value_position(8)

def r2_19():
    progression = ArithmeticProgression(128)
    count = 0
    
    number = math.pow(2, 20) # Careful, 63 take too long to run 
    print(f"Goal: {number}")
    for v in progression:
        count += 1
        print(f"Current value: {v} | Count: {count}")
        if v >= number:
            break

    print(f"Final result: {count}")

def r2_23():
    seq1 = Sequence_lt([1, 2, 3])
    seq2 = Sequence_lt([1, 2, 3])
    print(seq1 < seq2)

    seq1 = Sequence_lt([1, 2, 3])
    seq2 = Sequence_lt([1, 2, 3, 4])
    print(seq1 < seq2)

    seq1 = Sequence_lt(['apple', 'banana', 'cherry'])
    seq2 = Sequence_lt(['apple', 'banana', 'date'])
    print(seq1 < seq2)   

def c2_27():
    rang = Range_Contains(10)
    print(3 in rang, 10 in rang, 23 in rang, -4 in rang)

    # Output
    # True False False False

    rang = Range_Contains(5, 10)
    print(3 in rang, 10 in rang, 23 in rang, -4 in rang)

    # Output
    # False True True False

    rang = Range_Contains(5, 50, 2)
    print(3 in rang, 10 in rang, 23 in rang, -4 in rang)

    # Output
    # False False True False

    rang = Range_Contains(5, -50, -2)
    print(3 in rang, 10 in rang, 23 in rang, -23 in rang)

    # Output
    # True False False True

def c2_30():
    wallet = []
    wallet.append(PredatoryCreditCard_c2_30('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500, 0.015))
    wallet.append(PredatoryCreditCard_c2_30('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500, 0.011))
    wallet.append(PredatoryCreditCard_c2_30('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000, 0.019))

    for val in range(1, 17):
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

    # Output
    # Customer = John Bowman
    # Bank = California Savings
    # Account = 5391 0375 9387 5309
    # Limit = 2500
    # Balance = 136
    # New balance = 36

    # Customer = John Bowman
    # Bank = California Federal
    # Account = 3485 0399 3395 1954
    # Limit = 3500
    # Balance = 272
    # New balance = 172
    # New balance = 72

    # Customer = John Bowman
    # Bank = California Finance
    # Account = 5391 0375 9387 5309
    # Limit = 5000
    # Balance = 408
    # New balance = 308
    # New balance = 208
    # New balance = 108
    # New balance = 8

def c2_31():
    prog = AbsDiffProgression()
    prog.print_progression(10)

def c2_32():
    prog = SqrtProgression()
    prog.print_progression(10)

c2_32() 