print("SUM and AVERAGE of elements in a list\n")
lst=[]
sum=0
n=int(input("enter no. of elements:"))
for i in range(0,n):
    elements=float(input(f"enter element {i+1}:"))
    lst.append(elements)
    sum+=lst[i]
    average=sum/n
print("your list is",lst)
print("sum of elements in" ,lst,"is",sum)
print("average of elements in" ,lst,"is",average)
