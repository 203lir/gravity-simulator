// gravity.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <math.h>

static const int numofplanets = 3;

class planet {
	private:
		int mass = 0;
		double position[2] = {};
		double velocity[2] = {};
	public:
		planet(int mass1, double position1[2], double velocity1[2]) {
			mass = mass1;
			position[0] = position1[0];
			position[1] = position1[1];
			velocity[0] = velocity1[0];
			velocity[1] = velocity1[1];
		}
		int returnmass() {
			return mass;
		}
		double* returnposition() {
			return position;
		}
		void recalcvelocity(double positions[numofplanets], int masses[numofplanets]) {
			double force[2] = { 0, 0 };
			for (int i = 0; i < numofplanets; i++) {
				double positionofprocessing[2] = *positions[i];
				double xdistance = positionofprocessing[0] - position[0];
				double ydistance = positionofprocessing[1] - position[1];
				double distancesquared = pow(xdistance, 2) + pow(ydistance, 2);
				double totalgravity = mass * masses[i] / distancesquared;
				double multiplystuffbythis = totalgravity / sqrt(distancesquared);
				double xgravity = multiplystuffbythis * xdistance;
				double ygravity = multiplystuffbythis * ydistance;
			}
			velocity[0] += force[0];
			velocity[1] += force[1];
		}
		void recalcposition() {
			position[0] += velocity[0];
			position[1] += velocity[1];
		}
};

int main() {
    std::cout << "Hello World!\n";
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
