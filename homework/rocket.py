# Rocket Sections
# In order to identify budding rocket science talent, SpaceX has designed a new modular build-your-own rocket kit for amateur rocketeers to use to construct model rockets. After careful user-studies, SpaceX has found that its customers want to be able to build rockets of widely varying height. Thus, they've arrived at the following idea. Instead of selling rocket fuselage tubing at every height desired by their customers, they'll offer an array of rocket "sections" at varying heights that can be fit together to form a full sized rocket. For example, for the Lil Falcons parts (their entry level kit for preschoolers, that comes complete with a mix your own rocket fuel kit and size 3T smocks) they offer rocket sections in the following sizes: 1 inch, 2 inch  5 inch, and 7 inch sections.

# In order to build a rocket of height 15, a kinderscientist could use two 5" sections, two 2" sections, and one 1" section for a total of five sections. Or three 5" sections for a total of three sections. Obviously, construction is made more complicated by the number of sections that need to be arc welded together (there's a companion Kids-Do-Welding TM starter kit made by Hasbro for the preschooler who hasn't gotten started welding yet). The goal of any good rocket designer is to minimize the number of sections used in the construction of their rocket. 

 

# Input
# The input to the program will be a line containing a space separated, sorted list of the n lengths of available rocket sections for a given kit. The second line will be a single integer representing the length of rocket the user wants to construct. The first line will always include a part of length 1, meaning that all requested lengths can be constructed.

 

# Output
# For partial credit you can simply output a single line reporting the minimum total number of rocket sections needed to construct the rocket in the format "N rocket sections minimum\n". 

# # For full credit the output should have n+1 lines. The first n lines should detail how many of each rocket length the designer needs to buy. Each should be of the form "X of length Y" detailing how many (X) rocket sections of length value Y should be bought. The final line should report the total number of rocket sections in the format "N rocket sections minimum". 
# Sample Partial Credit Input/Output
# Sample Input	Sample Output
# 1 2 5 7
# 15
# 3 rocket sections minimum
 

# Sample Input	Sample Output
# 1 2 3 5 7 14
# 15
# 2 rocket sections minimum
 

# Sample Input	Sample Output
# 1 9 
# 17
# 9 rocket sections minimum
 

# Sample Input	Sample Output
# 1 9 10 
# 18
# 2 rocket sections minimum
 

# Sample Input	Sample Output
# 1 9 10 90 100 
# 198
# 4 rocket sections minimum
 

# Sample Full Credit Input/Output
# Note that multiple possible output strings may be correct.

# Sample Input	Sample Output
# 1 2 5 7
# 15
# 1 of length 1
# 0 of length 2
# 0 of length 5
# 2 of length 7
# 3 rocket sections minimum
 

# Sample Input	Sample Output
# 1 2 3 5 7 14
# 15
# 1 of length 1
# 0 of length 2
# 0 of length 3
# 0 of length 5
# 0 of length 7
# 1 of length 14
# 2 rocket sections minimum
 

# Sample Input	Sample Output
# 1 9
# 17
# 8 of length 1
# 1 of length 9
# 9 rocket sections minimum
 

# Sample Input	Sample Output
# 1 9 10
# 18
# 0 of length 1
# 2 of length 9
# 0 of length 10
# 2 rocket sections minimum
 

# Sample Input	Sample Output
# 1 9 10 90 100
# 198
# 0 of length 1
# 2 of length 9
# 0 of length 10
# 2 of length 90
# 0 of length 100
# 4 rocket sections minimum
def build_rocket(sections, length, minimum):
    if (length % sections[-1] == 0):
        minimum[-1] = length // sections[-1]
        return minimum
    



def main():
    rocket_section = list(map(int, input().split()))
    length = int(input())
    print(rocket_section)
    print(length)
    minimum = [0] * len(rocket_section)
    print (minimum)
    build_rocket(rocket_section, length, minimum)


if __name__ == '__main__':
    main()