l = [12,3,4,4,56,]
k_sum = sum([i for i in l if i%2!=0 ])
print(k_sum) 

def calci(price,discount,shipping):
    discounts=price-(price*(discount))   #discount=discount/100 ==20/100 =0.2
    final=discounts+shipping
    return  final
result=calci(1000,0.2,5)
print(result)