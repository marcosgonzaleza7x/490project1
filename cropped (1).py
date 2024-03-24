def read_sequence_lengths(filename):
    with open(filename, 'r') as file:
        lengths = [len(line.strip()) for line in file]
    return lengths

def find_optimal_length(lengths):
    sorted_lengths = sorted(lengths)
    median_index = len(lengths) // 2
    return sorted_lengths[median_index]

def crop_sequences(filename, optimal_length):
    cropped_sequences = []
    with open(filename, 'r') as file:
        for line in file:
            sequence = line.strip()
            if len(sequence) >= optimal_length:
                cropped_sequences.append(sequence[:optimal_length])
    return cropped_sequences

def write_sequences_to_file(sequences, output_filename):
    with open(output_filename, 'w') as file:
        for sequence in sequences:
            file.write(sequence + '\n')

# Example usage
output_filename = 'negSeqENCFF168GAN.txt'  #output file name
filename = 'seqNeg168GAN.txt'  # input file name
sequence_lengths = read_sequence_lengths(filename)
optimal_length = find_optimal_length(sequence_lengths)
cropped_sequences = crop_sequences(filename, optimal_length)
write_sequences_to_file(cropped_sequences, output_filename)