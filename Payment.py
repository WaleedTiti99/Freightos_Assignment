class Payment:
    def __init__(self, method, amount):
        self.method = method
        self.amount = amount
        self.total = 0
        self.remaining = 0

    def Validate_Card(self):
        print("Card successfully validated and you can resume")
        return True

    def Validate_Cash(self, amount, machine):
        total = 0
        while (total < amount):
            cashing = input(
                "Insufficient Funds, your total is ${} \n".format(total))
            if cashing in machine.coins:
                machine.coins[cashing] += 1
                total = total + float(cashing)
                self.total = total
            else:
                print("Money Not Accepted")

            choice = input("Do you want to continue? Y/N \n")
            if (choice == "N"):
                print("Dispensing Coins. Have a Good Time")
                return False
        self.remaining = total - amount
        print("Done total {}".format(total))
        return True

    def dispensingCoins(self, amount, coins):
        output = []

        sorted_coins = sorted(
            coins.items(), key=lambda kv: kv[0], reverse=True)

        for i in sorted_coins:
            while amount >= float(i[0]):
                if(i[1] > 0):
                    amount -= float(i[0])
                    output.append(float(i[0]))

        return output
