#include <iostream>
#include <vector>
using namespace std;

// void mergeTwoSortedArray(int arr[], int brr[], vector<int> &ans, int as, int bs)
// {
//     int i = 0, j = 0;
//     while (i < as && j < bs)
//     {
//         /* code */
//         if (arr[i] < brr[j])
//         {
//             ans.push_back(arr[i]);
//             i++;
//         }
//         else
//         {
//             ans.push_back(brr[j]);
//             j++;
//         }
//     }

//     while (i < as)
//     {
//         /* code */
//         ans.push_back(arr[i]);
//         i++;
//     }

//     while (j < bs)
//     {
//         /* code */
//         ans.push_back(arr[j]);
//         j++;
//     }
// }

void merge(int arr[], int s, int e, int mid)
{
    // create left and right arrays

    int leftLen = mid - s + 1;
    int rightLen = e - mid;

    int *leftArr = new int[leftLen];
    int *rightArr = new int[rightLen];

    // fill or copy the left and right arrays
    // copy original array -> values
    // original array ka starting index
    int index = s;
    // copying into left arr
    for (int i = 0; i < leftLen; i++)
    {
        leftArr[i] = arr[index];
        index++;
    }

    // copying into right arr
    index = mid + 1;

    for (int i = 0; i < rightLen; i++)
    {
        rightArr[i] = arr[index];
        index++;
    }

    // merge logic

    int i = 0;
    int j = 0;
    int mainArrayIndex = s;

    while (i < leftLen && j < rightLen)
    {
        if (leftArr[i] < rightArr[j])
        {
            arr[mainArrayIndex] = leftArr[i];
            i++;
            mainArrayIndex++;
        }
        else
        {
            arr[mainArrayIndex] = rightArr[j];
            j++;
            mainArrayIndex++;
        }
    }

    // i have to handle the 2 cases discoussed above in merge 2 sorted arrays wala question

    while (i < leftLen)
    {
        arr[mainArrayIndex] = leftArr[i];
        i++;
        mainArrayIndex++;
    }

    while (j < rightLen)
    {
        arr[mainArrayIndex] = rightArr[j];
        j++;
        mainArrayIndex++;
    }

    delete[] leftArr;
    delete[] rightArr;
}

void mergeSort(int arr[], int s, int e)
{

    // base case
    if (s >= e)
    {
        return;
    }
    int mid = (s + e) / 2;
    // left part recursion solve karne ke liye
    mergeSort(arr, s, mid);
    // right part recursion solve karne ke liye
    mergeSort(arr, mid + 1, e);
    // dono [parts] ko merge karne ke liye
    merge(arr, s, e, mid);
}

int main()
{

    // int arr[6] = {20, 40, 60, 80, 90, 100};
    // int brr[4] = {10, 30, 50, 70};
    // int as = 6;
    // int bs = 4;
    // vector<int> ans;
    // mergeTwoSortedArray(arr, brr, ans, as, bs);

    // for (int n : ans)
    // {
    //     cout << n << " ";
    // }

    int arr[] = {10,80,110,90,50,30,40,20};
    int size = 8;
    int s = 0;
    int e = size - 1;

    cout << "Before: " << endl;

    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }    
    
    mergeSort(arr,s,e);
    //printing entire arr

    cout <<  endl;

    cout << "After: " << endl;

    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }

    return 0;
    
}