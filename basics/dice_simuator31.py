from random import randint ## randint is function which pics a no itself between range
win_count=0
lose_count=0
dice=["1","2","3","4","5","6"]
while True:
    input("press enter to scroll dice")##input controls the running of program after we press enter in the program
    out=randint(1,6)##pick randomly an  int between 1 to 6 and store it in out
    print(f"dice=>{dice[out-1]}") ## f is format string and gives out-1 index's value so that slectted value must be dispalyed
    if out==6:
        win_count+=1
    elif out==1:
         lose_count+=1
    
    if win_count==3:
        print("you win")
        break
    elif lose_count==3:
         print("you loose")
         break    