print("THESE ARE WHAT WE HAVE:")
print("mobile\nwatch\nmonitor\nkeyboard\nmouse\ncalculator\nbulb\nfan")
products = {
	"mobile":15000,
	"watch":3000,
	"monitor":1700,
	"keyboard":500,
	"mouse":500,
	"bulb":350,
	"fan":1200 
}
total_cost = 0
budget = int(input("how many budget do you have ?? "))
cupon = input("do you have cupon card ?? (yes  /  no )>")
first_product = input("what you want to buy??")
def with_cupon(total_cost,budget):
	total_cost = total_cost - (15/100)
	print(f"after giving 15% discount in total amount , your total price is {total_cost}")
	change =  budget - total_cost
	print(f"your change is {change}")
def without_cupon(total_cost,budget):
	change = budget - total_cost
	print(f"total cost is {total_cost}")
	print(f"your change is {change}")
def having_cupon(cupon,total_cost,budget):
		if cupon == "yes":
			with_cupon(total_cost,budget)
		else:
			without_cupon(total_cost,budget)
def second_order(total_cost, asking_second_product,cupon,budget):
	if asking_second_product == 'yes':
		second_product = input("what more you want ??")
		if second_product in products:
			total_cost += products[second_product]
			having_cupon(cupon,total_cost,budget)
		else:
			print(f'{second_product} is not available')
			having_cupon(cupon,total_cost,budget)
	else:
		having_cupon(cupon,total_cost,budget)
if first_product in products:
	total_cost += products[first_product]
	asking_second_product = input("do you want anything more ??(yes / no)> ")
	second_order(total_cost,asking_second_product,cupon,budget)  
else:
	print("we don't have the product you want .")

