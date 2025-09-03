# Write your solution here
def anagrams(word1 : str, word2 : str):
    a= sorted(word1)
    b= sorted(word2)
    check= False
    if a==b:
        check=True
    return check

if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False