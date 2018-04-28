class Shark:

    def __init__(self,name,age):
        print("Woooooooosh here comes the constructor")
        self.name = name
        self.age = age

    def swim(self):
        print(f"{self.name} is swimming in the pool")

    def be_awesome(self):
        print(f"{self.name} is awesome and {self.age} years old")

def main():
    sonny = Shark("Sonny",13232)
    sonny.be_awesome()
    shanti = Shark("Shanti",95948)
    shanti.swim()

if __name__ == "__main__":
    main()



