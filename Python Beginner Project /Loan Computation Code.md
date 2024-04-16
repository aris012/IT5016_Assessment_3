## Loan Computation code 

Mini calculator project of loan computation

Get loan info from user

      loan = int(input('Please Enter Loan Amount: '))
      term = int(input('Please Enter Loan Term: '))
      rate = float(input('Please Enter the Loan Rate: '))
      down = int(input('Please Enter Down Payment: '))

Calculate loan

      months = term * 12
      rate_monthly = rate / 100 / 12
      payment = (rate_monthly / (1- (1+ rate_monthly) ** (-months))) * (loan - down)

Return Monthly payment

       print('Your mothly payment is: ' + '$' + str(round(payment,2))
