int compare(const void *a , const void *b ){
    int x = *(const int*)a ;
    int y = *(const int*)b ;
    return (x>y) - (x<y);
}
int minMoves2(int* nums, int numsSize) {
    qsort(nums,numsSize,sizeof(int),compare);
    int median = nums[numsSize/2];
    int count = 0;

    for (int i = 0 ; i < numsSize ; i++){
        count += abs( nums[i]-median);
    }
    return count;
}