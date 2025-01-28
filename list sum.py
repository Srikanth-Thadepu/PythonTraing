def sum(list):
    sum=0
    for i in range(len(list)):
        sum=sum+list[i]
    return sum
def main():
    list=[]
    n=int(input("Enter the size of list"))
    for i in range(n):
        ele=int(input("Enter the elements: "))
        list.append(ele)
    print("The sum of the elements of the list is: ",sum(list))
main()