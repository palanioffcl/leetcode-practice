#include <stdio.h>


int main() {
    int a[10][10] = {{1,2},{3,4},{5,6},{7,8},{9,10}};
//printf("%d", *a[3]);    
int *p = a[3];
    int result = (*p + 2) * a[4][1] + (++*p) + (*p + 7);
    printf("%d", result);
    return 0;
}main()
{
    int i=0;
    for(i=0; i<20; i++)
    {
        switch(i)
        {
            case 0: i+=5;
            case 1: i+=2;
            case 5: i+=5;
            default: i+=4;
                     break;
        }
        printf("%d", i);
    }
}