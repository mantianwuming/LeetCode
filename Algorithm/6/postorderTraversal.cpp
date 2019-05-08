/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// �ݹ�
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        if(root){
            postorderTraversal(root->left);
            postorderTraversal(root->right);
            v.push_back(root->val);
        }
        return v;
    }
private:
    vector<int> v;
};

// �ǵݹ飬ģ��ϵͳջ
struct Command{
    string s; // go, print
    TreeNode* node;
    Command(string s, TreeNode* node): s(s), node(node){}
};

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
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
                stack.push(Command("print", command.node));
                if(command.node->right)
                    stack.push(Command("go", command.node->right));
                if(command.node->left)
                    stack.push(Command("go", command.node->left));
            }
        }
        return res;
    }
};

int main() {

    return 0;
}
