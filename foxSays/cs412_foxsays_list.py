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
    fox_sounds = input().split()
    num = int(input())
    animals = []
    faked_animals = []
   
    for i in range(num):
        animal_sound = input().split()
        animals.append((animal_sound[0], animal_sound[2]))

    # filter out the foxSounds list using the animals tuple list
    sounds = list(filter(lambda sound: all(sound != animal[1] for animal in animals), fox_sounds))
    for sound in fox_sounds:
        for animal in animals:
            if sound == animal[1]:
                faked_animals.append(animal[0])
    # remove duplicates from faked_animals list
    faked_animals = list(dict.fromkeys(faked_animals))
    
    print("what the fox says: %s" % " ".join(sounds))
    print("also heard: %s" % " ".join(faked_animals))
    

if __name__ == "__main__":
    main()  