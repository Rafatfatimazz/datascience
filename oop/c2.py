## concept of conductor:used to set the properties of class
class cat:
   def __init__(self,breed,fur_color,gender="f",age="1",weight=1,height=1,is_tamed=True):
    self.breed=breed ## instance variable
    self.fur_color=fur_color
    self.age=age
    self.height=height
    self.is_tamed=is_tamed
    self.gender=gender
    self.weight=weight
   def eat(self,food="catfood"):
    print("cat is eating food{food}")

   def play(self):
    print("cat is playing")

   def sleep(self):
    print("cat is sleeping")

   def info(self):
    print("---"*15)
    print(f"breed:{self.breed}")
    print(f"gender:{self.gender}")
    print(f"height:{self.height}")
    print(f"weight:{self.weight}")
    print(f"fur_color:{self.fur_color}")
    print(f"is_tamed:{self.is_tamed}")
    print(f"age:{self.age}")

## out of the class now
tom=cat("street cat","grey",age=100,gender="F")
snowy=cat("persian","f","white")
print("tom")
tom.info()
tom.eat("jerry")
print("snowy")
snowy.info()
snowy.eat("stuart")    
