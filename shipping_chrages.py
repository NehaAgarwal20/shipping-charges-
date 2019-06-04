'''An online retailer provides express shipping for many of its items at a rate of $10.95
for the first item, and $2.95 for each subsequent item. Write a function that takes the
number of items in the order as its only parameter. Return the shipping charge for
the order as the function’s result. Include a main program that reads the number of
items purchased from the user and displays the shipping charge.'''



def shippingchr(n):
    if(n==1):
        fitem = 10.95
        return fitem
    elif(n>1):
        x = (10.95 + (n*(2.95)))
        print("Total rupees of shipping charges ")
        return x
    else:
        print("check the number of item")
n=int(input("Enter the number of items:"))
shippingchr(n)    
    