import numpy as np
import matplotlib.pyplot as plt

# define parameters
age = np.random.randint(low=6, high=16)
level = 'E'
training_days = np.random.randint(low=1, high=6) # training from 1 to 5 times a week
training_hours = 1.5 # 1.5h per once
competition_interval = 2 # competition once per 2 month
luck = np.random.randint(low=1, high=11) # luck score out of 10

# define simulation function
def simulate_progress(trials):
    progress = np.zeros(trials) # progress matrix for 1 person and trials
    for i in range(trials):
        # simulate progress for each trial
        progress[i] = np.random.normal(loc=0.5+0.01*age+0.1*training_days+0.1*competition_interval+0.05*luck, scale=0.1)
    return progress

# run simulation
trials = 100000
progress = simulate_progress(trials)

# plot histogram of final progress scores
plt.hist(progress, bins=20)
plt.axvline(x=1.6, color='r', linestyle='--', label='Passing Level')
plt.legend()
plt.title('Final Progress Scores')
plt.xlabel('Progress Score')
plt.ylabel('Count')
plt.show()
