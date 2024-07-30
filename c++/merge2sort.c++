#include <iostream>
#include <vector>
using namespace std;

void mergeTwoSortedArray(int arr[], int brr[], int ans[], int as, int bs)
{
    int i = 0, j = 0, k = 0;
    while (i < as && j < bs)
    {
        /* code */
        if (arr[i] < brr[j])
        {
            ans[k] = arr[i];
            k++;
            i++;
        }
        else
        {
            ans[k] = brr[j];
            k++;
            j++;
        }
    }

    while (i < as)
    {
        ans[k] = arr[i];
        k++;
        i++;
    }

    while (j < bs)
    {
        ans[k] = brr[j];
        k++;
        j++;
    }
}

int main()
{

    int arr[6] = {20, 40, 60, 80, 90, 100};
    int brr[4] = {10, 30, 50, 70};
    int as = 6;
    int bs = 4;
    int ans[10];
    mergeTwoSortedArray(arr, brr, ans, as, bs);

    for (int n : ans)
    {
        cout << n << " ";
    }
}