class BookOperations:
    def __init__(self,a,b,c,d,e):
        self.bookid=a
        self.bookName=b
        self.bookTechnology=c
        self.bookPrice=d
        self.authorName=e
class BookStore:
    def __init__(self,a,b):
        self.bookdb=a
        self.bookStoreName=b
    def searchByName(self,a):
        ls=[]
        for i,j in self.bookdb.items():
            if j.bookName==a:
                ls.append(j)
        return ls
    def calculatePriceByTechnology(self,a):
        b=0
        for i,j in self.bookdb.items():
            if j.bookTechnology==a:
                b+=j.bookPrice
        """else:
            return 0"""
        b-=(10*b)/100
        return b

book={}
for _ in range(int(input())):
    a=int(input())
    b=input()
    c=input()
    d=int(input())
    e=input()
    book[a]=BookOperations(a,b,c,d,e)
res=BookStore(book,"abc")
f=res.searchByName(input())
if len(f)==0:
    print("No Book Exixts with the book name")
else:
    for i in f:
        print(i.bookid)
        print(i.bookName)
        print(i.bookTechnology)
        print(i.bookPrice)
        print(i.authorName)
        
g=res.calculatePriceByTechnology(input())
if g!=0:
    print(g)
else:
    print("0.0")
