#Homework 2

#First question:Personal information
print('My name is James Ngo.')
print('My address is 3363 net court street , Jacksonville , FLorida , 32277.')
print('My telephone number is: (202)848-5691.')
print('My college major is information system.')

#Second question:Sales prediction
Total_Sales = int(input('Enter the projected amount of total sales: '))
percent = 0.23
profit = Total_Sales * percent
print('The amount of profit that would be made is ',format( profit, '.2f'),'.' )


#Third question:Land Calculation
One_acre = 43650
square_feet =int(input('Enter the total square feet of your land:'))
number_of_acre = square_feet / One_acre
print('You have a total of ', number_of_acre , 'acre(s).')

#fourth question: Total purhcase
first_item = float(input('Enter the price of the first item:'))
second_item = float(input('Enter the price of the second item:'))
third_item = float(input('Enter the price of the third item:'))
fourth_item = float(input('Enter the price of the fourth item:'))
fifth_item= float(input('Enter the price of the fifth item:'))

subtotal = (first_item + second_item + third_item + fourth_item + fifth_item)
sales_tax = subtotal * 0.06
total = subtotal + sales_tax

print('The subtotal is' , subtotal , 'the sales tax is',format( sales_tax , '.2f'),\
      ', and the total is ', total, )


#fifth question: Distance traveled
#note to self that distance = speed times time

car_speed = 60
time1 = 5
time2 = 8
time3 = 12

distance1 = car_speed * time1
distance2 = car_speed * time2
distance3 = car_speed * time3

print('The distance the car will travel in 5 hours is' ,distance1 , 'miles.' )
print('The distance the car will travel in 8 hours is' ,distance2, 'miles.')
print('The distance the car will travel in 12 hours is', distance3, 'miles.')

#sixth question: Sales tax

SST = 0.04
CST = 0.02
purchase = float(input('Enter the amount of your purchase:'))

SSTpurchase = SST * purchase
CSTpurchase = CST * purchase
Total_sales_tax = SSTpurchase + CSTpurchase
Total_sale = purchase + SSTpurchase + CSTpurchase 

print('The total amount of the purchase is', purchase , '.')
print('The state sales tax is', format(SSTpurchase, '.2f') , '.')
print('The county sales tax is', format(CSTpurchase, '.2f'), '.')
print('The total sales tax is', format(Total_sales_tax, '.2f'), '.')
print('The total of the sale is', format(Total_sale, '.2f') , '.')


#seventh question: Miles-per-Gallon

Miles_driven = int(input('Enter the number of miles you driven:'))
Gallons_of_use = int(input('Enter the number of gallons of gas used:'))
MPG = Miles_driven / Gallons_of_use
print('Your miles per gallon is' , MPG , '.')

#eighth question: tip , tax , and total
purchase = float(input('Enter the charge of the food you order:'))
percent_tip = 0.15
percent_sales_tax = 0.07
PT = purchase * percent_tip
PST = purchase *percent_sales_tax
Total = purchase + PT + PST
print('The amount of the 15 percent tip is', format(PT , '.2f'))
print('The amount of the 7 percent sales tax', format(PST, '.2f'))
print('The total amount is', format(Total, '.2f'))


#ninth question:stock transaction program

#note to self:last month information, Joe bought shares worth of 32,870 dollars
# 657.4 owe to the broker

shares_purchased = 1000
cost_per_share = 32.87
purchased_stock = shares_purchased * cost_per_share
commission = 0.02
broker1_owe = purchased_stock * commission

#two weeks later.
#note to self that joe has to pay 678.4 in commission when he sold it.
new_stock_price =33.92
sold_stock = shares_purchased * new_stock_price
broker2_owe = sold_stock * commission
broker_total = broker1_owe + broker2_owe
leftover = sold_stock - purchased_stock - broker_total
profit = 1
loss = -1


#writing the program that is displaying the following information
print('The amount that Joe paid for the stock is', purchased_stock ,'.')
print('The amount of commission that Joe had to paid when he brought it' , \
      'is' ,broker1_owe,)
print('The amount that Joe sold the stock for is ', sold_stock , '.')
print('The amount of commission Joe had to pay when he sold is ', broker2_owe , '.')
if leftover >= profit:
    print('Joe made a profit with a balance of', format(leftover, '.2f'))
else:
    print('Joe lost money as his balance is', format(leftover,'.2f'))











                 








