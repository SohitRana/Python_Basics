## while loop
## the while loop continues to execute as long as the conditional is true.
# count= 0 
# while count<5:      #(lessthan)
#     print(count)
#     count=count+1

# count = 0
# while count%2==0:
#     print(count) 

    #count=count+1   

## loop control statements
## break 
#the break statements exits the loop permaturely


# break statement
# for i in range(15):# range (collection)
#     if i == 10:
#         break
#     print(i)



# continue statement

# the continue statement skips the current iteration and continues with the next.
# for i in range (10):
#     if i % 2 ==0:
#         continue
#     print(i)

#pass statements
## the pass statement is null operations; it does nothing
# for i in range(10):
#      if i == 5:
#          print("the number is",i)
#          pass
#      print(i)

## nested loop 
# the loop is inside a loop
# for i in range(10):
    #  for j in range(5):
    #       print(f"i:{i} and j:{j}")   

# examples
# sum of first 10 natural number
n=10
sum=0
count=1

while count<=n:
     sum =sum+count
     count=count+1
print("sum of first 10 natural is:",sum)

