

int minimumSumSubarray(int* nums, int numsSize, int l, int r) {
    int min_sum = INT_MAX;

    for (int k = l; k <= r; k++) {
        int window_sum = 0;

        // 1. Build the initial window of size k
        for (int i = 0; i < k; i++) {
            window_sum += nums[i];
        }
        if (window_sum > 0 && window_sum < min_sum) {
            min_sum = window_sum;
        }

        // 2. Slide the window across the rest of the array
        for (int i = k; i < numsSize; i++) {
            window_sum += nums[i] - nums[i - k];
            if (window_sum > 0 && window_sum < min_sum) {
                min_sum = window_sum;
            }
        }
    }

    return (min_sum == INT_MAX) ? -1 : min_sum;
}