class MoneyCalculator:
    accepted_currency = {
        "dollar": 1.00,
        "quarter": 0.25,
        "dime": 0.10,
        "nickel": 0.05,
        "penny": 0.01
    }

    def __init__(self):
        pass

    # Example of DRY (don't repeat yourself):
    # We only have one method for calculating percentages, whereas
    # the horrible code has three (tip, tax, discount)
    @staticmethod
    def calculate_percentage(total, percentage):
        # Example of standard documentation:
        """
        Calculates any amount that is a percentage of the total (e.g. tips).
        :param total: float:
        :param percentage: float:
        :return float:
        """
        if percentage < 0:
            print("Percentage must be greater than 0!")
            return None
        return total * percentage

    @staticmethod
    def print_receipt(subtotal, tip, tax):
        """
        Print the customer's receipt.
        :param subtotal:
        :param tip:
        :param tax:
        :return None:
        """
        print(f"Subtotal: {subtotal}")
        print(f"Tip: {tip}")
        print(f"Tax: {tax}")
        total = subtotal + tip + tax
        print(f"Total: {total}")

    def sum_coins(self, coins):
        """
        Calculate total of coins provided by customer.
        :param coins: List[str]:
        :return float:
        """
        # Example of avoiding smelly comments:
        # Instead of providing a redundant comment here,
        # I used clear a variable name "coin"
        total = 0.0

        for coin in coins:
            # Example of single responsibility:
            # Another method handles checking a coin's validity
            if self.check_coin(coin):
                total += self.accepted_currency[coin]
            else:
                print(f"Invalid coin {coin} detected!")

        return total

    def check_coin(self, coin):
        """
        Checks if a coin is acceptable.
        :param coin: str:
        :return bool:
        """
        if coin in self.accepted_currency.keys():
            return True
        return False


def main():
    calculator = MoneyCalculator()

    paid = calculator.sum_coins(["penny", "nickel", "dollar", "dollar"])
    tip = calculator.calculate_percentage(10.50, 0.2)
    tax = calculator.calculate_percentage(10.50, 0.07)
    calculator.print_receipt(10.50, tip, tax)


if __name__ == "__main__":
    main()



