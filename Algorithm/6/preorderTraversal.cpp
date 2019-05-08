#include <iostream>
#include <cassert>
#include <stack>
#include <string>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 递归
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        if(root){
            v.push_back(root->val);
            preorderTraversal(root->left);
            preorderTraversal(root->right);
        }
        return v;
    }
private:
    vector<int> v;
};

// 非递归，模拟系统栈
struct Command{
    string s; // go, print
    TreeNode* node;
    Command(string s, TreeNode* node): s(s), node(node){}
};

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        if(root == NULL)
            return res;

        stack<Command> stack;
        stack.push(Command("go", root));
        while(!stack.empty()){
            Command command = stack.top();
            stack.pop();

            if(command.s == "print")
                res.push_back(command.node->val);
            else{
                assert(command.s == "go");
                if(command.node->right)
                    stack.push(Command("go", command.node->right));
                if(command.node->left)
                    stack.push(Command("go", command.node->left));
                stack.push(Command("print", command.node));
            }
        }
        return res;
    }
};

int main() {

    return 0;
}
