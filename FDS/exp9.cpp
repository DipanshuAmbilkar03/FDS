#include <iostream>
#include <stack>
#include <cctype>
#include <string>
using namespace std;

string cleanString(const string& str) {
    string cleaned = "";
    for (char ch : str) {
        if (isalnum(ch)) {
            cleaned += tolower(ch);
        }
    }
    return cleaned;
}

string reverseString(const string& str) {
    stack<char> s;
    string reversed = "";
    for (char ch : str) {
        s.push(ch);
    }
    while (!s.empty()) {
        reversed += s.top();
        s.pop();
    }
    return reversed;
}

bool isPalindrome(const string& str) {
    string cleaned = cleanString(str);
    string reversed = reverseString(cleaned);
    return cleaned == reversed;
}

int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);  // Read the entire line of input

    cout << "Original String: " << input << endl;
    string reversedInput = reverseString(input);
    cout << "Reversed String: " << reversedInput << endl;

    if (isPalindrome(input)) {
        cout << "The string is a palindrome." << endl;
    } else {
        cout << "The string is not a palindrome." << endl;
    }

    return 0;
}
