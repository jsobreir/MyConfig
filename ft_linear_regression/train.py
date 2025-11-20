import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys, json

def plot(df: any):
    start = df['km'].min()
    stop = df['km'].max()
    print(start, " ", stop)
    kms = np.arange(start, stop, 10000)
    theta0, theta1 = train(df)
    prices = []
    for km in kms:
        price = estimatePrice(km, theta0, theta1)
        prices.append(price)
    plt.plot(kms, prices, linestyle='-', marker='o', label="Predicted")
    plt.plot(df['km'], df['price'], linestyle='', label="Real")
    plt.xlabel("Distance [km]")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

def estimatePrice(mileage: float, theta0: float, theta1: float):
    return theta0 + theta1 * mileage

def train(df: any):
    m = len(df)
    LR = 0.1
    print(m)
    max = df['km'].max()
    df['km'] = df['km'] / max
    theta0 = theta1 = 0
    for _ in range(1000):
        tmp_theta0 = tmp_theta1 = 0
        for i in range(m):
            err = estimatePrice(df['km'][i], theta0, theta1) - df['price'][i]
            tmp_theta0 += err
            tmp_theta1 += err * df['km'][i]
        theta0 -= (LR / m) * tmp_theta0
        theta1 -= (LR / m) * tmp_theta1
    theta1 /= max
    df['km'] = df['km'] * max
    print("theta0 =", theta0)
    print("theta1 =", theta1)
    return theta0, theta1

if __name__ == "__main__":
    try:
        args = sys.argv
        input = [index for (index, item) in enumerate(args) if item == "-f"]
        output = [index for (index, item) in enumerate(args) if item == "-o"]  
        plot = [index for (index, item) in enumerate(args) if item == "-p"]

        if input:
            input_file = args[input + 1]
        else:
            input_file = "data.csv"
        try:
            df = pd.read_csv(input_file)
        except FileNotFoundError, pd.errors.ParserError as e:
            print("Invalid input file: ", e)
            sys.exit(1)
        
        theta0, theta1 = train(df)
        if output:
            data = {
                "theta0": str(theta0),
                "theta1": str(theta1) 
            }
            try:
                with open(args[output + 1], 'w') as out:
                    json.dump(data, out)
            except
        if plot:
            plot(df)
    
    except InputError:
        