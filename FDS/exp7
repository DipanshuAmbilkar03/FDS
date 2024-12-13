#include<iostream>
using namespace std;

class Node {
    public:
        string name;
        long prn;
        Node* next;
        Node(string n, long p): name(n), prn(p), next(nullptr) {}
};

class Club {
    private:
        Node* head;
        int count;

    public:
        Club(): head(nullptr), count(0) {}

        // Add president
        void addPresident(string name, long prn) {
            Node* newPresident = new Node(name, prn);
            newPresident->next = head;
            head = newPresident;
            count++;
        }
        void addSecretary(string name, long prn) {
            Node* newSecretary = new Node(name, prn);
            if (!head) {
                head = newSecretary;
            } else {
                Node* temp = head;
                while (temp->next != nullptr) {
                    temp = temp->next;
                }
                temp->next = newSecretary;
            }
            count++;
        }
        void addMember(string name, long prn) {
            Node* newMember = new Node(name, prn);
            if (!head) {
                head = newMember;
            } else {
                Node* temp = head;
                while (temp->next != nullptr) {
                    temp = temp->next;
                }
                temp->next = newMember;
            }
            count++;
        }
        void deleteMember(long prn) {
            if (!head) return;

            if (head->prn == prn) {
                Node* temp = head;
                head = head->next;
                delete temp;
                count--;
                return;
            }

            Node* temp = head;
            while (temp->next && temp->next->prn != prn) {
                temp = temp->next;
            }

            if (temp->next) {
                Node* delNode = temp->next;
                temp->next = delNode->next;
                delete delNode;
                count--;
            }
        }
        void display() {
            Node* temp = head;
            while (temp != nullptr) {
                cout << "Name: " << temp->name << ", PRN: " << temp->prn << endl;
                temp = temp->next;
            }
        }
        int totalMembers() {
            return count;
        }
        static void concatenate(Club& a, Club& b) {
            if (!a.head) {
                a.head = b.head;
            } else {
                Node* temp = a.head;
                while (temp->next != nullptr) {
                    temp = temp->next;
                }
                temp->next = b.head;
            }
            a.count += b.count;
        }
};

int main() {
    Club divA, divB;

    divA.addPresident("Amit", 1001);
    divA.addMember("Bhavesh", 1002);
    divA.addSecretary("Chirag", 1003);
    cout << "Division A Members: " << endl;
    divA.display();
    cout << "Total Members in Division A: " << divA.totalMembers() << endl;

    divB.addPresident("Deepak", 2001);
    divB.addMember("Esha", 2002);
    divB.addSecretary("Raju", 2003);
    cout << "Division B Members: " << endl;
    divB.display();

    Club::concatenate(divA, divB);
    cout << "After concatenation: " << endl;
    divA.display();
    cout << "Total Members after concatenation: " << divA.totalMembers() << endl;

    return 0;
}
