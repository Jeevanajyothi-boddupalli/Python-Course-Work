import matplotlib.pyplot as mplt 
#lineplot
months = ["Jan","Feb","Mar","April"]
sales = [25,32,28,47]
mplt.plot(months,sales,color="green",marker="o")
mplt.title("Monthly sales")
mplt.xlabel("Months")
mplt.ylabel("Sales")
mplt.grid()
mplt.show()