## Learning 'If statements' 

### What is 'If statements'?

The If statement on its own produces a single branch of execution, but only if the condition is met. The else: statement is optional. If with Else should be used to produce "either" and "or" branches of execution.

"The else: statement is optional. It should be used to produce "either" and "or" branches of execution."

##### Sample of 'If statements'

          print ("Kia Ora, this is a parking meter")
        park_time = 4
        print ("park_time time is ", park_time, " hours.")
 
        rate = 4
        cost = 0
        if park_time > 3:
            cost = rate *3
            # drop the rate by $2
            rate -= 2
            # get the remainder of the parking time
            park_time -= 3
            # add to the current cost
            cost += rate * park_time
            print("The cost of the parking is $", cost)
        else:
            cost = rate * park_time
            print ("The cost of the parking is $", cost)
 
        # test case assertion 1
        '''
        park_time = 4
        total cost of parking = $14
        '''

This program is straightforward. The If else statement performs an either/or branch execution and calculates the overall value of the parking.

What might also be new in this example is the use of augmented assignment such as += and -=.
