import neuron as n

dataset = [
    ([0,0], 0),
    ([0,1], 0),
    ([1,0], 0),
    ([1,1], 1)
]

n1 = n.PredictiveNeuron(num_context=2)

n.tools.teachOne(dataset, neuron=n1, rest_ticks=5)

n1.tick([0,0], -1)
v, _ = n.tools.read_neuron(n1)
print(v)
n1.tick([0,1], -1)
v, _ = n.tools.read_neuron(n1)
print(v)
n1.tick([1,0], -1)
v, _ = n.tools.read_neuron(n1)
print(v)
n1.tick([1,1], -1)
v, _ = n.tools.read_neuron(n1)
print(v)