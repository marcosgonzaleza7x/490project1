def read_sequence_lengths(filename):
    with open(filename, 'r') as file:
        lengths = [len(line.strip()) for line in file]
    return lengths

def crop_sequences(filename, optimal_length):
    cropped_sequences = []
    with open(filename, 'r') as file:
        for line in file:
            sequence = line.strip()
            cropped_sequence = sequence[:optimal_length]  # Crop sequences longer than optimal length
            cropped_sequences.append(cropped_sequence)
    return cropped_sequences

def find_optimal_length(lengths):
    total_length = sum(lengths)
    num_sequences = len(lengths)
    average_length = total_length / num_sequences
    return average_length

def write_sequences_to_file(sequences, output_filename):
    with open(output_filename, 'w') as file:
        for sequence in sequences:
            file.write(sequence + '\n')

# Example usage
input_filename = 'negSeqENCFF260PVK.txt'  # Input file name
output_cropped_filename = 'negSeq260PVK.txt'  # Output cropped file name

# Removing shorter lines and cropping sequences, then writing to the cropped file
sequence_lengths = read_sequence_lengths(input_filename)
optimal_length = 180 # replace with the calculated value after running the positive file
print("Optimal Length:", optimal_length)  # Print the optimal length
cropped_sequences = crop_sequences(input_filename, optimal_length)
write_sequences_to_file(cropped_sequences, output_cropped_filename)

