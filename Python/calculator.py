import math;

def takeinputs():
    X = int(input("whats the first value? "));
    Y = int(input("whats the second value? "));
    operation = input("type in the operation you want to perform : ['add','sub','divide','mul', 'floor' , 'power','reminder','absolutedivide'] ")
    return operation,X,Y;


def perform_operation(setofopsandinputs):
    if(len(setofopsandinputs)==3):
        operation = setofopsandinputs[0];
        firstnumber = setofopsandinputs[1];
        secondnumber = setofopsandinputs[2]
        if(operation == "add"):
            return firstnumber+secondnumber;
        elif(operation == "sub"):
            return secondnumber-firstnumber;
        elif(operation == "divide"):
            return secondnumber/firstnumber;
        elif(operation == "mul"):
            return firstnumber*secondnumber;
        elif(operation == "power"):
            return firstnumber**secondnumber;
        elif(operation == "floor"):
            return math.floor(firstnumber) + math.floor(secondnumber);
        elif(operation == "ceil"):
            return math.ceil(firstnumber) + math.ceil(secondnumber);
        elif(operation == "reminder"):
            return (secondnumber)%(firstnumber);
        elif(operation=="absolutedivide"):
            return (secondnumber)//(firstnumber);

def main():
    result = perform_operation(takeinputs());
    print(result)

if __name__ == "__main__":
    main()