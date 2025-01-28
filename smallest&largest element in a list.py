def max_min(l1):
    maximum=l1[0]
    minimum=l1[0]
    for i in range(len(l1)):
        if maximum<l1[i]:
            maximum=l1[i]
        elif minimum>l1[i]:
            minimum=l1[i]
    return maximum,minimum

def display(maximum,minimum):
    print("The largest element of the list is: ",maximum)
    print("The smallest element of the list is: ",minimum)

def get_input():
    l1=[]
    n=int(input("Enter the size of list: "))
    for i in range(n):
        ele=int(input("Enter the element: "))
        l1.append(ele)
    return l1
def main():
    l1=get_input()
    maximum,minimum=max_min(l1)
    display(maximum,minimum)
    
main()
