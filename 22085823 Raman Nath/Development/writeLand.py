def writeLand(landDetails):
    # Write the updated landDetails to the land.txt file
    file = open("land.txt", "w")
    for row in landDetails:
        file.write(",".join(row) + "\n") 
    file.close()