#gives the end state but changing the second for loop could give it after any number of people
number_of_doors=36
doors=[] #sets up doors as a global variable
#creates the doors and sets them to the initial state
for i in range(0,number_of_doors):
    doors+="c"
#goes through opening and closing the doors
for i in range(0,number_of_doors):
    for n in range(0,number_of_doors,i+1):
        if doors[n]=="c":
            doors[n]="o"
        else:
            doors[n]="c"
doors[0]=""
#removes the 0th door as it isn't in the original question
print(doors)
