#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
int main()
{
    int end = 7;
    // game loop
    while (1) {
        int spaceX;
        int spaceY;
        vector<int> mountains;
        vector<int> mSorted;
        string action;
        cin >> spaceX >> spaceY; cin.ignore();
        for (int i = 0; i < 8; i++) {
            int mountainH; // represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
            cin >> mountainH; cin.ignore();
            mountains.push_back(mountainH);
        }
        
        mSorted = mountains;
        sort(mSorted.begin(), mSorted.end());
        
        if (mountains[spaceX] == mSorted[end]) {
            action = "FIRE";
            //--end;
        }
        else action = "HOLD";

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;


        cout << action << endl; // either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
    }
}