// Singly-linked lists are already defined with this interface:
// template<typename T>
// struct ListNode {
//   ListNode(const T &v) : value(v), next(nullptr) {}
//   T value;
//   ListNode *next;
// };
//
bool isListPalindrome(std::string inputString) {
    int n = inputString.length();
    for(int i=0; i<n; i++){
        if(inputString[i] != inputString[n-1])
            return false;
        else n--;
    } return true;
}