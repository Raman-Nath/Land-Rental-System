import display
import writeLand
import datetime
import operation
import readLand

currentDate = datetime.datetime.now().date()
landDetails=readLand.readLand()

def generateRentInvoice(customer, address, phoneNumber, rentLand, rentDuration, emailAddress):
    
    invoice = "\n"+"--------------------------------------------------------------------------------------------------"+"\n"
    invoice += "                                    Rented Land Invoice"
    invoice += "\n"+"--------------------------------------------------------------------------------------------------"+"\n\n"
    invoice += "Customer Name: " + customer + "\n" 
    invoice += "Customer Phone Number: " + str(phoneNumber) + "\n"
    invoice += "Customer Address: " + address + "\n"
    invoice += "Customer Email Address: " + emailAddress + "\n"
    invoice += "Rent Date: " + str(currentDate) + "\n"
    invoice += "Rent Duration: " + str(rentDuration) + " month(s)" + "\n"
    invoice += "\n"+"--------------------------------------------------------------------------------------------------"+"\n"  
    invoice += "| Kitta Number | City                  | Direction         | Anna             | Price            |"
    invoice += "\n"+"--------------------------------------------------------------------------------------------------"+"\n" 
    
    totalAmount = 0
    for rowOfLand in rentLand:
        kittaNumber=rowOfLand[0]
        city=rowOfLand[1]
        direction=rowOfLand[2]
        anna=rowOfLand[3]
        price = int(rowOfLand[4]) * rentDuration
        totalAmount += price
        invoice +=("| "+ str(kittaNumber)+ " " * (13 - len(str(kittaNumber)))+              
                   "| "+ city+ " " * (22 - len(city))+
                   "| "+ direction+ " " * (18 - len(direction))+
                   "| "+ str(anna)+ " " * (17 - len(str(anna)))+
                   "| Rs "+ str(price)+ " " * (14 - len(str(price)))+"|"+"\n"
        )
    invoice += "--------------------------------------------------------------------------------------------------"+"\n"
    invoice += "\nTotal Amount: NPR " + str(totalAmount) + "\n\n"
    invoice += "--------------------------------------------------------------------------------------------------"+"\n\n"
    invoice += "We sincerely appreciate your decision to choose our system."+"\n\n"
    invoice += "For any furthur inquiry or assistance, you can contact us via RamanNath@gmail.com or 9876543210."+"\n\n"
    invoice += "--------------------------------------------------------------------------------------------------"
    return invoice

def rentLand(landDetails):
    rentLand = []
    print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
    print("                           ★ Greetings! You are renting land ★")
    print("                         -----------------------------------------")
    print("                            Please provide us your information.")
    print("──────────────────────────────────────────────────────────────────────────────────────────────────")
    while True:        
        customer = input("\nEnter customer name: ")                        
        if customer == "":
            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
            print("                  Customer name cannot be empty. Please enter a valid customer name.")
            print("──────────────────────────────────────────────────────────────────────────────────────────────────")
        else:
            break
    while True:
        address = input("\nEnter customer address: ")
        if address == "":
            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
            print("                      Address cannot be empty. Please enter a valid address.")
            print("──────────────────────────────────────────────────────────────────────────────────────────────────")
        else:
            break
    while True:
        try:
            phoneNumber = int(input("\nEnter your phone number: "))
            break
        except ValueError:  
            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")                   
            print("                       Invalid number! Please enter a valid phone number.")
            print("──────────────────────────────────────────────────────────────────────────────────────────────────")

    while True:
        emailAddress = input("\nEnter customer email address: ")
        if emailAddress == "":
            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
            print("                   Email address cannot be empty. Please enter a valid address.")
            print("──────────────────────────────────────────────────────────────────────────────────────────────────")
        else:
            break

    display.printLand(landDetails)
    
    while True:
        try:
            kittaNumber = int(input("\nEnter kitta number to rent: "))
            found = False
            for rowOfLand in landDetails: 
                if int(rowOfLand[0]) == kittaNumber:
                    found = True
                    if rowOfLand[5] == "Available":
                        rentLand.append(rowOfLand)
                        while True:
                            more = input("\nDo you want to rent more lands (y/n)?: ")
                            if more.lower() == 'n':
                                while True:
                                    try:
                                        rentDuration = int(input("\nEnter duration of rent (in months): "))
                                        if rentDuration <= 0:
                                            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                                            print("                         Invalid duration! Duration must be greater than 0.")
                                            print("──────────────────────────────────────────────────────────────────────────────────────────────────")
                                            continue
                                        break
                                    except ValueError:
                                        print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                                        print("                 Invalid input! Please enter a valid number for duration.")
                                        print("──────────────────────────────────────────────────────────────────────────────────────────────────")                                
                                    
                                rentInvoice = generateRentInvoice(customer, address, phoneNumber, rentLand, rentDuration, emailAddress)                            
                                print(rentInvoice)                                
                                print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                                print("                             Land has been rented successfully.")
                                print("──────────────────────────────────────────────────────────────────────────────────────────────────")
                                rentInvoiceName = customer+"-"+"Rent"+"-"+str(operation.dateAndTime())+".txt"
                                file=open(rentInvoiceName,"w")
                                file.write(rentInvoice)
                                # Update status of rented lands and write updated landDetails to land.txt
                                for rowOfland in rentLand:
                                    kittaNumber = int(rowOfland[0])
                                    for rowOfland in landDetails:
                                        if int(rowOfland[0]) == kittaNumber:
                                            rowOfland[5] = "Not Available" 
                                writeLand.writeLand(landDetails)                                
                                return rentLand, rentDuration
                            
                            if more.lower() == 'y':
                                break
                            else:
                                print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                                print("                            Invalid input. Please enter 'y' or 'n'.")  
                                print("──────────────────────────────────────────────────────────────────────────────────────────────────")                             
                    
                    else:
                        print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                        print("                         This land is not available for rent.")
                        print("──────────────────────────────────────────────────────────────────────────────────────────────────")
            if not found:
                print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                print("                                Please enter a valid Kitta Number.")  
                print("──────────────────────────────────────────────────────────────────────────────────────────────────")
        except ValueError:
            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
            print("                   Invalid Kitta Number! Please enter a valid Kitta Number.")
            print("──────────────────────────────────────────────────────────────────────────────────────────────────")



def generateReturnInvoice(customer, address, phoneNumber, returnLand, rentDuration, returnDuration, emailAddress):
    
    invoice = "\n"+"--------------------------------------------------------------------------------------------------"+"\n"
    invoice += "                                    Returned Land Invoice"
    invoice += "\n"+"--------------------------------------------------------------------------------------------------"+"\n\n"
    invoice += "Customer Name: " + customer + "\n" 
    invoice += "Customer Phone Number: " + str(phoneNumber) + "\n"
    invoice += "Customer Address: " + address + "\n"
    invoice += "Customer Email Address: " + emailAddress + "\n"
    invoice += "Rent Date: " + str(currentDate) + "\n"
    invoice += "Rent Duration: " + str(returnDuration) + " month(s)" + "\n"
    invoice += "\n"+"--------------------------------------------------------------------------------------------------"+"\n"  
    invoice += "| Kitta Number | City                  | Direction         | Anna             | Price            |"
    invoice += "\n"+"--------------------------------------------------------------------------------------------------"+"\n" 
    
    totalAmount = 0
    totalLateAmount = 0
    lateFine=0
    for rowOfLand in returnLand:
        kittaNumber=rowOfLand[0]
        city=rowOfLand[1]
        direction=rowOfLand[2]
        anna=rowOfLand[3]
        price=rowOfLand[4]
        if returnDuration>rentDuration:
            lateFine=(returnDuration-rentDuration)*int(price) # Assuming price is for per month rented
        else:
            lateFine=0                    
        totalLateAmount+=int(lateFine)  
        totalPrice = int(rowOfLand[4]) * returnDuration
        totalAmount += int(rowOfLand[4]) * rentDuration # Total amount= Duration of rent×Price per month
        # totalAmount += totalPrice
        invoice +=("| "+ str(kittaNumber)+ " " * (13 - len(str(kittaNumber)))+              
                   "| "+ city+ " " * (22 - len(city))+
                   "| "+ direction+ " " * (18 - len(direction))+
                   "| "+ str(anna)+ " " * (17 - len(str(anna)))+
                   "| Rs "+ str(totalPrice)+ " " * (14 - len(str(totalPrice)))+"|"+"\n"
        )
    invoice += "--------------------------------------------------------------------------------------------------"+"\n\n"
    if int(lateFine) > 0: 
        invoice += "\nTotal Fine: NPR " + str(totalLateAmount) + "\n"

    total=str(totalAmount+totalLateAmount)
    invoice += "\nTotal Amount: NPR " + str(total) + "\n\n"
    invoice += "--------------------------------------------------------------------------------------------------"+"\n\n"
    invoice += "We sincerely appreciate your decision to choose our system."+"\n\n"
    invoice += "For any furthur inquiry or assistance, you can contact us via RamanNath@gmail.com or 9876543210."+"\n\n"
    invoice += "--------------------------------------------------------------------------------------------------"
    return invoice

def returnLand(landDetails, rentDuration):
    returnLand=[]
    print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
    print("                          ★ Greetings! You are returning land ★")
    print("                         -----------------------------------------")
    print("                           Please provide us your information.")
    print("──────────────────────────────────────────────────────────────────────────────────────────────────")
    while True:        
        customer = input("\nEnter customer name: ")                        
        if customer == "":
            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
            print("                  Customer name cannot be empty. Please enter a valid customer name.")
            print("──────────────────────────────────────────────────────────────────────────────────────────────────")
        else:
            break
    while True:
        address = input("\nEnter customer address: ")
        if address == "":
            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
            print("                      Address cannot be empty. Please enter a valid address.")
            print("──────────────────────────────────────────────────────────────────────────────────────────────────")
        else:
            break
    while True:
        try:
            phoneNumber = int(input("\nEnter your phone number: "))
            break
        except ValueError:  
            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")                   
            print("                       Invalid number! Please enter a valid phone number.")
            print("──────────────────────────────────────────────────────────────────────────────────────────────────")

    while True:
        emailAddress = input("\nEnter customer email address: ")
        if emailAddress == "":
            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
            print("                   Email address cannot be empty. Please enter a valid address.")
            print("──────────────────────────────────────────────────────────────────────────────────────────────────")
        else:
            break

    display.printLand(landDetails)
    while True:
        try:
            kittaNumber = int(input("\nEnter kitta number to return: "))
            found = False
            for rowOfLand in landDetails: 
                if int(rowOfLand[0]) == kittaNumber:
                    found = True
                    if rowOfLand[5] == "Not Available":
                        returnLand.append(rowOfLand)
                        
                        while True:
                            more = input("\nDo you want to return more lands (y/n)?: ")
                            if more.lower() == 'n':
                                while True:
                                    try:
                                        returnDuration = int(input("\nEnter duration of return (in months): "))
                                        if returnDuration <= 0:
                                            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                                            print("                         Invalid duration! Duration must be greater than 0.")
                                            print("──────────────────────────────────────────────────────────────────────────────────────────────────")
                                            continue
                                        break
                                    except ValueError:
                                        print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                                        print("                 Invalid input! Please enter a valid number for duration.")
                                        print("──────────────────────────────────────────────────────────────────────────────────────────────────")                                
                                    
                                returnInvoice = generateReturnInvoice(customer, address, phoneNumber, returnLand, rentDuration, returnDuration, emailAddress)                            
                                print(returnInvoice)                                
                                print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                                print("                             Land has been returned successfully.")
                                print("──────────────────────────────────────────────────────────────────────────────────────────────────")
                                returnInvoiceName = customer+"-"+"Return"+"-"+str(operation.dateAndTime())+".txt"
                                file=open(returnInvoiceName,"w")
                                file.write(returnInvoice) 
                                # Update status of rented lands and write updatedlandDetails to land.txt
                                for rowOfLand in returnLand:
                                    kittaNumber = int(rowOfLand[0])
                                    for rowOfLand in landDetails:
                                        if int(rowOfLand[0]) == kittaNumber:
                                            rowOfLand[5] = "Available" 
                                writeLand.writeLand(landDetails)                              
                                return returnLand
                            
                            if more.lower() == 'y':
                                break
                            else:
                                print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                                print("                            Invalid input. Please enter 'y' or 'n'.")  
                                print("──────────────────────────────────────────────────────────────────────────────────────────────────")                             
                        
                    else:
                        print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                        print("                         This land is available for rent.")
                        print("──────────────────────────────────────────────────────────────────────────────────────────────────")
            if not found:
                print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                print("                                Please enter a valid Kitta Number.")  
                print("──────────────────────────────────────────────────────────────────────────────────────────────────")
        except ValueError:
            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
            print("                 Invalid Kitta Number. Please enter a valid Kitta Number.")
            print("──────────────────────────────────────────────────────────────────────────────────────────────────")
    

