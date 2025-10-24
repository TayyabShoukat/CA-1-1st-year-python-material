from package.studentInfo import show
from package.calculator import sum,multiply
from package.square import square

def main():
    show()
    print(sum(10,20,30)+100)
    multiply(10,20)
    print("Square is:",square(10)+2)


if __name__== "__main__":
    main()