fhand = open('sales_log.txt', 'w')

print('========================================')
print('    SALES RECORD MANAGEMENT SYSTEM   ')
print('========================================')
print('1. Add Sale Record')
print('2. View All Records & Summary Statistics')
print('3. Clear All Sales Data')
print('4. Exit System')
print('========================================')


quantiy = 0
price_per_unit = 0
total_amount = quantiy * price_per_unit

try:
    user_input = int(input('Choose from option 1 to 4:'))
    if user_input == 1:
        user_prompt = input(str('Item name: '))
        quantiy = int(input('Quantity Sold: '))
        price_per_unit = float(input('Price per unit: '))

        print(total_amount)

    if user_input == 2:
        print("No records found")

    elif user_input == 3:
        print("All records cleared. No records remaining")

    elif user_input == 4:
        print("Thank you for using the Sales Record Management System")
        exit()


except ValueError:
        print('Wrong input')
