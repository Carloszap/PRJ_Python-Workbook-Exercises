# This program display area of a field in acres.

length = float(input("Please enter length of field in feet: "))
width = float(input("Please enter width of field in feet: "))
area_feet = length * width
              
acre_in_feets = 43560
area_acre = area_feet / acre_in_feets

print(f"The area of the field is {area_acre} acres.")