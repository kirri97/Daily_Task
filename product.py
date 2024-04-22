def total():
   product_amount = 1000
   dicount = 20
   shipping_cost1 = 5
   shipping_cost2 = 10
   after_discount = product_amount -(product_amount * dicount/100)
   print(f"the total after discount is :  {after_discount+shipping_cost1}")
total()

def add():
         num = 3
         num2 = 2
         total = num + num2
         print(f"addition of {num} and {num2} : {total}")
add()


def swap():
      a = 10
      b = 20
      b = a
      a = a + b
      print(f"swap of a and b : {a}  {b}")

swap()



def swap1():
      a = 10
      b = 20
      temp = a
      a = b
      b = temp
      print(f"swap of a and b : {a}  {b}")

swap1()


addition = lambda x,y : x + y
x=10
y=20
print(addition(x,y))


swapp = lambda a,b : (b,a)
a = 10
b = 20
print(swapp(a,b))


def biodata():
      name = input("enter your name : ")
      age = int(input("enter your age : "))
      parents = input("enter your parents name : ")
      print(f"my biodata = my name is : {name} ; and my age  is : {age} years old ; and my parents names are : {parents}")
biodata()
