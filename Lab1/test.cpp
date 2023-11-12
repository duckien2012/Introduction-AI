#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> arr = {1,6,4,7,2,3,8,5};
    vector<int>temp = arr;
    // for ( int i = 0 ; i<8 ; i++)
    // {
    //     cout << temp[i] << " " ;
    // }
    int cnt = 0;
    int temp1;
    int test = 0;
    for ( int i = 0 ; i < 8 ; i++)
    {
        int temp1 = temp[i];
        for ( int j = 0 ; j< 8 ; j++)
        {
            if (j + 1 != temp[i])//
            {
                arr[i]=j + 1;
                if (arr == temp)
                    test++;
                for ( int i = 0 ; i<8 ; i++)
                    {
                        cout << arr[i] << " " ;
                    }
                cout << endl;
                            cnt ++;
            }
            //continue;
        }

        arr[i] = temp1;
    }
    cout << cnt << "  " << test;
    return 0;
}