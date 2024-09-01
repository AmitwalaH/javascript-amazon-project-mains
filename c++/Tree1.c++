#include <iostream>
#include <queue>
using namespace std;

class Node
{
public:
    int data;
    Node *leftChild;
    Node *rightChild;

    Node(int value)
    {
        this->data = value;
        leftChild = NULL;
        rightChild = NULL;
    }
};

Node *createTree()
{

    int value;

    // cout << "Enter the value For Node: " << endl;
    cin >> value;

    if (value == -1)
    {
        return NULL;
    }
    else
    {
        Node *root = new Node(value);
        // cout << "Adding left child for " << value << endl;
        root->leftChild = createTree();
        // cout << "Adding right child for " << value << endl;
        root->rightChild = createTree();

        return root;
    }
}

void preOrderTraversal(Node *root)
{
    if (root == NULL)
    {
        return;
    }

    // NLR
    // N
    cout << root->data << " ";
    // L
    preOrderTraversal(root->leftChild);
    // R
    preOrderTraversal(root->rightChild);
}

void inOrderTraversal(Node *root)
{
    if (root == NULL)
    {
        return;
    }

    // LNR
    // L
    inOrderTraversal(root->leftChild);
    // N
    cout << root->data << " ";
    // R
    inOrderTraversal(root->rightChild);
}

void postOrderTraversal(Node *root)
{
    if (root == NULL)
    {
        return;
    }

    // LRN
    // L
    preOrderTraversal(root->leftChild);
    // R
    preOrderTraversal(root->rightChild);
    // N
    cout << root->data << " ";
}

void levelOrderTraversal(Node *root)
{
    queue<Node *> q;

    q.push(root);
    q.push(NULL);

    while (!q.empty())
    {
        // queue se niklo;
        Node *front = q.front();
        q.pop();

        if (front == NULL)
        {
            cout << endl;
            if (!q.empty())
            {
                q.push(NULL);
            }
        }
        else
        {
            // phir tum print karlo
            cout << front->data << " ";
            // queue me insert krna
            if (front->leftChild != NULL)
            {
                q.push(front->leftChild);
            }
            if (front->rightChild != NULL)
            {
                q.push(front->rightChild);
            }
        }
    }
}

int main()
{
    Node *root;
    root = createTree();

    // 10 50 -1 -1 -1 30 20 -1 -1 -1

    levelOrderTraversal(root);

    return 0;
}