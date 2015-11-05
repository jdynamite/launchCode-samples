#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
 
int main()
{
    int lightX; // the X position of the light of power
    int lightY; // the Y position of the light of power
    int initialTX; // Thor's starting X position
    int initialTY; // Thor's starting Y position
    int thorX, thorY;
    cin >> lightX >> lightY >> initialTX >> initialTY; cin.ignore();

    // game loop
    
    thorX = initialTX;
    thorY = initialTY;
    
    while (1) {
        
        string directionX, directionY;
        
       if (thorX > lightX ) {
           directionX = "W";
           thorX = thorX - 1;
       }
       else if (thorX < lightX) {
           directionX = "E";
           thorX = thorX +1;
       }
       
       if (thorY > lightY) {
           directionY = "N";
           thorY = thorY - 1;
       }
       
       if (thorY < lightY) {
           directionY = "S";
           thorY = thorY + 1;
       }

        int remainingTurns;
        cin >> remainingTurns; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;

        cout << (directionY+directionX) << endl; // A single line providing the move to be made: N NE E SE S SW W or NW
    }
}