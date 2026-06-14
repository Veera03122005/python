"""Write a program that asks for a product price and quantity, then prints a neatly 
formatted bill showing item total, a 5% tax amount, and the grand total - all aligned and 
formatted to 2 decimals using f-strings."""
product_price = float(input("Enter the product price: "))
quantity = int(input("Enter the quantity: "))
print("******************Bill************************")
tax_rate = 0.05
total_bill = product_price * quantity
total_including_tax = total_bill + (total_bill * tax_rate)
print(f"Item Total:       {quantity}")
print(f"Total bill:       {total_bill:>5.2f}")
print(f"Tax Amount(5%):   {total_bill * tax_rate:>5.2f}")
print(f"Grand Total:      {total_including_tax:>5.2f}")
print("*********************X************************")
