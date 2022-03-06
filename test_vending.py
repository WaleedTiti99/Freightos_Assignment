import imp
import unittest
import Products
import SnackMachine
import Payment

from random import randint


class TestVending (unittest.TestCase):

    def test_available(self):
        vending_slots = [[None for j in range(5)] for i in range(5)]
        for i in range(5):
            for j in range(5):
                vending_slots[i][j] = Products.Product(str("{}{}".format(i, j)), str(
                    "item at row {} column {}".format(i, j)), randint(0, 10) - (randint(0, 4) / 4), randint(0, 200))

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
        vend = SnackMachine.SnackMachine(125, vending_slots, vending_coins)

        self.assertTrue(vend.checkAvailableSnack(vend.slots[1][3]))

    def test_not_available(self):
        vending_slots = [[None for j in range(5)] for i in range(5)]
        for i in range(5):
            for j in range(5):
                vending_slots[i][j] = Products.Product(str("{}{}".format(i, j)), str(
                    "item at row {} column {}".format(i, j)), randint(0, 10) - (randint(0, 4) / 4), randint(0, 200))

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
        vend = SnackMachine.SnackMachine(125, vending_slots, vending_coins)
        vend.slots[1][4].stock = 0
        self.assertFalse(vend.checkAvailableSnack(vend.slots[1][4]))

    def test_validate_card(self):
        pay = Payment.Payment(2, 5.5)
        self.assertTrue(pay.Validate_Card)

    def test_validate_cash(self):
        vending_slots = [[None for j in range(5)] for i in range(5)]
        for i in range(5):
            for j in range(5):
                vending_slots[i][j] = Products.Product(str("{}{}".format(i, j)), str(
                    "item at row {} column {}".format(i, j)), randint(0, 10) - (randint(0, 4) / 4), randint(0, 200))

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
        vend = SnackMachine.SnackMachine(125, vending_slots, vending_coins)

        pay = Payment.Payment(1, 5.5)
        self.assertTrue(pay.Validate_Cash(vend.slots[1][3].price, vend))

    def test_validate_cash_reject(self):
        vending_slots = [[None for j in range(5)] for i in range(5)]
        for i in range(5):
            for j in range(5):
                vending_slots[i][j] = Products.Product(str("{}{}".format(i, j)), str(
                    "item at row {} column {}".format(i, j)), randint(0, 10) - (randint(0, 4) / 4), randint(0, 200))

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
        vend = SnackMachine.SnackMachine(125, vending_slots, vending_coins)

        pay = Payment.Payment(1, 5.5)
        self.assertFalse(pay.Validate_Cash(vend.slots[1][3].price, vend))

    def test_dispensing(self):
        vending_slots = [[None for j in range(5)] for i in range(5)]
        for i in range(5):
            for j in range(5):
                vending_slots[i][j] = Products.Product(str("{}{}".format(i, j)), str(
                    "item at row {} column {}".format(i, j)), randint(0, 10) - (randint(0, 4) / 4), randint(0, 200))

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
        vend = SnackMachine.SnackMachine(125, vending_slots, vending_coins)

        pay = Payment.Payment(1, 5.5)
        pay.remaining = 23.5
        test_out = []
        test_out.append(20.0)
        test_out.append(1.0)
        test_out.append(1.0)
        test_out.append(1.0)
        test_out.append(0.5)
        self.assertEqual(pay.dispensingCoins(
            pay.remaining, vend.coins), test_out)

    def test_purchase(self):
        vending_slots = [[None for j in range(5)] for i in range(5)]
        for i in range(5):
            for j in range(5):
                vending_slots[i][j] = Products.Product(str("{}{}".format(i, j)), str(
                    "item at row {} column {}".format(i, j)), randint(0, 10) - (randint(0, 4) / 4), randint(0, 200))

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
        vend = SnackMachine.SnackMachine(125, vending_slots, vending_coins)
        previous_am = vend.slots[1][3].stock
        vend.slots[1][3].purchase_product()
        self.assertEqual(vend.slots[1][3].stock, previous_am - 1)

    def test_purchase_fail(self):
        vending_slots = [[None for j in range(5)] for i in range(5)]
        for i in range(5):
            for j in range(5):
                vending_slots[i][j] = Products.Product(str("{}{}".format(i, j)), str(
                    "item at row {} column {}".format(i, j)), randint(0, 10) - (randint(0, 4) / 4), randint(0, 200))

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
        vend = SnackMachine.SnackMachine(125, vending_slots, vending_coins)
        vend.slots[1][2].stock = 0
        self.assertFalse(vend.slots[1][2].purchase_product())


if __name__ == "__main__":
    unittest.main()
