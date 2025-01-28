def get_input():
    l1=[]
    n=int(input("Enter the size of the list: "))
    for i in range(n):
        ele=str(input("Enter the elements of the list: "))
        l1.append(ele)
    return l1

def is_palindrome(word):
    return word==word[::-1]
    
def main():
    l1 = get_input()
    for word in l1:
        if is_palindrome(word):
            print(f"{word} is a palindrome.")
        else:
            print(f"{word} is not a palindrome.")
main()