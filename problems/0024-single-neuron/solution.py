import math
import numpy as np
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    features = np.asarray(features, dtype=float)
    weights = np.asarray(weights, dtype=float)
    labels = np.asarray(labels)

    logits = features @ weights + bias
    probabilities = 1 / (1 + np.exp(-logits))
    mse = np.mean((probabilities - labels) ** 2)

    return probabilities.tolist(), float(mse)