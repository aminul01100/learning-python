
while True:
    principle = int(input("Enter principal (0 to stop): "))

    if principle == 0:
        break
    else:
        rate = int(input("Enter rate (%): "))
        time = int(input("Enter time (years): "))
        i = (principle*rate*time/100)
        Tm = principle+i
        print("Customer 1:")
        print("Principal: $",principle,"Rate: ",rate,"%, Time: ",time," years")
        print("Interest: $",i, "Total Amount: $",Tm)
        print("Total Interest Earned: $",i)
        print("Total Amount Processed: $",Tm)
