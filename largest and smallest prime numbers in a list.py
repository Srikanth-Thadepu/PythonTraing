def prime(n):
    if n<2:
        return False
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return False
    return True
def get_input():
    l1=[]
    starting=int(input("Enter the starting range: "))
    ending=int(input("Enter the ending range: "))
    return l1,starting,ending

def prime_list(l1,starting,ending):
    for i in range(starting,ending+1):
        if prime(i):
            l1.append(i)
    return l1

def display(l1,starting,ending):
    print(f"The list of prime numbers between {starting} and {ending} is: ",l1)
    print("The smallest prime number of the list is: ",l1[0])
    print("The largest prime number of the list is: ",l1[-1])

def main():
    l1,starting,ending=get_input()
    l1=prime_list(l1,starting,ending)
    display(l1,starting,ending)
main()