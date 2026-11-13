import numpy as np


def digit_network_forward(image, weights, biases):
    """Run an image through a fully connected sigmoid network.

    Returns (output activations rounded to 4 decimals, predicted digit).
    """
    image = np.array(image).flatten()
    logits = image
    for idx, wt in enumerate(weights):
        wt = np.asarray(weights[idx])
        bb = np.asarray(biases[idx])
        logits = logits@wt.T + bb
        logits = 1/(1+np.exp(-logits))
    predicted_digit = int(np.argmax(logits))
    activations = np.round(logits, 4).tolist()
    return activations, predicted_digit
