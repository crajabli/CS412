"""
    name:  Chingiz Rajabli

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
            - I used this stack overflow answer as an example 
              https://stackoverflow.com/q/19798480
  
           Comments here on your code and submission.
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    foxSounds = input().split()
    num = int(input())
    animals = []
    sounds = []

    for i in range(num):
        animalSound = input().split()
        animals.append((animalSound[0], animalSound[2]))

    # filter out the foxSounds using the animals tuple list
    sounds = filter(lambda x: x[1] not in animals, foxSounds)
    sounds = list(sounds)
    print(sounds)

    # for animal in animals:
    #     if animal[1] in foxSounds:
    #         foxSounds.remove(animal[1])

    

    print(animals)
    # print("%s \n %d" % (foxSounds, num))
    pass

if __name__ == "__main__":
    main()  