from BankAccount import Savings, Checking


def main():
    savings1 = Savings("Jordan", 1000, 100, 0.05)
    savings2 = Savings("Ryan", 500, 50, 0.03)

    savings1.apply_interest()
    savings2.apply_interest()

    checking1 = Checking("Jordan", 571, 50, 300)
    checking2 = Checking("Ryan", 992, 100, 200)

    checking1.withdraw(200)

    checking1.transfer(150, checking2)
    checking1.transfer(400, checking2)

    checking2.withdraw(50)
    checking2.transfer(100, checking1)


if __name__ == "__main__":
    main()
