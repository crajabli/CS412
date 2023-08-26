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

    # filter out the foxSounds list using the animals tuple list
    sounds = list(filter(lambda sound: all(sound != animal[1] for animal in animals), foxSounds))
    animals = list(filter(lambda x: x[1] in foxSounds, animals))
    
    print(sounds)

    print(animals)


    print("what the fox says: %s" % " ".join(sounds))
    print("animals: %s" % " ".join([x[0] for x in animals]))
    pass

if __name__ == "__main__":
    main()  