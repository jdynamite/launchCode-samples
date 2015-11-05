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
    int surfaceN; // the number of points used to draw the surface of Mars.
    cin >> surfaceN; cin.ignore();
    for (int i = 0; i < surfaceN; i++) {
        int landX; // X coordinate of a surface point. (0 to 6999)
        int landY; // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
        cin >> landX >> landY; cin.ignore();
    }

    // game loop
    while (1) {
        int X;
        int Y;
        int hSpeed; // the horizontal speed (in m/s), can be negative.
        int vSpeed; // the vertical speed (in m/s), can be negative.
        int fuel; // the quantity of remaining fuel in liters.
        int rotate; // the rotation angle in degrees (-90 to 90).
        int power; // the thrust power (0 to 4).
        cin >> X >> Y >> hSpeed >> vSpeed >> fuel >> rotate >> power; cin.ignore();
        
        // MARS G -> 3.711 m/s2
        // LAND AT ANGLE 0, <= 40m/s VS and <= 20m/s HS
        // I ONLY CARE ABOUT VS AND THRUST ATM
        
        rotate = 0.00;
        
        if (vSpeed < -40) power = 4;
        else if ((vSpeed > -40)&&(vSpeed < -20)) power = 3;
        else if ((vSpeed > -20)&&(vSpeed < -10)) power = 2;
        else if ((vSpeed > -10)&&(vSpeed < 0)) power = 1;
        else power = 0;
        
        

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;

        cout << rotate << " " << power  << endl; // rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    }
}