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


# forward algorithm
def forward(forward_probability, observation):
    current_probability = []
    # The initialization of forward_probability
    if forward_probability is None:
        for i in range(pi.shape[1]):
            current_probability.append(np.squeeze(pi[0, i] * np.squeeze(B[i, observation])))
        return current_probability
    # The forward_probability of every step
    else:
        size = len(forward_probability)
        for j in range(size):
            current_probability.append(sum(forward_probability[i] * np.squeeze(A[i, j]) for i in range(A.shape[0])) *
                                       np.squeeze(B[j, observation]))
        return current_probability


# model
def model(moods):
    size = len(moods)
    forward_probability = None
    probability_list = []
    for i in range(size):
        observation = pair_observation[moods[i]]
        forward_probability = forward(forward_probability, observation)
        probability_list.append(forward_probability)
    return probability_list, sum(forward_probability)


pl, pl_obs = model(moods)
print(pl_obs)
