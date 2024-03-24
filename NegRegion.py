def parse_bed_file(bed_file):
    regions = []
    with open(bed_file, 'r') as f:
        for line in f:
            chrom, start, end, *_ = line.strip().split('\t')
            start, end = int(start), int(end)
            regions.append((chrom, start, end))
    return regions

def find_inaccessible_regions(regions):
    inaccessible_regions = []
    for i in range(len(regions) - 1):
        end_current = regions[i][2]
        start_next = regions[i + 1][1]
        if start_next > end_current:
            inaccessible_regions.append((regions[i][0], end_current + 1, start_next - 1))
    return inaccessible_regions

def write_bed_file(regions, output_file):
    with open(output_file, 'w') as f:
        for chrom, start, end in regions:
            if start > end:
                start, end = end, start  # Swap start and end positions
            f.write(f"{chrom}\t{start}\t{end}\n")



def main():
    bed_file = "ENCFF986UZO.bed" 
    output_file = "neg986UZO.bed"

    regions = parse_bed_file(bed_file)
    inaccessible_regions = find_inaccessible_regions(regions)
    write_bed_file(inaccessible_regions, output_file)

if __name__ == "__main__":
    main()
