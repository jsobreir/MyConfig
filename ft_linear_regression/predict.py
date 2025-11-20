def predict():
    mileage = float(input("What is the mileage?"))
    theta0 = float(input("What is the theta0?"))
    theta1 = float(input("What is the theta1?"))
    ret = theta0 + theta1 * mileage
    print(ret)
    return ret

if __name__ == "__main__":
    predict()