#!/bin/bash
#PBS -A @account
#PBS -q batch
#PBS -l walltime=24:00:00,procs=12,mem=36g
#PBS -j oe

module load singularity/3.11.4

basedir=@base_dir
entrypoint=@entrypoint
samplesheet=${basedir}/input/input.csv
nconfig=${basedir}/nextflow.config
outdir=${basedir}/output

mkdir -p $outdir

nextflow -log $outdir run $entrypoint -profile singularity -c $nconfig --input $samplesheet --outdir $outdir -w $outdir