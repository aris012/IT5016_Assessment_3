## While Loops

Loops are everywhere in the real world. We make them without thinking; we wash our hands until they are clean, we pour water into a glass until it is full, and so on.

#### A loop is a continuous action that stops when a condition is met.

This is a powerful tool in programming and is used everywhere, from login web pages and EFTPOS machines, to petrol pumps that dispense fuel until a credit limit is reached, or until the user releases the petrol hose trigger.

##### Here is the example of while loop function.

        is_running = True
 
        while is_running:
            answer = input("What is the meaning of life?...\n")
            if answer == "42":
                print("Correct! Well done!\n")
                # correct answer, so exit loop - reset is_running
                is_running = False
            else:
                print("Sorry that is the wrong answer.... "
                      "Try again!\n")
 
        x = input("Press any key to exit.")
 
        '''
        # assertion test case 1
        answer = love then loop executes
 
        # assertion test case 2
        answer = 42 results in Correct! Well done!
        '''

##### Here's another example of while loop with number of tries.

        number_of_tries = 3
 
        while True:
            answer = input("What is the meaning of life?...\n")
            if answer == "42":
                print("Correct! Well done!\n")
                # correct answer, so exit loop using break
                break
            else:
                print("Sorry that is the wrong answer.... "
                      "Try again!\n")
                number_of_tries -= 1
 
            # check number of tries and break if none left
            if number_of_tries == 0:
                print("You have run out of goes. Sorry.")
                  break
 
          x = input("Press any key to exit.")
 
          '''
          # assertion test case 1
          answer = 42 results in Correct! Well done!
 
          # assertion test case 2
          answers 1,2 then 3 results in You have run out of goes
