import sys

def show_sales():
    with open('bakery.csv', encoding='utf-8') as f:
        for val in f:
            print(val.strip())

def show_sales_num_1(num_1):
    with open('bakery.csv', encoding='utf-8') as f:
        a = []
        for val in f:
            a.append(val.strip())
        num_1 -= 1
        for i in range(len(a)):
            if i >= num_1:
                print(a[i])
            else:
                pass

def show_sales_num_2(num_1, num_2):
    with open('bakery.csv', encoding='utf-8') as f:
        a = []
        for val in f:
            a.append(val.strip())
        num_1 -= 1
        num_2 -= 1
        for i in range(len(a)):
            if i >= num_1 and i <= num_2:
                print(a[i])
            else:
                pass

num = len(sys.argv)

if num == 2:
    num_1 = int(sys.argv[1])
    show_sales_num_1(num_1)
elif num == 3:
    num_1 = int(sys.argv[1])
    num_2 = int(sys.argv[2])
    show_sales_num_2(num_1, num_2)
else:
    show_sales()