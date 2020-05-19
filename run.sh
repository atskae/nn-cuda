#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --ntasks=1

# Build the program
make

# Run neural network on MNIST data
srun ./nn-cuda

# Clean executable
make clean
