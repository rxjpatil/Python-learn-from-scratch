print("Welcome to the Tip Calculator!")
bill = float(input("Enter the total bill! :₹"))
tip = int(input("Enter the Tip (in percent) you want to give. eg. 10, 20, 30  :"))
bill_with_tip = tip / 100 * bill + bill
print(f"Bill with Tip is :₹ {bill_with_tip}")
person = int(input("Total number of person to split the bill with?"))
bill_per_person = bill_with_tip / person
print(f"Each Person should pay total: {bill_per_person} ₹")