## Countdown Coding
#### Project countdown coding

        import time


        print("Welcome to Count Down Timer")
        my_time = int(input("Please enter the number of seconds to count \n"))
        print("Starting...")
        for x in range(my_time, 0, -1):
            print(x)
            time.sleep(1)


        print("TIME'S UP!!!")
