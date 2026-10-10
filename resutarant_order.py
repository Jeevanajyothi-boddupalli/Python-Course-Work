def total_revenue(orders, n):
    if n==0:
        return 0
    return orders[n - 1] + total_revenue(orders, n - 1)
n=int(input("Enter number of orders: "))
orders=list(map(int, input("Enter order amounts: ").split()))
total=total_revenue(orders, n)
highest=max(orders)
above_500=sum(1 for order in orders if order > 500)
print("Total Revenue:", total)
print("Highest Order:", highest)
print("Orders above 500:", above_500)

