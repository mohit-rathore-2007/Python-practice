principal=int(input("enter the value of principal"))
rate_of_int=int(input("enter the value of rate_of_int"))
time_duration=int(input("enter the time_duration in years"))
simple_int=(principal*rate_of_int*time_duration)/100
print(simple_int) 
total_payable_amount=simple_int+principal
print(total_payable_amount)
monthly_installments=time_duration*12
emi=total_payable_amount/monthly_installments
print(emi)

