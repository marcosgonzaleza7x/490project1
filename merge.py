def zipper_merge(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'a') as out:
        for line1, line2 in zip(f1, f2):
            out.write(f"0 {line1.strip()}\n")  # Label 0 for negative
            out.write(f"1 {line2.strip()}\n")  # Label 1 for positive

# List of file paths for positive and negative files
positive_files = ["posSeqENCFF050GDF.txt","posSeqENCFF168GAN.txt","posSeqENCFF260PVK.txt","posSeqENCFF275TRN.txt","posSeqENCFF522GCK.txt", 
                  "posSeqENCFF749FDY.txt", "posSeqENCFF769QHG.txt","posSeqENCFF820RAY.txt","posSeqENCFF844TKP.txt","posSeqENCFF986UZO.txt"]
negative_files = ["negSeq050GDF.txt","negSeq168GAN.txt","negSeg260PVK.txt","negSeg275TRN.txt","negSeg522GCK.txt","negSeg749FDY.txt",
                  "negSeg769QHG.txt","negSeg820RAY.txt","negSeg844TKP.txt","negSeg986UZO.txt"]

# Output file path
output_file = "merged_data.txt"

# Merge each pair of positive and negative files
for pos_file, neg_file in zip(positive_files, negative_files):
    zipper_merge(neg_file, pos_file, output_file)
