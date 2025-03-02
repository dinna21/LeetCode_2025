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
    x->height = 1 + (getHight(x->left) > getHight(x->left)) ? getHight(x->left):getHight(x->right);
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
}