def d2i_nVm():
    rate=int(input("Enter the conversion rate"))
    amt=int(input("Entrer the amount in dollars"))
    def d2i_nV(rate,amt):
        print("The price in USD is ",rate*amt)
    d2i_nV(rate,amt)
def d2i_V():
    rate=int(input("Enter the conversion rate"))
    amt=int(input("Entrer the amount in dollars"))
    print("The price in USD is ",rate*amt)
d2i_nVm()
d2i_V()