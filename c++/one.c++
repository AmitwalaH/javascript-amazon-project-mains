// 1.
// #include<iostream>
// using namespace std;

// int main() {
// 	char c;
//     cin>>c;
//     if('a'<=c || c >= 'z'){
//         cout<<0;
//     }
// 	else if('A'<=c || c >= 'Z'){
//         cout<<1;
//     }
//     else{
//         cout<<-1;
//     }
// }

// 2.
//  /*
//  Pattern
//  1
//  23
//  345
//  4567
//  */
//  #include<iostream>
//  using namespace std;

// int main(){
//     int n = 4;
//     int i = 1;
//     while(i<=n){
//         int j = i,count = 1;
//         while(count<=i){
//             cout<<j;
//             j = j + 1;
//             count = count + 1;
//         }
//         cout<<"\n";
//         i = i + 1;
//     }
// }

// #include<iostream>
// #include<vector>
// using namespace std;

// int main(){
//     vector<int> v(5,5);
//     int s = v.size();
//     cout << "Vector Array: " << endl;
//     for (int i = 0; i < s; i++)
//     {
//         cout << v[i] << " ";
//     }
//     v.push_back(6);

//     cout << "Vector Array: " << endl;
//     for (int i = 0; i < v.size(); i++)
//     {
//         cout << v[i] << " ";
//     }

//     return 0;

// }

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// const int ROWS = 3;
// const int COLS = 4;

// int search(vector<int>& nums, int target) {
//     int s = 0;
//     int n = nums.size();
//     int e = n - 1;
//     int mid = (e+s) / 2;
//     while (s <= e)
//     {
//         if (nums[mid] == target)
//         {
//             return mid;
//         }
//         if (nums[mid] < target)
//         {
//             s = mid + 1;
//         }
//         if (nums[mid] > target)
//         {
//             e = mid - 1;
//         }
//         mid = (e + s) / 2;
//     }

// }

int *insertX(int arr[], int &n, int x, int pos)
{
    int i;
    n++;
    for (i = n; i >= pos; i--)
        arr[i] = arr[i - 1];

    // insert x at pos
    arr[pos - 1] = x;

    return arr;
}

int main()
{

    int arr[6] = {1, 2, 6, 4, 9, 5};
    int n = 6;
    int x, pos;
    x = 50;
    pos = 3;

    insertX(arr, n, x, pos);

    for(int x : arr){
        cout << x << " ";
    }

    // int arr[ROWS][COLS];

    // // Filling the 2D array with a specific value
    // int value = 5;
    // for (int i = 0; i < ROWS; i++) {
    //     fill(arr[i], arr[i] + COLS, value);
    // }

    // // Printing the 2D array
    // cout << "2D Array filled with value " << value << ":" << endl;
    // for (int i = 0; i < ROWS; i++) {
    //     for (int j = 0; j < COLS; j++) {
    //         cout << arr[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    // cout << "Amit Wala" << endl;
    // int arr[10];
    // cout << arr << " " << &arr << " " << &arr[0] << endl;
    // int n = 5;
    // int a[5][n];

    // for (int i = 0; i < n; i++)
    // {
    //     for (int j =  i + 1; j < n; j++)
    //     {

    //     }

    // }

    return 0;
}
