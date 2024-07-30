import display
import readLand
import function

def main():
    landDetails=readLand.readLand()
    display.display()
    rentDurationIndex=None
    while True:
        try:        
            choice=int(input("\nEnter your choice (1, 2, 3, 4 or 5): "))
            if choice == 1:
                display.printLand(landDetails)
                
            elif choice == 2:        
                rentDuration=function.rentLand(landDetails)
                rentDurationIndex=rentDuration[1]

            elif choice == 3:
                function.returnLand(landDetails, rentDurationIndex)

            elif choice == 4:
                input("\nProvide us your feedback (press Enter to finish):\n\n")
                print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                print("                             Thank you for your feedback!")     
                print("──────────────────────────────────────────────────────────────────────────────────────────────────")   
        
            elif choice == 5:
                print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                print("                     Thank you for using our system. Do visit again!")
                print("──────────────────────────────────────────────────────────────────────────────────────────────────\n")
                break

            else:
                print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
                print("                 Please enter your choice as (1, 2, 3, 4, or 5).")
                print("──────────────────────────────────────────────────────────────────────────────────────────────────")
        except ValueError:
            print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
            print("                         Invalid choice. Please enter a vaild choice.")
            print("──────────────────────────────────────────────────────────────────────────────────────────────────")
main()
    
