# Aided by OpenAI's ChatGPT and Microsoft's Copilot
import argparse
import pysam
import random
import numpy as np
from tqdm import tqdm
import subprocess
import shutil

def get_vcf_record_count(vcf_file):
    """Try to get the number of records using bcftools index --nrecords."""
    if shutil.which("bcftools") is None:
        return None
    try:
        result = subprocess.run(
            ["bcftools", "index", "--nrecords", vcf_file],
            capture_output=True, text=True, check=True
        )
        return int(result.stdout.strip())
    except subprocess.CalledProcessError:
        return None

def process_vcf(input_vcf, output_vcf, seed=42):
    """Processes a VCF file using pysam, introducing missing genotypes with optional progress tracking.
    Outputs a bgzipped VCF and generates a CSI index."""
    
    assert output_vcf.endswith(".vcf.gz"), "Output file must end with .vcf.gz for bgzip compression"

    random.seed(seed)
    np.random.seed(seed)

    vcf_in = pysam.VariantFile(input_vcf, 'r')
    vcf_out = pysam.VariantFile(output_vcf, 'wz', header=vcf_in.header)

    samples = list(vcf_in.header.samples)
    num_samples = len(samples)
    sample_indices = list(range(num_samples))
    num_missing_samples = int(0.2 * num_samples)
    missing_sample_indices = set(random.sample(sample_indices, num_missing_samples))
    missing_sample_prob = np.random.beta(1, 3, size=num_samples)

    total_variants = get_vcf_record_count(input_vcf)

    variant_iter = tqdm(vcf_in.fetch(), total=total_variants, 
                        desc="Processing", unit=" variants", unit_scale=True)

    for record in variant_iter:
        if random.random() < 0.3:
            missing_snp_prob = np.clip(np.random.beta(0.5, 3) * np.random.uniform(0.8, 1.5), 0, 1)
            for j in missing_sample_indices:
                if random.random() < (missing_snp_prob * missing_sample_prob[j]):
                    record.samples[samples[j]]['GT'] = (None, None)
        vcf_out.write(record)

    vcf_in.close()
    vcf_out.close()

    print("Indexing the output VCF file...")
    pysam.tabix_index(output_vcf, preset="vcf", force=True, csi=True)

    print(f"Modified VCF written to {output_vcf}")
    print(f"CSI index written to {output_vcf}.csi")

def main():
    """Parses command-line arguments and runs the VCF processing function."""
    parser = argparse.ArgumentParser(description="Introduce random missing genotypes in a VCF file.")
    parser.add_argument("-i", "--input", required=True, help="Input VCF file (.vcf or .vcf.gz)")
    parser.add_argument("-o", "--output", required=True, help="Output VCF file (.vcf.gz required)")
    parser.add_argument("-s", "--seed", type=int, default=42, help="Random seed (default: 42)")

    args = parser.parse_args()
    process_vcf(args.input, args.output, args.seed)

if __name__ == "__main__":
    main()
