weight = 0.5
goal_pred = 0.8
input = 2
alpha = 0.1
iterations = 20

for iteration in range(iterations):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    derivative = input * (pred - goal_pred)
    weight = weight - (alpha * derivative)
    
    print("Error:" + str(error) + " Prediction:" + str(pred))