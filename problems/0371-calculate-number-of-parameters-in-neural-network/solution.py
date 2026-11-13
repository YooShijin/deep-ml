def calculate_parameters(layers: list[dict]) -> int:
    """
    Calculate the total number of trainable parameters in a neural network.

    Args:
        layers: List of dictionaries, each describing a layer.

    Returns:
        Total number of trainable parameters (int).
    """
    total = 0
    for layer in layers:
        if layer['type'] == 'dense':
            total = total + layer['input_size']*layer['output_size']
            if layer.get("bias", True):
                total += layer['output_size']
        else:
            total = total + layer['in_channels']*layer['out_channels']*layer['kernel_size']*layer['kernel_size']
            if layer.get("bias", True):
                total += layer['out_channels']          
    return total