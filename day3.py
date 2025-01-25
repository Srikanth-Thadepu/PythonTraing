# # # # # def display(data):
# # # # #     print(f'The area is {data}')

# # # # # def get_input():
# # # # #     recieved_length=input('Length: ')
# # # # #     recieved_width=input('Width: ')
# # # # #     return (recieved_length,recieved_width)

# # # # # def compute_area(length,width):
# # # # #     area=int(length)*int(width)
# # # # #     return area

# # # # # def main():
# # # # #     (length,width)=get_input()
# # # # #     area=compute_area(length,width)
# # # # #     display(area)

# # # # def get_input():
# # # #     a=input('1st no: ')
# # # #     b=input('2nd no: ')
# # # #     c=input('3rd no: ')
# # # #     d=input('4th no: ')
# # # #     n=input('n: ')
# # # #     return a,b,c,d,n
# # # # def sum(a,b,c,d):
# # # #     sum=(int(a)+int(b)+int(c)+int(d))
# # # #     return sum
# # # # def average(sum,n):
# # # #     avg=sum/int(n)
# # # #     return avg
# # # # def display(data):
# # # #     print(f'the average is {data}')

# # # # def main():
# # # #     (a,b,c,d,n)=get_input()
# # # #     x=sum(a,b,c,d)
# # # #     result=average(x,n)
# # # #     display(result)
# # # # main()

# # # def get_input():
# # #     a=input('1st no: ')
# # #     b=input('2nd no: ')
# # #     c=input('3rd no: ')
# # #     return a,b,c
    
# # # def maximum(a,b,c):
# # #     if a>b and a>c:  
# # #         return a
# # #     elif b>c and b>a:
# # #         return b
# # #     elif c>a and c>b:
# # #         return c
                
# # # def display(data):
# # #     print(f'{max_var} storing {data} is the maximum variable')

# # # def main():
# # #     (a,b,c)=get_input()
# # #     value=maximum(a,b,c)
# # #     display(value)
# # # main()
# # import dis

# # def get_input():
# #     a=input('Enter the value of a: ')
# #     b=input('Enter the value of b: ')
# #     return a,b
# # def multiply(a,b):
# #     product=int(a)*int(b)
# #     return product
# # def display(data):
# #     print(f'Product of the numbers is: {data}')
# # def main():
# #     a,b=get_input()
# #     value=multiply(a,b)
# #     display(value)
# #     dis.dis(get_input)
# # main()

# def prime(n):
#     for i in range(2,int((n**0.5)+1)):
#         if n%i==0:
#             return False
#     return True
# def main():
#     n=int(input('Enter value of n: '))
#     for i in range(2,n+1):
#         if prime(i):
#             print(i)
# main()

def prime(n):
    i=2
    while(i<=int(n**0.5)):
        if n%i==0:
            return False
        i+=1
    return True
def main():
    i=2
    n=int(input('Enter the value of n: '))
    while(i<=n):
        if prime(i):
            print(i)
        i+=1
main()