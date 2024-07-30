def readLand():
    file=open("land.txt","r")
    landDetails=[]
    for lands in file.readlines():
        landDetails.append(lands.replace("\n","").split(","))
    return landDetails
    
