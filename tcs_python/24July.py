class Book:
    def __init__(self,a,b,c,d):
        self.bookid=a
        self.bookName=b
        self.subject=c
        self.bookPrice=d
class Library:
    def __init__(self,a,b):
        self.libraryName=a
        self.bookList=b
    def findSubjectWiseBooks(self):
        dic={}
        for i in self.bookList:
            if i.subject in dic:
                dic[i.subject]+=1
            else:
                dic[i.subject]=1
        return dic
                
    def checkBookCategoryByPriceL(self,a):
        for i in self.bookList:
            #print (i.bookid,a)
            if (i.bookid == a):
                #print("hello",a)
                if i.bookPrice >= 1000 :
                    return "High Price"
                elif i.bookPrice <1000 and i.bookPrice >=750 :
                    return "Medium Price"
                elif i.bookPrice < 750 and i.bookPrice >=500 :
                    return "Average Price"
                else:
                    return "Low Price"
        else:
            return None
book1=[]
for _ in range(int(input())):
    a=int(input())
    b=input()
    c=input()
    d=int(input())
    book1.append(Book(a,b,c,d))
    #print(book)

libobj=Library("abc",book1)
res1=libobj.findSubjectWiseBooks()
g=int(input())
res2=libobj.checkBookCategoryByPriceL(g)
for i,j in res1.items():
    print(i,j)
print(res2)
