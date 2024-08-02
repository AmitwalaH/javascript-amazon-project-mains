// Debug Ex-> of array
// Q.1
//  #include<iostream>
//  using namespace std;

// int main(){
//     int n, sum = 0;
//     cin >> n;
//     int input[n];
//     for(int i=0;i<n;i++){
//         cin >> input[i];
//     }
//      for(int i=0; i<n; i++){
//          sum = sum + input[i];
//      }
//     cout << sum << endl;
//     return 0;
// }

// Q.2
//  #include<iostream>
//  using namespace std;

// int linearSearch(int arr[], int n ,int val){
//     for(int i=0;i<n;i++){
//         if(arr[i]==val){
//             return true;
//         }
//     }
//    return false;
// }

// int main(){

//     int n = 7;
//     int val = 5;
//     int arr[n];
//         for(int i=0;i<n;i++){
//         cin >> arr[i];
//     }
//     int ans = linearSearch(arr,n,val);
//     cout << ans << endl;
//     return 0;
// }

// Q,3
//  #include<iostream>
//  using namespace std;

// void swapAlternate(int arr[],int size){
//     for(int i=0;i<size-1;i=i+2){
//         int temp= 0;
//         temp = arr[i];
//         arr[i] = arr[i+1];
//         arr[i+1] = temp;
//     }
// }

// int main(){

//     int size = 7;
//     int arr[7];

//     for (int i = 0; i < size; i++)
//     {
//         cin >> arr[i];
//     }
//     cout << "Array before swaping alternate " << endl;
//     for (int i = 0; i < size; i++)
//     {
//         cout << arr[i] << " ";
//     }
//     cout<< "Array after swaping alternate " << endl;
//     swapAlternate(arr,size);
//     for (int i = 0; i < size; i++)
//     {
//         cout << arr[i] << " ";
//     }

//     return 0;
// }

// Q.4
//  #include<iostream>
//  using namespace std;

// void kmTomiles(float km){
//     //one miles to one kilometer 1m -> 1.609 km
//     float a = 1.609;
//     float ans = km / a;
//     cout << "Kilometer to Miles: " << ans << endl;
// }

// int main(){

//     float km;
//     cout << "Enter the kilometer:";
//     cin >> km;

//     kmTomiles(km);

//     return 0;
// }

#include <iostream>
#include <vector>
using namespace std;

int removeDuplicates(vector<int> &nums)
{
    vector<int> result = {nums[0]};

    for (int i = 1; i < nums.size(); i++)
    {
        if (nums[i] != result.back())
            result.push_back(nums[i]);
    }

    nums = result;

    return result.size();
}

int main(){

    vector<int> nums = {0,0,1,1,1,2,2,3,3,4};

    int k = removeDuplicates(nums);

    cout << k << endl;

    return 0;
}
