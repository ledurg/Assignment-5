# Program takes input from user as long as user inputs a positive integer
# When a negative integer is put in. The program stops and
# prints the maximum intger the user put in
max_int = 0
num_int = int(input("Input a number: "))

while(num_int > 0):
    if(num_int > max_int):
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)