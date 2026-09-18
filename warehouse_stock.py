warehouse_stock= {"rice_bag": 120, "cooking_oil": 45, "sugar": 0}
product_name= input("Enter a product name:")
try:
    price = warehouse_stock[product_name]
except KeyError:
    print(f"Product'{product_name}'not found!")
else:
    print(f"Product'{product_name}':{price}")
    if(price<=0):
        print("Out of stock!")
finally:
    print( "Stock check completed")    