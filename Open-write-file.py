

# opeing a file 
file1 = open("myfile.txt")  
print(file1.read())
file1.close()

# Writing/ editing a file 
file1 = open("myfile.txt", "a")
file1.write("\nWriting to file :)")
file1.close()
