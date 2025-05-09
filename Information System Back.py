print("BASIC INFORMATION SYSTEM")
#Name:
First_Name = input("Enter First Name: ")
Second_Name = input("Enter Second Name: ")
Full_Name = First_Name + " " + Second_Name
print(Full_Name)

#Age(from Birthyear)
Birthyear = input("Enter Birthyear: ")
Age = 2025 - int(Birthyear)
print("You're " + str(Age))

#Gender
while True:
    Gender = input("Enter Gender Male/Female: ")

    if Gender == "Male":
        print("Gender: " + Gender)
        break
    elif Gender == "Female":
        print("Gender: " + Gender)
        break
    else:
        print("Try Again")


#Civil Status
while True:
        Civil_Status = input("Enter Civil Status: (Married/N-Married): ")

        if Civil_Status == "Married":
           print(Civil_Status)
           break
        elif Civil_Status == "N-Married":
           print(Civil_Status)
           break
        else:
           print("Try Again")

#Address
Address = input("Enter Adress: ")
print(Address)

#Employment Status
while True:
    Emp = input("Enter your Job Title (type 'None' if unemployed): ")

    if Emp.strip().lower() == "none":  # Allow "none", "None", "NONE", etc.
        print("File for Employment")
        break
    elif Emp.strip() != "":  # Accept any non-blank input as a job title
        print("Job Title: " + Emp)
        break
    else:
        print("Try Again — Job Title cannot be blank\n")




#Nationality
while True:
       Nation = input("Enter Nation: ")
       if Nation != "":
          print("")
          break
       elif Nation == "None":
          print("Alien")
          break
       else:
          print("Try Again")

#Contact Number

Num = input("Enter Number: ")
print(Num)



# Displaying the summary of all information in a table-like format
print("\n--- Summary of Your Information ---")
print(f"{'Status':<20}{'Information'}")  # Header
print("-" * 40)

# Printing each line with column alignment
print(f"{'Name:':<20}{Full_Name}")
print(f"{'Age:':<20}{Age}")
print(f"{'Gender:':<20}{Gender}")
print(f"{'Civil Status:':<20}{Civil_Status}")
print(f"{'Address:':<20}{Address}")
print(f"{'Employment Status:':<20}{Emp}")
print(f"{'Nationality:':<20}{Nation}")
print(f"{'Contact Number:':<20}{Num}")