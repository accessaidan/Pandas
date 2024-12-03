import pandas as pd


# Outputs the initial menu and checks validates the input
############################################################
###################### MAIN MENU ###########################
############################################################
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Recoats Adventure Park ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total income by source")
        print("### 2. Change in income sources and payment methods")
        print("### 3. Total income by day")
        

        choice = input('Enter your number selection here: ')

        arr_valid_choice = ["1","2","3"]
        if choice in arr_valid_choice:
            print("Thank you")
            flag = False
            return choice
        else:
            print("Sorry that was not a valid option")

############################################################
#################### MENU OPTION 1 #########################
############################################################

# Submenu for totals, provides type check validation for the input
def menu_option_1():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total income by source ##############")
        print("####################################################")
        print("")
        print("########## Please select an income source ##########")
        print("")
        print("### 1. Tickets")   
        print("### 2. Gift Shop") 
        print("### 3. Snack Stand")  
        print("### 4. Pictures")

        choice = input('Enter your number selction here: ')
        arr_valid_choice = ["1","2","3","4"]
        if choice in arr_valid_choice:
            print("Choice accepted")
            flag = False
            return choice
        else:
            print("Sorry that was not a valid option")
  

# takes the total submenu input and converts the number to a string of the source name
def convert_1(total_men_choice):
    
    if total_men_choice == "1":
        tot_choice = "Tickets"
    elif total_men_choice == "2":
        tot_choice = "Gift Shop"
    elif total_men_choice == "3":
        tot_choice= "Snack Stand"
    else:
        tot_choice = "Pictures" 
    
    return tot_choice

# creates a new dataframe with the selected income source then creates a total row
# outputs the final total in a message
def income_by_source(total_choice):
    df = pd.read_csv("Pandas\\task_4-data.csv")
    income = df[["Day", total_choice]]

    total = income[total_choice].sum()

    msg = "The total income from {} was: £{}".format(total_choice, total)
    return msg


############################################################
#################### MENU OPTION 2 #########################
############################################################

def menu_option_2():
    flag = True

    while flag:

        print("####################################################")
        print("####### Change in payment type annd sources ########")
        print("####################################################")
        print("")
        print("Please select the payment type you would like to view")
        print("")
        print("### 1. Cash payments")
        print("### 2. Card paymets")

        choice = input('Enter your number selction here: ')
        arr_valid_choice = ["1","2"]
        if choice in arr_valid_choice:
            print("Choice accepted")
            flag = False
            return choice
        else:
            print("Sorry that was not a valid option")

def payment_methods(type):
    df = pd.read_csv("Pandas\\task_4-data.csv")
    print("")
    print("With", type)
    tickets = sum(df['Tickets'][df['Pay Type'] == type])
    print(tickets, "Tickets were sold")
    gift_shop = sum(df['Gift Shop'][df['Pay Type'] == type])
    print(gift_shop,"Items were bought from the gift shop")
    snack_stand = sum(df['Snack Stand'][df['Pay Type'] == type])
    print(snack_stand, "Items were bought at the snack stand")
    pictures = sum(df['Pictures'][df['Pay Type'] == type])
    print("And", pictures, "Pictures were taken")



############################################################
#################### MENU OPTION 3 #########################
############################################################

def menu_option_3():
    flag = True

    while flag:

        print("####################################################")
        print("########### Difference in days of week #############")
        print("####################################################")
        print("")
        print("##### Please select the day you want to view #######")
        print("")
        print("### 1. Monday ")
        print("### 2. Tuesday")
        print("### 3. Wednesday")
        print("### 4. Thursday")
        print("### 5. Friday")
        print("### 6. Saturday")
        print("### 7. Sunday")

        choice = input('Enter your number selction here: ')
        arr_valid_choice = ["1","2","3","4","5","6","7"]
        if choice in arr_valid_choice:
            print("Choice accepted")
            flag = False
            return choice
        else:
            print("Sorry that was not a valid option")

def day_of_week(choice):
    df = pd.read_csv("Pandas\\task_4-data.csv")
    print("")
    print("Across all " + choice +"s")
    tickets = sum(df['Tickets'][df['Day'] == choice])
    print(tickets, "Tickets were sold")
    gift_shop = sum(df['Gift Shop'][df['Day'] == choice])
    print(gift_shop,"Items were bought from the gift shop")
    snack_stand = sum(df['Snack Stand'][df['Day'] == choice])
    print(snack_stand, "Items were bought at the snack stand")
    pictures = sum(df['Pictures'][df['Day'] == choice])
    print("And", pictures, "Pictures were taken")




############################################################
####################### MENU  ##############################
############################################################

main_menu_choice = main_menu()
if main_menu_choice == "1":
    total_men_choice = menu_option_1()
    total_choice = convert_1(total_men_choice)
    print(income_by_source(total_choice))

elif main_menu_choice == "2":   # how payment types and income sources havae changed quarterly
    total_men_choice = menu_option_2() # asks which oaymetn type they want to see
    if total_men_choice == "1": # change in income sources
        type = 'Card'
        payment_methods(type)

    elif total_men_choice == "2": # change in payment types
        type = 'Cash'
        payment_methods(type)




elif main_menu_choice == "3":   #trends and pattern for income over different days of week
    total_men_choice = menu_option_3() # asks weather they want to see total for each day

    if total_men_choice == "1": # change in income sources
        choice = 'Monday'
        day_of_week(choice)

    elif total_men_choice == "2": # tuesday
        choice = 'Tuesday'
        day_of_week(choice)
    
    elif total_men_choice == "3": # wednesday
        choice = 'Wednesday'
        day_of_week(choice)

    elif total_men_choice == "4": # thursday
        choice = 'Thursday'
        day_of_week(choice)

    elif total_men_choice == "5": # friday
        choice = 'Friday'
        day_of_week(choice)

    elif total_men_choice == "6": # saturday
        choice = 'Saturday'
        day_of_week(choice)

    elif total_men_choice == "7": # Sunday
        choice = 'Sunday'
        day_of_week(choice)

