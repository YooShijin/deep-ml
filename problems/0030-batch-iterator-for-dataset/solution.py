import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    # Your code here
    batch =[]
    for i in range(0,len(X),batch_size):
        X_temp = X[i:i+batch_size]
        temp = []
        temp.append(X_temp.tolist())
        if(y is not None):
            y_temp = y[i:i+batch_size]
            temp.append(y_temp.tolist())
        batch.append(temp)
    return batch