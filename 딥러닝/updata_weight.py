def update_weights(model, one_train, one_label, lr):
    for i in range(len(model)):
        inputs=one_train
        if i!=0:
            inputs=[neroun['output'] for neroun in model[i-1]]
        for neuron in model[i]:
            for n in range(len(inputs)):
                neuron['weights'][n] -= lr * neuron['delta'] * inputs[n]
            neuron['weights'][-1] -= lr * neuron['delta']