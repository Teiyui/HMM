import numpy as np

# Transaction Probabilities
p_ss = 0.8
p_sr = 0.2
p_rr = 0.6
p_rs = 0.4
# Transaction Probabilities Matrix
A = np.array([[p_ss, p_rs],
              [p_sr, p_rr]])

# Initial Probabilities
p_s = 2 / 3
p_r = 1 / 3
# Initial Probabilities Matrix
pi = np.array([[p_s, p_r]])

# Emission Probabilities (bad and happy)
p_hs = 0.8
p_bs = 0.2
p_hr = 0.4
p_br = 0.6
# Emission Probabilities Matrix
B = np.array([[p_hs, p_bs],
              [p_hr, p_br]])

# Observation sequence(the moods of human)
moods = ['B', 'H', 'H', 'B', 'B', 'H']
# Observation key-value
pair_observation = {'H': 0, 'B': 1}


# backward algorithm according to matrix calculation
def backward(backward_probability, observation):
    # The backward_probability of every step
    current_probability = (np.dot(A * np.array(backward_probability).T, B[:, observation])).tolist()
    return current_probability


# Calculate the sum probability
def sum_probability(backward_probability, observation):
    total = np.dot(pi*np.array(backward_probability).T, B[:, observation])
    return np.squeeze(total)


# Model
def model(moods):
    moods = moods[::-1]
    size = len(moods)
    backward_probability = np.ones(shape=pi.shape[1]).tolist()
    probability_list = []
    for i in range(size - 1):
        observation = pair_observation[moods[i]]
        backward_probability = backward(backward_probability, observation)
        probability_list.append(backward_probability)
    # Calculate the total probability
    total = sum_probability(backward_probability, pair_observation[moods[-1]])
    return probability_list, total


pl, total = model(moods)
print(total)
