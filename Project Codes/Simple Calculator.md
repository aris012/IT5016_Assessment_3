## Simple Calculator
#### Creating a simple calculator that just sums 2 numbers entered by the user.

        sum = int(input("Please enter first number \n"))
        sum1 = int(input("Please enter second number \n"))


        def add(s1,s2):
            sums = s1 + s2
            return sums


        total = add(sum,sum1)


        print("------------------")
        print("The answer is ", total)
