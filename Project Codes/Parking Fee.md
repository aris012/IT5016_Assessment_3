## Parking Fee 
#### A sample parking fee code program with calculated cost of parking return statement.

        def parking_fee(hours):
        #first_2hours = 4 fee
            if hours <= 2:
                fee = 4
            else:
                fee = 4 + (hours - 2) * 3
            return(fee)
   
        hours = int(input("Enter Number of Hours...\n" ))
        total_fee = parking_fee(hours)
        print(total_fee)
