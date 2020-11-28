class ProductManagement:
    def __init__(self,a,b,c,d):
        self.product_id=a
        self.product_name=b
        self.product_type=c
        self.product_price=d
    def apply_discount(self,a):
        self.product_price-=(a*self.product_price)/100
class Store:
    def __init__(self,a,b):
        self.store_name=a
        self.prod_list=b
    def calculate_price(self,a,b):
        ls={}
        for i in self.prod_list:
            if i.product_type==b:
                i.apply_discount(a)
                ls[i.product_name]=(i.product_price)
        return ls

ls=[]
for _ in range(int(input())):
    a=int(input())
    b=input()
    c=input()
    d=int(input())
    ls.append(ProductManagement(a,b,c,d))
st=Store("abc",ls)
f=input()
e=int(input())

res=st.calculate_price(e,f)
if res==None:
    print("Product Not Found")
else:
    r=sorted(res.items(),key=lambda x:(x[1]),reverse=True)
    for i,j in  r:
        print(i,j)
