import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    weights = initial_weights
    bias = initial_bias
    mse_values = []
    for i in range(epochs):
        logits = features@(weights.T) + bias
        y_pred = 1/(1+np.exp(-logits))
        mse_values.append(np.mean((y_pred - labels)**2))
        delta = 2 * (y_pred - labels) * y_pred * (1 - y_pred)
        step_size = learning_rate / len(labels)
        weights = weights - step_size*(features.T@delta)
        bias = bias - step_size*delta.sum()
    
    updated_bias = bias
    updated_weights = weights
    return updated_weights, updated_bias, mse_values