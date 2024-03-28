def read_sequence_lengths(filename):
    with open(filename, 'r') as file:
        lengths = [len(line.strip()) for line in file]
    return lengths

def crop_sequences(filename, optimal_length):
    cropped_sequences = []
    with open(filename, 'r') as file:
        for line in file:
            sequence = line.strip()
            if len(sequence) >= optimal_length:
                cropped_sequences.append(sequence[:optimal_length])
    return cropped_sequences

def find_optimal_length(lengths):
    sorted_lengths = sorted(lengths)
    num_sequences = len(sorted_lengths)
    if num_sequences % 2 == 0:
        median_length = (sorted_lengths[num_sequences // 2 - 1] + sorted_lengths[num_sequences // 2]) / 2
    else:
        median_length = sorted_lengths[num_sequences // 2]
    return median_length

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
