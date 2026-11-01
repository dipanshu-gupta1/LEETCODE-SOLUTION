int minMoves(int* nums, int numsSize) {
    if (numsSize <= 1) return 0 ;

    int min_val = nums[0];
    for(int i = 1 ; i < numsSize; i++){
        if (nums[i] < min_val){
            min_val = nums[i];
        }
    }
    long long total_moves = 0 ;
    for (int i = 0 ; i < numsSize ; i++){
        total_moves += (long long)(nums[i] - min_val);
    }
    return (int)(total_moves);
}