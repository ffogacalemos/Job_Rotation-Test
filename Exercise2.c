#include <stdio.h>
#include <stdlib.h>


//Exercise 2
int chk_fib(int n){
    int i = 0, j = 1;

    while(1){
        if(j == n || i == n)
            return 1;
        if(j>n)
            return 0;


        i=j+i;
        j=i+j;

        //printf("%i %i", i, j );
    }
}

int main(){
    //printf(" %i",chk_fib(22));

}
