#include <stdio.h>

typedef struct {
    char data[100];
} Block;

int main() {
    Block my_block;
    sprintf(my_block.data, "Hello, World!");

    printf("%s\n", my_block.data);

    return 0;
}
