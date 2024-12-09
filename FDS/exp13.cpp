#include <iostream>
using namespace std;

#define MAX 5

int queue[MAX];
int front = -1;
int rear = -1;

bool isFull() {
    return (front == 0 && rear == MAX - 1) || (front == rear + 1);
}

bool isEmpty() {
    return front == -1;
}

void placeOrder(int order) {
    if (isFull()) {
        cout << "Queue full hai, aur orders nahi le sakte." << endl;
    } else {
        if (front == -1) front = 0;
        rear = (rear + 1) % MAX;
        queue[rear] = order;
        cout << "Order " << order << " place ho gaya." << endl;
    }
}

void serveOrder() {
    if (isEmpty()) {
        cout << "Queue khali hai, koi order nahi hai serve karne ke liye." << endl;
    } else {
        cout << "Order " << queue[front] << " serve ho gaya." << endl;
        if (front == rear) {
            front = rear = -1; // Queue is now empty
        } else {
            front = (front + 1) % MAX;
        }
    }
}

void displayOrders() {
    if (isEmpty()) {
        cout << "Queue khali hai." << endl;
    } else {
        cout << "Queue mein orders: ";
        int i = front;
        while (i != rear) {
            cout << queue[i] << " ";
            i = (i + 1) % MAX;
        }
        cout << queue[rear] << endl;
    }
}

int main() {
    int orderNum = 101;

    placeOrder(orderNum++);
    placeOrder(orderNum++);
    placeOrder(orderNum++);
    placeOrder(orderNum++);
    displayOrders();

    serveOrder();
    displayOrders();

    placeOrder(orderNum++);
    placeOrder(orderNum++);
    displayOrders();

    serveOrder();
    displayOrders();

    return 0;
}
