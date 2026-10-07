# Predictive coding neurons
## What is predictive coding?
Predictive coding is the theory of brain function which states that neurons are 
constantly updating a mental model. The mental model is used to predict input 
signals from the senses that are then compared to the inputs. This is different
from standard neural networks as there is no back propogation, and learning is
a constant process. 
## Why use it for Neural Networks?
There are many benefits to PC neurons, versus the standard model. In the standard 
model, inputs are calculated through every layer to reach an output. With PC, the
input values only go to the next layer if the current layer's neurons fail to 
predict. Given it only computes the minimum it needs it, it uses less computational 
power. Another benefit comes from it's ability to constantly learn. While it is
possible to inhibit learning, its default state is to constantly predict new inputs
and adjust it's weights if it hasn't been encountered before. 
## What issues are there?
Because one of it's main benefits is it's ability to constantly learn, you cannot
simply remove inputs for prediction. Instead the solution I am testing is to have
each neuron trigger a decaying flag, similar to a trace, telling a program designed 
to read those signals when that neuron had last spiked, functioning almost as an
FMRI.