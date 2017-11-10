#include <vector>
#include <string>
#include <iostream>

using namespace std;

class MotifEvent {
	int pos1, pos2;
	string m1, m2;
	float energy;
public:
	MotifEvent() : pos1(0), pos2(0), m1(""), m2("") {}
	MotifEvent(int p1, string& motif1, int p2, string& motif2) : pos1(p1), pos2(p2), m1(motif1), m2(motif2) {}
	friend ostream& operator<< (ostream& out, MotifEvent& m);
	friend istream& operator>> (istream& in, MotifEvent& m);
	bool checkIfConsistent(MotifEvent& m);
};


class Itemset {
	vector<int> items;
public:
	Itemset() {}
	int first() { return items.front(); }
	int last() { return items.back(); }
	int size() { return items.size(); }
	int getItem(int which) { return items[which]; }
	void insert(int item) { items.insert(items.end(),item); }
	bool checkIfConsistent(vector<MotifEvent>& v, int item);
	friend ostream& operator<< (ostream& out, Itemset& m);
	friend istream& operator>> (istream& in, Itemset& m);
};
