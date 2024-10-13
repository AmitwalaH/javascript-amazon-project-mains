#include <iostream>
#include <algorithm>
using namespace std;

class Heap
{
public:
    int *arr;
    int index;
    int capacity;

    Heap(int n)
    {
        this->capacity = n;
        this->arr = new int[n]; // +1 to handle 1-based indexing
        this->index = 0;
    }

    void print()
    {
        for (int i = 1; i <= index; i++) // Print from 1 to index
        {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    void insertInHeap(int val)
    {
        if (index == capacity - 1)
        {
            cout << "Overflow" << endl;
            return;
        }

        index++;
        arr[index] = val;

        int i = index;

        while (i > 1)
        {
            int parentIndex = i / 2;
            if (arr[parentIndex] < arr[i])
            {
                swap(arr[parentIndex], arr[i]);
                i = parentIndex;
            }
            else
            {
                break;
            }
        }
    }

    void deleteFromHeap(){
        //Step->1 replace the root node with laast node
        swap(arr[1],arr[index]);
        //step->2 dlete the node
        index--;
        //step->right position HEAPIFY
        // heapify(arr,index,1);
    }

};

    void heapify(int *arr, int n, int currIndex){
        int i = currIndex;
        int leftIndex = 2 * i;
        int rightIndex = 2 * i + 1;

        //assumming sabse badi value i par hi hai
        int largetIndexVal = i;

        //paar left ya right mai bhi ho sakte hai

        //check left tree

        if (leftIndex < n && arr[leftIndex] > arr[largetIndexVal])
        {
            largetIndexVal = leftIndex;
        }

        //check right Tree

        if (rightIndex < n && arr[rightIndex] > arr[largetIndexVal])
        {
            //right badi valu mil gayi
            largetIndexVal = rightIndex;
        }
        
        if (largetIndexVal != i)
        {
            //matlab i badi value nai hai
            swap(arr[i],arr[largetIndexVal]);
            i = largetIndexVal;
            //baki recursion sambhal lege
            heapify(arr,n,i);
        }
    }

    void buildHeap(int *arr,int n){
        for (int i = n / 2; i > 0; i--)
        {
            heapify(arr,n,i);
        }
        
    }

    void sortHeap(int *arr,int n){
        int e = n - 1;
        while(e > 1){
            swap(arr[1],arr[e]);
            e--;
            heapify(arr,e+1,1);
            for (int i = 1; i < n; i++)
            {
                cout << arr[i] << " ";
            }
            cout << endl;
        }
    }


int main()
{

    int arr[] = {-1,10,20,30,40,50};

    int n = 6;

    buildHeap(arr,n);

    for (int i = 1; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    
    cout << endl;

    // sortHeap(arr,n);

//     Heap dq(10);

//     dq.insertInHeap(10);
//     dq.insertInHeap(20);
//     dq.insertInHeap(30);
//     dq.insertInHeap(40);

//     dq.print();

//     dq.deleteFromHeap();
//     dq.print();
//     dq.deleteFromHeap();
//     dq.print();

    return 0;
}

