#include <stdio.h>
#include <string.h>
// void concatenate(char p[], char q[]) {
//    int c, d;
//    c = 0;
//    while (p[c] != '\0') {
//       c++;      
//    }
//    d = 0;
//    while (q[d] != '\0') {
//       p[c] = q[d];
//       d++;
//       c++;    
//    }
//    p[c] = '\0';
// }

int writeTemp(char *filename,char *data){
   FILE *fp;
   char a[50];
//    must declare length??? so matrix can be formed?
// I have to choose lucky numbers?
// you have to make it small, or exact.
// printf("hello world");
// concatenate(a,"./");
   strcpy(a,"/dev/shm/");
   // use it here???
   // well ,very delicate shit. but will never gonna work without some global shell emulator.
   // check about 100 running process??
   // timeout will not gonna work?
// //    printf("hello world");
   strcat(a,filename);
// concatenate(a,filename);
//    printf("hello world");
//    printf("%s",a);
   fp = fopen(a, "w+");
//    fprintf(fp, "This is testing for fprintf...\n");
   fputs(data, fp);
   fclose(fp);
   //what the fuck?
}

int main(){
    // printf("hello world");
    char *filename="lazero_console_buffer";
    char *data="sample console data";
    // printf("%s %s", filename, data);
    writeTemp(filename,data);
    return 0;}