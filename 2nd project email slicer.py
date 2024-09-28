#Ask to enter any email
email = input("Enter Email : ")

#remove any unncessary white space
email = email.strip()

username = email[:-10] # sinhabhishek08054
domain_name = email[-10:] # @gmail.com

#print the result separatly
print("\n\tYour username name is ", username, " and your doamin is ", domain_name + '\n')
