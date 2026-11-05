int findTheDistanceValue(int* arr1, int arr1Size, int* arr2, int arr2Size,
                         int d) {
    int count = 0;
    for (int i = 0; i < arr1Size; i++) {
        int flag = 0;
        for (int j = 0; j < arr2Size; j++) {
            int diff = abs(arr1[i] - arr2[j]);
            if (diff <= d) {
                flag = 1;
                break;
            }
        }
        if (flag == 0 )
        count++;
    }
    return count;
}