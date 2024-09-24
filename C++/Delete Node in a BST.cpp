// Link to the exercise : https://leetcode.com/problems/delete-node-in-a-bst/description/?envType=study-plan-v2&envId=leetcode-75

// INSTRUCTIONS //

// Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

// Basically, the deletion can be divided into two stages:
// Search for a node to remove.
// If the node is found, delete the node.

// EXERCISE //

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (root == nullptr) return root;  

        if (key < root->val) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->val) {
            root->right = deleteNode(root->right, key);
        } else {
            // Case 1: No child or one child (right child or left child is nullptr)
            if (root->left == nullptr) {
                TreeNode* temp = root->right; 
                delete root;
                return temp;
            } else if (root->right == nullptr) {
                TreeNode* temp = root->left; 
                delete root;
                return temp;
            }

            // Case 2: Node with two children
            TreeNode* temp = minValue(root->right);

            root->val = temp->val;
            root->right = deleteNode(root->right, temp->val);
        }

        return root;
    }

    TreeNode* minValue(TreeNode* node) {
        TreeNode* current = node;
        while (current && current->left != nullptr)
            current = current->left;
        return current;
    }
};
