/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (head==NULL)
            return head;
        ListNode* prev = head;
        int pval = head->val;
        ListNode* curr;
        while(prev->next!=NULL){
            curr = prev->next;
            if(curr->next==NULL){
                if(prev->val==curr->val)
                    prev->next=NULL;
                break;
            }
            if (prev->val==curr->val){
                while(curr->val==prev->val){
                    if(curr->next == NULL){
                        prev->next = NULL;
                        break;
                    }
                    prev->next = curr->next;
                    curr = curr->next;
                }
            }
            prev = curr;
        }
        
        return head;
        
        
    }
};