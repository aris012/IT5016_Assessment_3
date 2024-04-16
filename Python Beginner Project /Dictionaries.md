## Python useful method for dictionaries

#### Sample code to use for dictionaries

        user_role = {'Dan': 'read',
                     'Paula' : 'edit',
                     'Bradley' : 'edit'
                     'Devin' : 'admin'}

        user = input('Enter username: ')

        if user_role.get(user) == 'read':
            print('Access Denied')
        elif user_role.get(user) in ('edit', 'admin'):
            print('Access Granted')
        else:
            print('Please enter a valid username')

This is also a good practice for 'if' 'elif' and 'else'.
