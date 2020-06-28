import time
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    time.sleep(1)
    print("There's a giant bear here eating a cheese cake.")
    time.sleep(2)
    print("What do you do?")
    time.sleep(2)
    print("1.Take the cake.")
    time.sleep(2)
    print("2.Scream at the bear.")
    time.sleep(5)
    
    bear = input(">")
    
    if bear == "1":
        print("The bear eats your face off.Good job!")
    elif bear == "2":
        print("The bear eats your legs off.Good job!")
    else:
        print(f"Well,doing{bear} is probably better.")
        print("Bear runs away.")
        
elif door == "2":
    time.sleep(1)
    print("You stare into the endless abyss at Cthulhu's retina.")
    time.sleep(2)
    print("1.Blueberries.")
    time.sleep(2)
    print("2.Yellow jacket clothespins.")
    time.sleep(2)
    print("3.Understanding revolvers yelling melodies")
    time.sleep(5)
    
    insanity = input(">")
    
    if insanity == "1" or insanity == "2":
        time.sleep(2)
        print("Your body survives powered by a mind of jello.")
        time.sleep(2)
        print("Good job!")
    else:
        time.sleep(2)
        print("The insanity rots your eyes into a pool of muck.")
        time.sleep(2)
        print("Good job!")
        
else:
    print("You stumble around and fall on a knife and die.Good job!")
        
        
        
        
        
        
        
        
        
        
        