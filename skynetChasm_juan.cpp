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
    string action;
    bool jumped = 0;;
    int road; // the length of the road before the gap.
    cin >> road; cin.ignore();
    int gap; // the length of the gap.
    cin >> gap; cin.ignore();
    int platform; // the length of the landing platform.
    cin >> platform; cin.ignore();

    // game loop
    while (1) {
        int speed; // the motorbike's speed.
        cin >> speed; cin.ignore();
        int coordX; // the position on the road of the motorbike.
        cin >> coordX; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;

        // road <- road length
        // platform <- landing platform length
        // gap <- gapLength
        
        
        bool doom = coordX+speed >= road+1; // are we doomed on the next step?
        
        if (!jumped){
            if (gap+1 > speed) {
                action = "SPEED";
            }
            else if (speed > gap+1) {
                action = "SLOW";
            }
            else if (doom) {
                action = "JUMP";
                jumped = 1;
            }
            else action = "WAIT";
        }
        else action = "SLOW";
        

        cout << action << endl; // A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    }
}