import numpy as n

#default trigger threshold
DEFAULT_V_THRESH = 2
#how fast the neuron states decay, default -1 per tick
DEFAULT_DECAY = -1
DEFAULT_STDP = 8
DEFAULT_REFRACTORY = 100

class Neuron:
    def __init__(self, num_inputs=0, v_thresh=DEFAULT_V_THRESH, v_decay=DEFAULT_DECAY, stdp=DEFAULT_STDP, max_refractory = DEFAULT_REFRACTORY):
        self.v_mem = 0
        self.v_thresh = v_thresh
        self.out = 0

        self.weights = [0] * num_inputs
        self.traces = [0] * num_inputs

        self.v_decay = v_decay
        self.stdp = stdp
        self.refractory = 0
        self.max_refractory = max_refractory

    def add_input(self, initial_weight=0):
        self.weights.append(initial_weight)
        self.traces.append(0)

    def tick(self, inputs):
        if (self.refractory == 0):
            for i in range(len(inputs)):
                if inputs[i] == 1:
                    self.traces[i] = 15
                elif self.traces[i] > 0:
                    self.traces[i] -= self.v_decay
            charge_in = sum(inputs[i] * self.weights[i] for i in range(len(inputs)))
            self.v_mem += charge_in
            

            if self.v_mem >= self.v_thresh:
                self.out = 1
                self.v_mem = 0
                self.refractory = self.max_refractory
            else:
                self.out = 0
                if self.v_mem > 0:
                    self.v_mem = max(0, self.v_mem + self.v_decay)

        else:
             self.out = 0
             self.refractory -= 1
        return self.out

    def applystdp(self):
        for i in range(len(self.traces)):
            if self.traces[i] >= self.stdp:
                self.weights[i] = min(7, self.weights[i] + 1)
            else:
                self.weights[i] = max(-8, self.weights[i] - 1)
                

    


class PredictiveNeuron:
    def __init__(self, num_context):
        self.error = 0
        self.predictor = Neuron(num_inputs=num_context)

    def tick(self, context, raw_in):
        pred_spike = self.predictor.tick(context)

        self.error = 1 if (raw_in == 1 and pred_spike != 1) else 0
        
        if(self.error == 1):
            self.predictor.applystdp()
        
        return self.error
        