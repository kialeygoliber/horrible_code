class MoneyCalculator:

    #definition of a tip_calc function that takes a total as an argument
    def tip_calc(self, t, g):
        #returns the result of multiplying them together
        #accepts t as total and g as the percentage of the tip to be added
        return t * g

    #calculates the discount
    def discount_calculator(self, t, g):
        #returns the multiple of t and g
        return t * g

    #calculates the tip total and prints it

    def myfunc(p, pt):
        #add the tip and the total and print it to the console
        total = p
        percentage_total = pt
        final_total = total + percentage_total
        print(final_total)





def main():
    print("money calculator")

    moneycalc = MoneyCalculator()


    total = moneycalc.tip_calc(10, 100)

    myfunc(total,100 )