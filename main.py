from User import User

miriam_user = User("Miriam")
miriam_user.create_new_account() #The ID of your new account is: 1
miriam_user.make_a_deposit(1000,1) 
miriam_user.show_balance(1) #1000
miriam_user.withdraw_money(500,1)
miriam_user.show_balance(1) #500


miriam_user.create_new_account() #The ID of your new account is: 2
miriam_user.make_a_deposit(2000,2) 
miriam_user.show_balance(2) #2000
miriam_user.withdraw_money(500,2)
miriam_user.show_balance(2) #1500
