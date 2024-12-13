#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};
void insert(Node*& head, int value) {
    Node* newNode = new Node;  // Create a new node
    newNode->data = value;     
    newNode->next = nullptr;  

    if (!head) {               
        head = newNode;
    } else {
        Node* temp = head;
        while (temp->next) {   // Go to the end of the list
            temp = temp->next;
        }
        temp->next = newNode;  // Attach the new node
    }
}
bool exists(Node* head, int value) {
    Node* temp = head;
    while (temp) {
        if (temp->data == value)
            return true;  
        temp = temp->next;
    }
    return false;  
}
void unionSets(Node* setA, Node* setB) {
    Node* result = nullptr;
    while (setA) {
        insert(result, setA->data);  // Insert all elements from setA
        setA = setA->next;
    }
    while (setB) {
        if (!exists(result, setB->data))  // Insert only new elements from setB
            insert(result, setB->data);
        setB = setB->next;
    }
    cout << "Students who like either vanilla or butterscotch or both: ";
    while (result) {
        cout << result->data << " ";  
        result = result->next;
    }
    cout << endl;
}

void intersectionSets(Node* setA, Node* setB) {
    Node* result = nullptr;
    while (setA) {
        if (exists(setB, setA->data))  // Insert only common elements
            insert(result, setA->data);
        setA = setA->next;
    }
    cout << "Students who like both vanilla and butterscotch: ";
    while (result) {
        cout << result->data << " "; 
        result = result->next;
    }
    cout << endl;
}
void neitherVanillaNorButterscotch(Node* allStudents, Node* setA, Node* setB) {
    int count = 0;
    while (allStudents) {
        if (!exists(setA, allStudents->data) && !exists(setB, allStudents->data))  
            count++;
        allStudents = allStudents->next;
    }
    cout << "Number of students who like neither vanilla nor butterscotch: " << count << endl;
}

int main() {
    Node *setA = nullptr, *setB = nullptr, *allStudents = nullptr;

    insert(setA, 1); insert(setA, 2); insert(setA, 3); 
    insert(setB, 3); insert(setB, 4); insert(setB, 5);
    insert(allStudents, 1); insert(allStudents, 2); insert(allStudents, 3);
    insert(allStudents, 4); insert(allStudents, 5); insert(allStudents, 6);  

    unionSets(setA, setB);
    intersectionSets(setA, setB);
    neitherVanillaNorButterscotch(allStudents, setA, setB);

    return 0;
}
