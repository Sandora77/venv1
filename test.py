class User:
    name = "default"
    age = 0

    def __int__(self, out_name, out_age):
        self.name = out_name
        self.age = out_age

    def say(self):
        if self.age >=  18:
            print(f"Hello my name is {self.name}. My age is {self.age}")
        else:
             pf"Bye bye {self.name}. You so young!"

user1 = User()
user2 = User()
user3 = User()

user1.say()
user2.say()
user3.say()



def name_function(name, age):
    if age >=  18:
        return f"Hello {name}"
    else:
        return f"Bye bye {name}. You so young!"


#result = name_function("isip18", 189)
#print(result.upper())
#name_functio("liza", 18)
#name_functio("daler", 15)