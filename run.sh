#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --ntasks=1

if [ $# < 2] # if number of arguments < x
then
    echo "./nn-cuda <mnist path>"
    exit 1
fi

# Build the program
make

MNIST_PATH=$1
echo "MNIST_PATH=$MNIST_PATH"

# Run neural network on MNIST data
srun ./nn-cuda $MNIST_PATH

# Clean executable
make clean
