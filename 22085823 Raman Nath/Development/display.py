def display():
    print("""
──────────────────────────────────────────────────────────────────────────────────────────────────
                            Welcome to TechnoPropertyNepal Company  
──────────────────────────────────────────────────────────────────────────────────────────────────
    
Greetings and welcome to TechnoPropertyNepal's Land Renting System! We're here to assist you in 
finding the perfect land for your needs in various locations across Nepal.         
                                                                                            
        ─────────────────────────────────────────────────────────────────────────────────           
        | S.N. | Please choose the following options:                                   |
        ─────────────────────────────────────────────────────────────────────────────────
        | 1.   | Display Available Lands                                                |
        | 2.   | Rent Available Lands                                                   |
        | 3.   | Return Available Lands                                                 |
        | 4.   | Comments/Feedback (if any)                                             |
        | 5.   | Exit the system                                                        | 
        ─────────────────────────────────────────────────────────────────────────────────          
""")   # This is multiline comment also called doc string.
    
    
def printLand(landDetails):
    print("\n──────────────────────────────────────────────────────────────────────────────────────────────────")
    print("                                  Available land for Rent")
    print("──────────────────────────────────────────────────────────────────────────────────────────────────\n")
    print("──────────────────────────────────────────────────────────────────────────────────────────────────")
    print("| Kitta Number | City             | Direction    | Anna         | Price        | Status          |")
    print("──────────────────────────────────────────────────────────────────────────────────────────────────")
    for rowOfLand in landDetails:        
        kittaNumber=rowOfLand[0]
        city=rowOfLand[1]
        direction=rowOfLand[2]
        anna=rowOfLand[3]
        price=rowOfLand[4]
        status=rowOfLand[5]
        
        print("|", str(kittaNumber), " " * (11 - len(str(kittaNumber))),              
              "|", city, " " * (15 - len(city)),
              "|", direction, " " * (11 - len(direction)),
              "|", str(anna), " " * (11 - len(str(anna))),
              "|", str(price), " " * (11 - len(str(price))),
              "|", status, " " * (14 - len(status)), "|"
            )
    print("──────────────────────────────────────────────────────────────────────────────────────────────────")

              
              
              
        
    
    
    
    
    
    
    