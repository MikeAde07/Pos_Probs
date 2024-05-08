import sys


# Define the hypothese and their priors
hypotheses = {
    'h1' : 0.1,
    'h2' : 0.2,
    'h3' : 0.4,
    'h4' : 0.2,
    'h5' : 0.1
}

# Define probabilities for each hypothesis

transition_probs = {
    'h1':{'C':1.0, 'L':0.0},
    'h2':{'C':0.75, 'L':0.25},
    'h3':{'C':0.5, 'L':0.5},
    'h4':{'C':0.25, 'L':0.75},
    'h5':{'C':0.0, 'L':1.0}
}

# Function to compute posterior probabilities and probabilites of next observation
def compute_posterior(observations):
    counts = {hypothesis: 0 for hypothesis in hypotheses}
    next_probs = {'C':0, 'L':0}
    total_count = 0

    for observation in observations:
        total_count +=1
        for hypothesis in hypotheses:
            counts[hypothesis] *= transition_probs[hypothesis][observation]
            counts[hypothesis] += hypotheses[hypothesis]
        next_probs[observation] += 1

    for hypothesis in counts:
        counts[hypothesis] /= total_count
        next_probs['C'] /= total_count
        next_probs['L'] /= total_count

    return counts, next_probs

# Function to write results to a file
def write_results(observations, posterior, next_probs):
    with open("result.txt", "w") as file:
        file.write(f"Observation sequence Q: {observations}\n")
        file.write(f"Length of Q: {len(observations)}\n\n")

        for i, observation in enumerate(observations):
            file.write(f"After Observation {i+1} = {observation}:\n")
            for hypothesis, probability in posterior.items():
                file.write(f"P({hypothesis} | Q) = {probability:.5f}\n")
            file.write(f"\nProbability that the next candy will pick will be C, given Q: {next_probs['C']:.5f}\n")
            file.write(f"Probability that the next candy we pick will be L, given Q: {next_probs['L']:.5f}\n\n")

# main function
def main():
    if len(sys.argv) !=2:
        observations = ""
    else: 
        observations = sys.argv[1]

    posterior, next_probs = compute_posterior(observations)
    write_results(observations, posterior, next_probs)


if __name__ == "__main__":
    main()
