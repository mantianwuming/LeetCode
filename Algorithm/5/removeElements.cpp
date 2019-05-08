#include <iostream>

using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        // while(head != NULL && head->val == val){
        //     ListNode* delNode = head;
        //     head = delNode->next;
        //     delete delNode;
        // }
        //
        // if(head == NULL)
        //     return NULL;
        // ListNode* cur = head;
        // while(cur->next != NULL ){
        //     if(cur->next->val == val){
        //         //É¾³ıcur->next
        //         ListNode* delNode = cur->next;
        //         cur->next = delNode->next;
        //         delete delNode;
        //         //delNode->next = NULL;
        //     }
        //     else
        //         cur = cur->next;
        // }
        // return head;

        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;

        ListNode* cur = dummyHead;
        while(cur->next != NULL ){
            if(cur->next->val == val){
                //É¾³ıcur->next
                ListNode* delNode = cur->next;
                cur->next = delNode->next;
                delete delNode;
                //delNode->next = NULL;
            }
            else
                cur = cur->next;
        }

        ListNode* retNode = dummyHead->next;
        delete dummyHead;
        return retNode;
    }
};

int main() {

    return 0;
}
