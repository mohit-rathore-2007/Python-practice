daily_running=int(input("enter daily running in KM"))
life_time=int(input("enter life time of vehicle in years"))
petrol_average=float(input("enter petrol averag<e"))
CNG_average=float(input("enter CNG average"))
electric_average=float(input("enter electric average"))
cost_price_petrol=int(input("enter price of petrol vehicle"))
cost_price_CNG=int(input("enter price of cng vehicle"))
cost_price_electric=int(input("enter price of electric vehicle"))
petrol_cost=int(input("enter price of petrol"))
CNG_cost=int(input("enter price of CNG"))
electric_cost=int(input("enter price of electric"))
total_running=daily_running*life_time*365
fuel_requirment_petrol=total_running/petrol_average
fuel_requirment_CNG=total_running/CNG_average
fuel_requirment_electric=total_running/electric_average
total_cost_petrol=cost_price_petrol+(fuel_requirment_petrol*petrol_cost)
total_cost_CNG=cost_price_CNG+(fuel_requirment_CNG*CNG_cost)
total_cost_electric=cost_price_electric+(fuel_requirment_electric*electric_cost)
if total_cost_petrol<total_cost_electric and total_cost_petrol<total_cost_CNG:
	print("buy the petrol verient")
elif total_cost_electric<total_cost_petrol and total_cost_electric<total_cost_CNG:
	print("buy the electric verient")
else:
	print("buy the CNG verient")