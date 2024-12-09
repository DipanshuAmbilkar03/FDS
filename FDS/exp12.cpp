#include <iostream>
using namespace std;

#define MAX 5

class Deque {
    int deque[MAX];
    int front, rear;

public:
    Deque() {
        front = -1;
        rear = -1;
    }

    void insertFront(int x) {
        if ((front == 0 && rear == MAX - 1) || (front == rear + 1)) {
            cout << "Deque full hai." << endl;
        } else if (front == -1) {
            front = rear = 0;
            deque[front] = x;
        } else if (front == 0) {
            front = MAX - 1;
            deque[front] = x;
        } else {
            front--;
            deque[front] = x;
        }
    }

    void insertRear(int x) {
        if ((front == 0 && rear == MAX - 1) || (front == rear + 1)) {
            cout << "Deque full hai." << endl;
        } else if (rear == -1) {
            front = rear = 0;
            deque[rear] = x;
        } else if (rear == MAX - 1) {
            rear = 0;
            deque[rear] = x;
        } else {
            rear++;
            deque[rear] = x;
        }
    }

    void deleteFront() {
        if (front == -1) {
            cout << "Deque khali hai." << endl;
        } else if (front == rear) {
            front = rear = -1;
        } else if (front == MAX - 1) {
            front = 0;
        } else {
            front++;
        }
    }

    void deleteRear() {
        if (front == -1) {
            cout << "Deque khali hai." << endl;
        } else if (front == rear) {
            front = rear = -1;
        } else if (rear == 0) {
            rear = MAX - 1;
        } else {
            rear--;
        }
    }

    void display() {
        if (front == -1) {
            cout << "Deque khali hai." << endl;
            return;
        }
        cout << "Deque ke elements: ";
        if (front <= rear) {
            for (int i = front; i <= rear; i++)
                cout << deque[i] << " ";
        } else {
            for (int i = front; i < MAX; i++)
                cout << deque[i] << " ";
            for (int i = 0; i <= rear; i++)
                cout << deque[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    Deque dq;
    dq.insertRear(1);
    dq.insertRear(2);
    dq.insertFront(3);
    dq.display();
    cout<<"{deleting elements in front}"<<endl;
    dq.deleteFront();
    dq.display();
    cout<<"{insert elements in front"<<endl;
    dq.insertFront(4);
    dq.insertRear(5);
    dq.display();
    cout<<"{deleting rear elements}"<<endl;
    dq.deleteRear();
    dq.display();
    cout<<"{deleting front elements}"<<endl;
    dq.deleteFront();
    dq.display();
    return 0;
}
