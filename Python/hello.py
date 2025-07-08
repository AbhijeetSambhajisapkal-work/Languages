"""
basics print and functions
input : accepts string
print : sep-> seperator for print arguments , end-> /n ends with a new line 
string : methods : strip,capitalize,title
"""

def print_captilize_strip_usingfunction():
    name = input(" what's your name? "); # variable
    name = name.strip().capitalize().title();
    print(f"Your name is {name}"); # print function use

def print_captilize_strip_using_ascii_values():
    name = input(" what's your name? "); # variable
    name = name.strip();
    namearray = list(name);
    print(namearray);
    for i in range(len(namearray)):
        if(i == 0):
            if(ord(name[i]) in range(97, 123)):
                namearray[i] = chr(ord(namearray[i])-32);
        if((i!= len(namearray)-1) and (namearray[i]== " ")):
             if(ord(name[i+1]) in range(97, 123)):
                namearray[i+1] = chr(ord(namearray[i+1])- 32);
    name_str = ''.join(namearray)  # Convert list to string
    print(f"Your name is {name_str}")

def main():
    print_captilize_strip_usingfunction()
    print_captilize_strip_using_ascii_values()

if __name__ == "__main__":
    main()