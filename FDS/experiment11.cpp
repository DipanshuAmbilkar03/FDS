#include <iostream>
using namespace std;

#define MAX 5

class JobQueue {
    int queue[MAX];
    int front, rear;

public:
    JobQueue() {
        front = -1;
        rear = -1;
    }

    void kaamAddKaro(int job) {
        if (rear == MAX - 1) {
            cout << "Queue full hai." << endl;
        } else {
            if (front == -1) front = 0;
            rear++;
            queue[rear] = job;
            cout << "Kaam " << job << " queue mein add hua." << endl;
        }
    }

    void kaamRemoveKaro() {
        if (front == -1 || front > rear) {
            cout << "Queue khali hai." << endl;
        } else {
            cout << "Kaam " << queue[front] << " queue se remove hua." << endl;
            front++;
        }
    }

    void queueDikhao() {
        if (front == -1 || front > rear) {
            cout << "Queue khali hai." << endl;
        } else {
            cout << "Current Queue: ";
            for (int i = front; i <= rear; i++) {
                cout << queue[i] << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    JobQueue jq;
    jq.kaamAddKaro(1);
    jq.kaamAddKaro(2);
    jq.kaamAddKaro(3);
    jq.queueDikhao();
    jq.kaamRemoveKaro();
    jq.queueDikhao();
    jq.kaamAddKaro(4);
    jq.queueDikhao();
    
    return 0;
}
