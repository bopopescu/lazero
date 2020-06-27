#include <stdio.h>
int main(int argc, char *argv[]){
        for (int i = 0; i < argc; i++)
    {
        printf("%s", argv[i]);
        printf("\n");
    }
}
// xargs allow only registered items in path.