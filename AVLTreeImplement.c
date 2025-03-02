#include <stdio.h>
#include <stdlib.h>

struct Node{
    int key;
    struct Node *left, *right;
    int height;
};
struct Node* createNode(int key)
{
    struct Node* newnode = (struct Node*)malloc(sizeof(struct Node));
    newnode->key = key;
    newnode->left = NULL;
    newnode->right = NULL;
    newnode->height = 1;
    return newnode;
}
int getHight(struct Node* node)
 {
    if (node == NULL)
        return 0;
    return node->height;
}
int getBalanceFactor(struct Node* node)
{
    if (node == NULL)
        return 0;
    return getHight(node->left) - getHight(node->right);
}
struct Node* rightRotate(struct Node* y)
{
    struct Node* x = y->left;
    struct Node* T2 = x->right;
    //Perform Rotation 
    x->right = y;
    y->left = T2;
    // Update Heights
    y->height = 1 + (getHight(y->left) > getHight(y->right)) ? getHight(y->left):getHight(y->right);
    x->height = 1 + (getHight(x->left) > getHight(x->right)) ? getHight(x->left):getHight(x->right);
    // Return new root
    return x;
}

struct Node* leftRotate(struct Node* x)
{
    struct Node* y = x->right;
    struct Node* T2 = y->left;
    // Perform Rotation
    y->left = x;
    x->right = T2;
    // Update Heights
    x->height = 1 + (getHight(x->left) > getHight(x->right)) ? getHight(x->left):getHight(x->right);
    y->height = 1 + (getHight(y->left) > getHight(y->right)) ? getHight(y->left):getHight(y->right);
    // Return new root
    return y;
}
struct Node* insertNode(struct Node* node, int key)
{
    if(node == NULL)
        return createNode(key);
    if(key < node->key)
        node->left = insertNode(node->left, key);
        
    else if(key > node->key)
        node->right = insertNode(node->right, key);
        
    else
        return node;
    node->height = 1+ ((getHight(node->left) > getHight(node->right)) ? getHight(node->left):getHight(node->right));
    int balanceFactor = getBalanceFactor(node);
    
    if(balanceFactor > 1 && key<node->left->key)
    {
        return rightRotate(node);
    }
    
    if(balanceFactor < -1 && key>node->right->key)
    {
        return leftRotate(node);
    }
    
    if(balanceFactor > 1 && key > node->left->key)
    {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }
    
    if(balanceFactor < -1 && key < node->right->key)
    {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }
    return node;
}
void inorderTravesal(struct Node* node)
{
    if (node!= NULL)
    {
        inorderTravesal(node->left);
        printf("%d ", node->key);
        inorderTravesal(node->right);
    }
}
int main() {
    struct Node* root = NULL;

    root = insertNode(root, 10);
    root = insertNode(root, 20);
    root = insertNode(root, 30);
    root = insertNode(root, 40);
    root = insertNode(root, 50);
    root = insertNode(root, 25);

    printf("Inorder Traversal of AVL Tree:\n");
    inorderTravesal(root);
    printf("\n");

    return 0;
}
