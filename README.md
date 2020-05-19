# Neural Network in CUDA
Implementing a fully-connected neural network to recognize the [MNIST handwriting dataset](http://yann.lecun.com/exdb/mnist/) in CUDA.

## How to Compile and Run
To compile, run `make`. This will generate an executable called `nn-cuda`.

To run the program, first download the MNIST dataset by running `python get-mnist.py`. This will save the dataset to the directory `mnist/`.
To run on `openhpc`, run `sbatch ./run.sh`. Otherwise, run `./nn-cuda`.

## Notes
In the `get-mnist.py` script, the `urllib.request` function is not available on `openhpc`. Use `urllib2`.
