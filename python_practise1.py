#p1:Given two integer numbers return their product only ,if the product is equal to or lower than 1000, else return their sum.
from operator import truediv


def multiplication_or_sum(num1,num2):
    #calculate the product of the two number 
    product=num1*num2
    if product<=1000:
        return product
    else :
        return num1 + num2
            
            
#first condition
result =multiplication_or_sum(20, 30)
print ("the result is ", result)

#second condition
result =multiplication_or_sum(40, 30)
print ("the result is", result)

#Print the sum of the current number and the previous number

print("printing current number and previous number and there sum(10)" )
previous_num_=0
# for loop 1 to 10
for i in range(10):
    x_sum=previous_num_+i
    print("current num",i ,"previous num",previous_num_,"sum:",x_sum)
    #modify the previous num
    #set it to the current number
    previous_num_=i

#Print characters from a string that are present at an even index number
word =input("enter the word")
print("original string:",word)
# get the lenght of the string
size=len(word)
#ieterate each character of strings
#start :0 to starts with first character of the word
#stop: size -1 because index starts with 0 
#step 2 : to get the characters present at even index like 0,2,4
print("printing only even index char")
for i in range (0, size -1 ,2):
    print("index[",i,"]", word[i])


#accept input string from user
word=input("enter the word :")
print("original strings:",word)
#using list slicing
#convert string to list
#pick only even index char
x= list(word)
for i in x[0::2]:
    print(i)

#Write a program to remove characters from a string starting from zero up to n and return a new string.
def remove_char(word,n):
    print("original string:",word)
    x = word[n:]
    return x

print("removing char from strings")
print(remove_char("shivkumar",(5)))


#Check if the first and last number of a list is the same
def first_last_same(numbers):
    print("given number list:",numbers)
    first_num=numbers[0]
    last_num=numbers[-1]
    if first_num == last_num :
        return True
    else:
        return False

numbers_x=(10,40,30,60,80)
print("the result is ",first_last_same(numbers_x))

#Display numbers divisible by 5 from a list
num_list=[10, 20, 33, 46, 55]
print("given list :",num_list)
print("divisiable by 5:")
for num in num_list:
    if num%5==0:
        print(num)


#Exercise 7: Return the count of a given substring from a string
str_x ="shiv is a good dev.shiv is writer."
cnt=str_x.count("shiv")
print(cnt)

# p7: question
print("shiv")

