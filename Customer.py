import Payment
import Products
import SnackMachine
from random import randint


class Customer:
    def __inti__(self):
        pass


if __name__ == "__main__":
    vending_slots = [[None for j in range(5)] for i in range(5)]

    for i in range(5):
        for j in range(5):
            vending_slots[i][j] = Products.Product(str("{}{}".format(i, j)), str(
                "item at row {} column {}".format(i, j)), randint(0, 10) - (randint(0, 2) / 2), randint(0, 200))

    for i in range(5):
        for j in range(5):
            if vending_slots[i][j].price <= 0:
                vending_slots[i][j].price = 0.5

    vending_coins = {
        "0.1": 200,
        "0.2": 70,
        "0.5": 120,
        "1": 50,
        "20": 100,
        "50": 77
    }
    vending = SnackMachine.SnackMachine(125, vending_slots, vending_coins)

    print("Hello there, Start Ordering, Row first")
    customer_in = input()

    if len(customer_in) > 2 or len(customer_in) < 2:
        print("Invalid Input")
    elif int(customer_in[0]) < 0 or int(customer_in[0]) > 4:
        print("Row is out of boundries")
    elif int(customer_in[1]) < 0 or int(customer_in[1]) > 4:
        print("Column is out of boundries")

    else:
        print("Customer Ordered {}".format(
            vending.slots[int(customer_in[0])][int(customer_in[1])]))
        if not(vending.checkAvailableSnack(vending.slots[int(customer_in[0])][int(customer_in[1])])):
            print("Sorry Not Available")
        else:
            print("Available and Costs ${}".format(
                vending.slots[int(customer_in[0])][int(customer_in[1])].price))
            print("If you want to pay by cash press 1, by card press 2")
            pay_in = int(input())
            if pay_in < 1 or pay_in > 2:
                print("Wrong Input")
            else:
                pay = Payment.Payment(pay_in, vending.slots[int(
                    customer_in[0])][int(customer_in[1])].price)

                if pay.method == 1:
                    if(not(pay.Validate_Cash(
                            vending.slots[int(customer_in[0])][int(customer_in[1])].price, vending))):
                        coins_paid = pay.dispensingCoins(
                            pay.total, vending.coins)

                        for i in coins_paid:
                            print("Dispensing ${}".format(i))
                            if (i >= 1):
                                i = int(i)
                            vending.coins[str(i)] -= 1

                        quit()

                elif pay.method == 2:
                    if (not(pay.Validate_Card())):
                        quit()

                vending.slots[int(customer_in[0])][int(
                    customer_in[1])].purchase_product()
                print("Dispensing {}" .format(
                    vending.slots[int(customer_in[0])][int(customer_in[1])].name))
                if pay.remaining > 0:
                    print("Remaining ${} to dispense!" .format(pay.remaining))

                coins_paid = pay.dispensingCoins(pay.remaining, vending.coins)

                for i in coins_paid:
                    print("Dispensing ${}".format(i))
                    if (i >= 1):
                        i = int(i)
                    vending.coins[str(i)] -= 1
