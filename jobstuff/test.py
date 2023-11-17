def solution(src):
    sentence = src.split(" ")
    new_sentence = []
    for word in sentence:
        new_sentence.append(to_camel_case(word))
    return " ".join(new_sentence)


def to_camel_case(src):
    new_src = ""
    i = 0
    while i < len(src):
        if src[i] == "_":
            if i == 0 or i == len(src) - 1 or (i > 0 and src[i-1] == '_') or (i < len(src)-1 and src[i+1] == '_'):
                new_src += "_"
            else:
                new_src += src[i+1].upper()
                i += 1
        else:
            new_src += src[i]
        i += 1
    return new_src

def main():
    src = input()
    print(solution(src))

if __name__ == "__main__":
    main()