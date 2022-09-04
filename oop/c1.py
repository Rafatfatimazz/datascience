class cat:
    breed=None
    gender=None
    fur_color=None
    age=None
    weight=None
    height=None
    is_tamed=None
    def eat(self,food="cat food"):## food is default parameter
        print(f"😸{food}")
    def play(self):
        print("😸 is playing")   
    def sleep(self):
        print("😸 is sleeping")     
billu=cat()## constructor calling
print(billu,type(billu))
tom=cat()
snowy=cat()
print(tom.breed)## functions in cube and 
billu.breed="persian"
billu.age=2
billu.fur_color="white"
billu.gender="female"
billu.is_tamed=True
billu.weight=2
billu.height=1
tom.breed="street cat"
tom.age=2
tom.fur_color="black"
tom.gender="male"
tom.is_tamed=False
tom.weight=2.5
tom.height=1.5
snowy.breed="american"
snowy.age=2
snowy.fur_color="white"
snowy.gender="female"
snowy.is_tamed=True
snowy.weight=1.5
snowy.height=1
print("billu details")
print("breed",billu.breed)
print("age",billu.age)
print("color",billu.fur_color)
print("weight",billu.weight)
print("height",billu.height)
print("pet",billu.is_tamed)
print("gender",billu.gender)
billu.eat()
billu.play()
billu.sleep()
print("tom details")
print(tom.breed)
print(tom.age)
print(tom.fur_color)
print(tom.gender)
print(tom.is_tamed)
print(tom.weight)
print(tom.height)
tom.eat()
tom.play()
tom.sleep()