#include "motifEvent.h"
#include <vector>
#include <set>
#include <fstream>

ostream& operator<< (ostream& out, MotifEvent& m) {
	out << m.pos1 << ' ' << m.m1 << ' ' << m.pos2 << ' ' << m.m2 << ' ' << m.energy << endl;
	return out;
}

istream& operator>> (istream& in, MotifEvent& m) {
	string gb;
	in >> m.pos1 >> gb >> m.m1 >> gb >> m.pos2 >> gb >> m.m2 >> gb >> m.energy;
	return in;
}

ostream& operator<< (ostream& out, Itemset& its) {
	for (int i=0; i<its.size(); i++) {
		if (i>0) out << ' ';
		out << its.items[i];
	}
	out << endl;
	return out;
}

istream& operator>> (istream& in, Itemset& its) {
	return in;
}

bool MotifEvent::checkIfConsistent(MotifEvent& m) {
	int s1 = pos1+m1.size();
	int s2 = pos2-m2.size();
	int s3 = m.pos2-m.m2.size();
	bool cond = (m.pos1+m.m1.size() < pos1 || m.pos1 > s1) && (s3 > pos2 || m.pos2 < s2);
	return cond;
}

bool Itemset::checkIfConsistent(vector<MotifEvent>& v, int item) {
	bool cond = true;
	for (int i=0; i<items.size() && cond; i++)
		cond = cond && v[i].checkIfConsistent(v[item]);
	return cond;
}

vector<Itemset> makeItemsets(vector<Itemset>& itemsets, vector<Itemset>& pairs, vector<MotifEvent>& v) {
	vector<Itemset> newItemsets;
	vector<Itemset> finished;
	for (int i=0; i<itemsets.size(); i++) {
		bool extended = false;
		Itemset s1 = itemsets[i];
		for (int j=0; j<pairs.size(); j++) {
			Itemset s2 = pairs[j];
			if (s1.last() == s2.first()) {
				if (s1.checkIfConsistent(v,s2.last())) {
					s1.insert(s2.last());
					newItemsets.insert(newItemsets.end(),s1);
					extended = true;
				}
			}
		}
		if (!extended) finished.insert(finished.end(), s1);
	}
	if (newItemsets.size() > 0) {
		vector<Itemset> extended = makeItemsets(newItemsets, pairs, v);
		finished.insert(finished.end(), extended.begin(), extended.end());
	}
	return finished;
}

void printPath(Itemset& items, vector<MotifEvent>& v) {
	for (int i=0; i<items.size(); i++)
		cout << v[items.getItem(i)];
}

int main (int argc, char * argv[]) {
	vector<MotifEvent> v;
	MotifEvent m;
	vector<Itemset> itemsets;

	ifstream in(argv[1]);
	if (in.fail()) {
		cout << "Cannot open file " << argv[1] << endl;
		return 1;
	}
	while (!in.eof()) {
		in >> m;
		if (in.eof()) break;
		v.insert(v.end(), m);
	}
	in.close();
	for (int i=0; i<v.size()-1; i++) {
		for (int j=i+1; j<v.size(); j++) {
			Itemset s;
			if (v[i].checkIfConsistent(v[j])) {
				s.insert(i);
				s.insert(j);
				itemsets.insert(itemsets.end(),s);
			}
		}
	}
	itemsets = makeItemsets(itemsets, itemsets, v);
	for (int i=0; i<itemsets.size(); i++) {
		cout << "Consistent Path nr " << i << " size " << itemsets[i].size() << endl;
		printPath(itemsets[i], v);
		cout << "***********************" << endl;
	}

	return 0;
}

