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