char** fizzBuzz(int n, int* returnSize) {
    char** res=(char**)malloc(sizeof(char*)*n);
    if(res==NULL){
        *returnSize=0;
        return NULL;
    }
    *returnSize=n;
    for(int i=1;i<=n;i++){
        res[i-1]=(char*)malloc(sizeof(char)*12);
        if(i%3==0&&i%5==0){
            strcpy(res[i-1],"FizzBuzz");
        }else if(i%3==0){
            strcpy(res[i-1],"Fizz");
        }else if(i%5==0){
            strcpy(res[i-1],"Buzz");
        }else{
            sprintf(res[i-1],"%d",i);
        }
    }
    return res;
}