opening_stock = [100, 50, 75, 200]   
closing_stock = [90, 60, 70, 210] 
product = ["product A", "product B", "product C", "product D"]   


# for i in range(len(opening_stock)):
#     if closing_stock[i] > opening_stock[i]:
#         print(f"Product {i+1}: Stock Increased")
#     elif closing_stock[i] < opening_stock[i]:
#         print(f"Product {i+1}: Stock Reduced")
#     else:
#         print(f"Product {i+1}: Stock Unchanged")

for i in range(len(product)):
    if closing_stock > opening_stock:
        print(product[i],"stock increased")
    elif(closing_stock < opening_stock):
        print(product[i],"stock reduced")
    else:
        print(product[i],"stock unchanged")