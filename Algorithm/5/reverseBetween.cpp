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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if(m == n)
            return head;
        ListNode* pre = NULL;
        ListNode* cur = head;
        int i = 1;
        while(i < m && cur != NULL){
            pre = cur;
            cur = cur->next;
            i++;
        }

        ListNode* t1 = pre;
        ListNode* t2 = cur;

        while(i <= n && cur != NULL){
            ListNode* next = cur->next;

            cur->next = pre;
            pre = cur;
            cur = next;
            i++;
        }

        if(m == 1){
            t2->next = cur;
            return pre;
        }

        t1->next = pre;
        t2->next= cur;
        return head;
    }
};
