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

def sort_lines_and_write_to_file(filename, output_sorted_filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        sorted_lines = sorted(lines)
    with open(output_sorted_filename, 'w') as file:
        for line in sorted_lines:
            file.write(line)

# Example usage
input_filename = 'negSeqENCFF168GAN.txt'  # Input file name
output_sorted_filename = 'sorted_negSeqENCFF168GAN.txt'  # Output sorted file name
output_cropped_filename = 'negSeq168GAN.txt'  # Output cropped file name

# Sorting lines and writing to the sorted file
sort_lines_and_write_to_file(input_filename, output_sorted_filename)

# Removing shorter lines and cropping sequences, then writing to the cropped file
sequence_lengths = read_sequence_lengths(input_filename)
optimal_length = 180 #replace with value after runing postive file
print("Optimal Length:", optimal_length)  # Print the optimal length
cropped_sequences = crop_sequences(input_filename, optimal_length)
write_sequences_to_file(cropped_sequences, output_cropped_filename)
