from art import *
import os


classification = [0, 0 , 0, 1]

inputs = [
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1),
]


def activationFunction(output: float):
    if(output >= 0): 
        return 1
    return 0

def training(w1: float, w2: float, n:float, b:float):
    
    for x1, x2 in inputs:
        print(type(x1))
        print(type(x2))
        print(f"y = {x1}.{w1} + {x2}.{w2} + {b}")

        y = (float(x1) * w1) + (float(x2) * w2) + b
        print(y)
        
        error = classification[0] - activationFunction(y)
        print(error)

        if not (error == 0 ):
            print("classification failt: update the weights...");

        
    


def main():
    os.system('clear || cls')
    tprint("Pyneural")
    print("by Ryan Oliveira\n")


    print("[*] Perceptron to resolve END Gate")
    
    print("[*] Provide the following weights: ")

    weight_1 = float(input("[?] w1: "))
    weitht_2 = float(input("[?] w2: "))

    print("[*] Provide the Learning rate: ")
    learning_rate = float(input("[?] n: "))

    print("[*] Provide the bias: ")
    bias = float(input("[?] b: "))

    training(weight_1, weitht_2, learning_rate, bias)




if(__name__ == "__main__"):
    main()