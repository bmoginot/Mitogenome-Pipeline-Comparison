import os
import shutil
import subprocess
import sys
import argparse

def get_args(args):
    parser = argparse.ArgumentParser(description="run mtgrasp")
    parser.add_argument("-a", "--acc",
    help="sra accession number",
    required=True)
    parser.add_argument("-o", "--output",
    help="output directory",
    required=True)
    return parser.parse_args(args)

def make_outdir(outdir):
    if os.path.isdir(outdir):
        os.system(f"rm -r {outdir}")
    os.system(f"mkdir {outdir}")
    os.chdir(outdir)
    return

def fastqc(f, r):
    f_in = f"../{f}"
    r_in = f"../{r}"
    try:
        subprocess.run(["fastqc", f_in, r_in], check=True)
    except subprocess.CalledProcessError as e:
        print("Error in fastqc:", e)
        exit(1)
    return

def fastp(f, r):
    f_in = f"../{f}"
    r_in = f"../{r}"
    f_out = f"out.{f}"
    r_out = f"out.{r}"
    try:
        subprocess.run(["fastp", "-i", f_in, "-I", r_in, "-o", f_out, "-O", r_out, "-Q"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error in fastp:", e)
        exit(1)
    return f_out, r_out

def mtgrasp():
    pass

def main():
    args = get_args(sys.argv[1:])
    acc, outdir = args.acc, args.output
    f_read = f"{acc}_1.fastq"
    r_read = f"{acc}_2.fastq"
    print(f_read, r_read)

    """make_outdir(outdir)

    fastqc(f_read, r_read)

    f_clean, r_clean = fastp(f_read, r_read)
    
    ref = "/home/bmoginot/mtdna/sequence.fasta"
    threads = 12
    mtgrasp(acc, ref, threads)
    return"""

# python3 pipeline_pipeline.py -a SRR15139196 -o pp_test

if __name__ == "__main__":
    main()