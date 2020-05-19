CC=nvcc
CFLAGS=-std=c++11

all: nn-cuda

nn-cuda: main.cu
	$(CC) main.cu $(CFLAGS) -o nn-cuda

clean:
	rm nn-cuda
