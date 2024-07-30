#include<iostream>
using namespace std;

// int sqrt(int n){
//     int s= 0;
//     int e = n;
//     int ans = 0;
//     int mid = (s+e)/ 2;
//     while (s <= e)
//     {
//         if (mid * mid <= n)
//         {
//             ans = mid;
//             s = mid + 1; // right
//         }
//         else
//         {
//             e = mid - 1;//left
//         }
//         mid = (s+e)/ 2;
//     }
//     return ans;
// }
    int divide(int dividend, int divisor) {
        int s = 0;
        int e = dividend;
        int ans = -1;
        while(s <= e){
            int mid =  s + (e - s) >> 1;
            if(mid * divisor <= dividend){
                ans = mid;
                s = mid + 1; //right
            }
            else{
                e = mid - 1;//left
            }
            mid =  s + (e - s) >> 1;
        }
        return ans;
    }

int main(){
   // int n=63;
    int dividend = 10;
    int divisor = 3;

  //  int answer = sqrt(n);
  int answer = divide(dividend,divisor);

    cout << "Sqrt: " << answer << endl;

    return 0;
}