import os
import shutil
import subprocess
import sys
import argparse

def get_args(args):
    parser = argparse.ArgumentParser(description="run software")
    parser.add_argument("-i", "--in1",
    help="forward read",
    required=True)
    parser.add_argument("-I", "--in2",
    help="reverse read",
    required=True)
    parser.add_argument("-o", "--output",
    help="output directory",
    required=True)
    return parser.parse_args(args)

def make_outdir(outdir):
    if os.path.isdir(outdir):
        shutil.rmtree(outdir)
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

def main():
    args = get_args(sys.argv[1:])
    f_read, r_read, outdir = args.in1, args.in2, args.output

    make_outdir(outdir)

    fastqc(f_read, r_read)

    f_clean, r_clean = fastp(f_read, r_read)
"""
    ref = "/home/bmoginot/mtdna/sequence.fasta"
    threads = 10
    mtgrasp(acc, ref, threads)
    return"""

# python pipeline_pipeline.py -i SRR15139196_1.fastq -I SRR15139196_2.fastq -o pp_test

if __name__ == "__main__":
    main()