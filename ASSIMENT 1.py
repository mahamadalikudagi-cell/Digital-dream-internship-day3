item_prices = [5000.00,200.00,2000.00,6000.00,15000.00]

total_order_value = sum(item_prices)

average_item_price = total_order_value / len(item_prices)

print("Item Prices:", item_prices)
print("Total Order Value:", total_order_value)
print("Average Item Price:", average_item_price)