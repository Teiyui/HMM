import numpy as np

# Transaction Probabilities
p_ss = 0.8
p_sr = 0.2
p_rr = 0.6
p_rs = 0.4
# Transaction Probabilities Matrix
A = np.array([[p_ss, p_rs],
              [p_sr, p_rr]])
# A = np.array([[0.5, 0.2, 0.3],
#               [0.3, 0.5, 0.2],
#               [0.2, 0.3, 0.5]])

# Initial Probabilities
p_s = 2 / 3
p_r = 1 / 3
# Initial Probabilities Matrix
pi = np.array([[p_s, p_r]])
# pi = np.array([[0.2, 0.4, 0.4]])

# Emission Probabilities (bad and happy)
p_hs = 0.8
p_bs = 0.2
p_hr = 0.4
p_br = 0.6
# Emission Probabilities Matrix
B = np.array([[p_hs, p_bs],
              [p_hr, p_br]])
# B = np.array([[0.5, 0.5],
#               [0.4, 0.6],
#               [0.7, 0.3]])

# Observation sequence(the moods of human)
moods = ['B', 'H', 'H', 'B', 'B', 'H']
# moods = ['R', 'W', 'R']
# Observation key-value
pair_observation = {'H': 0, 'B': 1}
# pair_observation = {'R': 0, 'W': 1}

# backward algorithm
def backward(backward_probability, observation):
    current_probability = []
    # The backward_probability of every step
    size = len(backward_probability)
    for i in range(size):
        current_probability.append(sum(backward_probability[j] * np.squeeze(A[i, j]) * np.squeeze(B[j, observation])
                                   for j in range(A.shape[0])))
    return current_probability


# Calculate the sum probability
def sum_probability(backward_probability, observation):
    total = 0
    for i in range(len(backward_probability)):
        total += (pi[0][i] * B[i][observation] * backward_probability[i])
    return total


# Model
def model(moods):
    moods = moods[::-1]
    size = len(moods)
    backward_probability = np.ones(shape=pi.shape[1]).tolist()
    probability_list = []
    for i in range(size-1):
        observation = pair_observation[moods[i]]
        backward_probability = backward(backward_probability, observation)
        probability_list.append(backward_probability)
    # Calculate the total probability
    total = sum_probability(backward_probability, pair_observation[moods[-1]])
    return probability_list, total


pl, total = model(moods)
print(total)
