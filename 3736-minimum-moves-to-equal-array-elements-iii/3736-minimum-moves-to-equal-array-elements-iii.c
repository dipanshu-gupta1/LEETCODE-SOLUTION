int minMoves(int* nums, int numsSize) {

    if (numsSize <= 1 ) return 0 ; 
    int max_val = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > max_val) {
            max_val = nums[i];
        }
    }
    int total_moves = 0;
    for (int i = 0; i < numsSize; i++) {
        total_moves += (max_val - nums[i]);
    }
    return total_moves;
}