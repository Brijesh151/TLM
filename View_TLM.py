def main_menu():
  print(' \nWELCOME TO TERMINAL LIBRARY MANAGEMENT SYSTEM (TLM)\n ')
  print('-------------L I B R A R Y    M E N U--------------- ')
  print("Enter 1- Log in as Librarian/Admin \nEnter 2- Log in as User/Member \nEnter 0- Close Application")
  while True:
    choice=int(input("Please Enter Your Option-->"))
    if choice<=2:
      break
    else:
      print("Invalid Entry By You...Please Try Again!")
  return choice 

def user_validation():

  # Write a code to ask user name pwd and validate it with database.
  # The user role will be decided based on the value of choice in main menu.
  # login_details=dict()
  # login_details["email"]=input("Please Enter Your User Name(Email)-->")
  # login_details["password"]=input("Please Enter Your Password-->")
  # return login_details
  email = input("Please Enter Your User Name(Email)-->")
  password = input("Please Enter Your Password-->")
  return email, password

def librarian_menu():
  print("Enter 1- Add User \nEnter 2- Add Books \nEnter 3- Update User Details"
  "\nEnter 4- Update Book Details \nEnter 5- Delete User \nEnter 6- Delete Books"
  "\nEnter 7- Books Details \nEnter 8- List of Books Available \nEnter 9- Fine Amount \nEnter 0- Close Application")
  while True:   
      choice=int(input("Please Enter Your Option-->"))
      if choice<=9:
        break
      else:
          print("Invalid Entry By You...Please Try Again!")
  return choice
  
def user_menu():
  print("Enter 1- Register/Add User \nEnter 2- Update User Details \nEnter 3- Delete User"
  "\nEnter 4- Books Details \nEnter 5- List of Books Available \nEnter 6- Fine Amount"
  "\nEnter 7- Rental Operations- Issue/Checkout Book \nEnter 8- Return Book \nEnter 0- Close Application")
  while True:
      choice=int(input("Please Enter Your Option-->"))
      if choice<=8:
        break
      else:
          print("Invalid Entry By You...Please Try Again!")
  return choice
