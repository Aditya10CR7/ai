# Define prior probabilities and likelihoods
p_h = 0.1  # prior probability of condition being present
p_e_given_h = 0.8  # probability of symptom given condition is present
p_e_given_not_h = 0.2  # probability of symptom given condition is not present

# Calculate marginal likelihood of evidence
p_e = p_e_given_h * p_h + p_e_given_not_h * (1 - p_h)

# Calculate posterior probability of condition given evidence
p_h_given_e = p_e_given_h * p_h / p_e

print(f"Probability of condition given symptom: {p_h_given_e:.2f}")