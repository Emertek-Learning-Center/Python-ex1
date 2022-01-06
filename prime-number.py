#In this script we will display all the prime numbre in a given interval#
#########################################################################

#This function return true if the number is prime
def isPrime(nb):
    if nb==1:
        return False
    for i in range(2,int(nb/2)+1):
        if nb % i == 0:
            return False
    return True

#Main programe

#The user should enter the interval
print("the interval start from: ")
start = int(input())
print("the interval end with: ")
end = int(input())

#Verify if number is prime for each number
for i in range(start,end):
    if isPrime(i):
        print(i, end="\t")
