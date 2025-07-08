def trycatch():
    try : 
        x=int(input("enter number"));
    except ValueError:
        #pass
        print("failed");
    else:
        print(x);

trycatch()

#ValueError
#NameError
#MemoryError
#KeyError
#Exception
