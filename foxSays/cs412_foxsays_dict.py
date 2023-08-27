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
    animals = {}
    sounds = []
    fake_animals = []
   
    for i in range(num):
        animal_sound = input().split()
        animals[animal_sound[2]] = animal_sound[0]

    # filter out the foxSounds list using the animals dictionary
    sounds = list(filter(lambda sound: sound not in animals, fox_sounds))
    animals_uttered = list(filter(lambda animalsound: animalsound in fox_sounds, animals))
    for sound in animals_uttered:
        fake_animals.append(animals[sound])
    
    print("what the fox says: %s" % " ".join(sounds))
    print("animals: %s" % " ".join(fake_animals))


if __name__ == "__main__":
    main()