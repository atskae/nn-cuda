#include <stdio.h>

#include <curand.h>
#include <curand_kernel.h>

__global__ void test() {
    printf("Hello from GPU!\n");
}

int main(int argc, char* argv[]) {

    if(argc < 2) {
        printf("Usage: ./nn-cuda <mnist path>");
        return 1;
    }    

    int bx = 2;
    int by = 2;
    int numBlocks = 1;
    dim3 block(bx, by);
    dim3 grid(numBlocks);

    // launch CUDA kernel 
    test<<<grid, block>>>();

    printf("Hello from CPU!\n");

    return 0;
}
