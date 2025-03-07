import argparse
import gzip
import random
import numpy as np

def process_vcf(input_vcf, output_vcf, seed=42):
    """Processes a VCF file in a memory-efficient way, introducing missing genotypes."""
    random.seed(seed)
    np.random.seed(seed)

    open_func = gzip.open if input_vcf.endswith(".gz") else open
    out_func = gzip.open if output_vcf.endswith(".gz") else open

    with open_func(input_vcf, 'rt') as vcf_in, out_func(output_vcf, 'wt') as vcf_out:
        num_samples = None
        sample_indices = None
        missing_sample_indices = set()

        for line in vcf_in:
            if line.startswith("#"):
                # Write header directly
                vcf_out.write(line)
                if line.startswith("#CHROM"):
                    # Extract number of samples from last header line
                    num_samples = len(line.strip().split("\t")) - 9
                    sample_indices = list(range(num_samples))
                    # Select ~20% of samples for missing data
                    num_missing_samples = int(0.2 * num_samples)
                    missing_sample_indices = set(random.sample(sample_indices, num_missing_samples))
                    missing_sample_prob = np.random.beta(1, 3, size = num_samples)
            else:
                fields = line.strip().split("\t")
                genotypes = fields[9:]

                # Decide if this SNP should have missing data (~30% of SNPs)
                if random.random() < 0.3:
                    # missing_snp_prob = np.random.beta(0.5, 3)
                    missing_snp_prob = np.clip(np.random.beta(0.5, 3) * np.random.uniform(0.8, 1.5), 0, 1)

                    # Modify genotypes for selected samples
                    for j in missing_sample_indices:
                        if random.random() < (missing_snp_prob * missing_sample_prob[j]):
                            genotypes[j] = "./."  # Introduce missing genotype

                # Write modified line
                vcf_out.write("\t".join(fields[:9] + genotypes) + "\n")

    print(f"Modified VCF written to {output_vcf}")

def main():
    """Parses command-line arguments and runs the VCF processing function."""
    parser = argparse.ArgumentParser(description="Introduce random missing genotypes in a VCF file.")
    parser.add_argument("-i", "--input", required=True, help="Input VCF file (can be .vcf or .vcf.gz)")
    parser.add_argument("-o", "--output", required=True, help="Output VCF file (can be .vcf or .vcf.gz)")
    parser.add_argument("-s", "--seed", type=int, default=42, help="Random seed (default: 42)")

    args = parser.parse_args()
    
    process_vcf(args.input, args.output, args.seed)

if __name__ == "__main__":
    main()
