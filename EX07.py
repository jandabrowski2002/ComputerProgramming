#Task 7


#file = open('countries.txt','r')
#file_content = file.read()
#print(file_content)
#file.close()

#Task 8


#file = open('countries.txt','r')
#x = 1
#for line in file:    
    #print(x, line, end="")
    #x += 1

#file.close()


#Task 9


#file = open('numbers.txt','r')
#sum = 0
#for line in file:
    #print(line, end="")
    #sum += int(line)
#print()
#print("Sum of the numbers is:",sum)
#file.close()


#Task 10

#file = open('numbers.txt','w')

#file.write("Jan" + "\n")
#file.write("Dąbrowski" + "\n")
#file.write("Universty of economics" + "\n")

#file.close()

#Task 11 źle, za duzo roboty :(

#film_titles = ["Titanic", "Avengers", "No Time To Die", "Harry Potter", "Hobbit"]

#file = open('numbers.txt','w')

#file.write(film_titles[0] + "\n")
#file.write(film_titles[1] + "\n")
#file.write(film_titles[2] + "\n")
#file.write(film_titles[3] + "\n")
#file.write(film_titles[4] + "\n")

#file.close()

#Task 11 git :)

#film_titles = ["Titanic", "Avengers", "No Time To Die", "Harry Potter", "Hobbit"]
#file = open('numbers.txt','w')
#sum = 0
#while sum<5:
    #file.write(film_titles[sum]+"\n")
    #sum+=1
               
#file.close()

#Task 11 for statement

#film_titles = ["Titanic", "Avengers", "No Time To Die", "Harry Potter", "Hobbit"]
#file = open('numbers.txt','w')
#k=0
#for k in film_titles:
    #file.write(film_titles[k]+"\n")
    #k+=1
#file.close()

#Task 12 źle narazie

#file = open('shopping.txt','a')
#k=0
#while k<10:
    #x = input("Enter the product name:")
    #k+=1
#file.append("{x}")
#file.close()

#Task 12

file = open('numbers.txt','a')
x = input("Enter the product name:")
file.write(x+"\n")
file.close()

















    



































