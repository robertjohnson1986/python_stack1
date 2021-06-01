#1
for x in range (151):
    print(x)

#2
for num in range(5,1001,1):
    if num % 5 == 0:
        print(num)

#3
for num in range(1,101,1):
    if num % 5 == 0:
        print("Coding")
    if num % 10 == 0:
        print("Coding Dojo")
    else:
        print(num)

#4
sum = 0 
for x in range(500001): 
    sum = sum + x 
print (sum)

#5
for x in range(2018,1,-4): 
    print(x)

#6
lowNum=2
highNum=9
mult=3
for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)