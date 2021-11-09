#6
#import array as arr

#numbers = arr.array("i",[15, 8, 31, 47, 2, 19])
#mean = 0
#for i in range (len(numbers)):
    #mean += numbers[i]

#mean/len(numbers)

#print("The result is", mean/len(numbers))


#7

#import array
#numbers = [1,2,3,4,5,6]
#even = 0
#odd = 0
#for i in range (len(numbers)):
    #if (numbers[i]%2==0):
        #even +=1
    #else:
        #odd +=1

#print("even", even)
#print("odd", odd)


#8
#import array

#numbers = [-15, 8, -31, 47, -2, 19]

#print(max(numbers))
#print(min(numbers))
  #źle

#import array

#numb = [-15, 8, -31, 47, -2, 19]

#max = numb[1]
#min = numb[1]

#for i in range (len(numb)):
    #if (numb[i]>max):
        #max=numb[i]
    #if (numb[i]<min):
        #min=numb[i]
        
#print(max)
#print(min)
        
        
        
#9
#months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

#def month(n):
    #x = months[n-1]
    #return x

#print(month(5))
        
        
#10


#numbers = [1,2,3,4,5]

#def sum(array):
    #sum=0
    #for i in range(len(array)):
      #sum+=array[i]
    #return sum
    
        
        
#def array2str(array):
    #st=""
    #for i in range(len(array)):
        #st += str(array[i])+" "
    #return st

#print (sum(numbers))
#print(array2str(numbers))     
        
        
 #11       

array1 = ["water","book","sky"]
array2 = ["water","book","sky"]

def compare(array1,array2):
    i=0
    if len(array1) != len(array2):
        return False
        
    if len(array1) == len(array2):
        while i<len(array1):
            if(array1[i] == array2[i]):
                return False
            else:
                i=i+1
            return True

print(compare(array1,array2))
            
        
        





















