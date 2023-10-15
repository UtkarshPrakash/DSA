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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int n1=n2=0;
        int mul = 1;
        while(l1!=NULL){
            n1 = n1 + l1->val*mul;
            mul *= 10;
            l1 = l1->next;
        }
        mul = 1;
        while(l2!=NULL){
            n2 = n2 + l2->val*mul;
            mul *= 10;
            l2 = l2->next;
        }
        int res = n1+n2;
        ListNode* ans = new ListNode();
        while(res>0){
            ans->val=res%10;
            res=res/10;
            ListNode* temp=new ListNode(res%10);
            ans->next=temp;
             
        }
    }
    
};