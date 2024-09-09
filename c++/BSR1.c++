#include <iostream>
#include <queue>
using namespace std;

class Node
{
public:
    int data;
    Node *left;
    Node *right;

    Node(int val)
    {
        this->data = val;
        this->left = NULL;
        this->right = NULL;
    }
};

Node *buildBst(Node *root, int val)
{
    if (root == NULL)
    {
        root = new Node(val);
        return root;
    }
    else
    {
        if (val < root->data)
        {
            // val -> left Subtree
            root->left = buildBst(root->left, val);
        }
        else
        {
            // val -> right Subtree
            root->right = buildBst(root->right, val);
        }
    }
    return root;
}

Node *createTree()
{
    int val;
    cout << "Enter the value for Node: " << endl;
    cin >> val;

    Node *root = NULL;

    while (val != -1)
    {
        root = buildBst(root, val); // Update root
        cout << "Enter the value for Node: " << endl;
        cin >> val;
    }
    return root;
}

vector<int> ans;

void inOrder(Node *root)
{
    if (root == NULL)
    {
        return;
    }

    inOrder(root->left);
    cout << root->data << " ";
    ans.push_back(root->data);
    inOrder(root->right);
}

void minimumValue()
{
    int minBST = ans.front();

    cout << endl
         << "Minimum value in BST: " << minBST << endl;
}

void maximumValue()
{
    int maxBST = ans.back();

    cout << "Minimum value in BST: " << maxBST << endl;
}

void levelOrderTraversal(Node *root)
{
    if (root == NULL)
    {
        return;
    }
    queue<Node *> q;
    // initial state maintain
    q.push(root);
    q.push(NULL);
    // logic -> step A, B C
    while (!q.empty())
    {
        // queue se nikalo
        Node *front = q.front();
        q.pop();
        if (front == NULL)
        {
            // iska mtlb, current lvl complete hogya h
            cout << endl;
            if (!q.empty())
            {
                q.push(NULL);
            }
        }
        else
        {
            // fer tum print karalo
            cout << front->data << " ";
            // iske bache khalo
            // khalo -> queue me insert krna
            if (front->left)
            {
                q.push(front->left);
            }
            if (front->right)
            {
                q.push(front->right);
            }
        }
    }
}

bool searchInBST(Node *root, int target)
{
    if (root == NULL)
    {
        return false;
    }
    if (root->data == target)
    {
        return true;
    }
    else
    {
        if (target < root->data)
        {
            bool leftAns = searchInBST(root->left, target);
            if (leftAns)
            {
                return true;
            }
        }
        else
        {
            bool rightAns = searchInBST(root->right, target);
            if (rightAns)
            {
                return true;
            }
        }
    }
    return false;
}

int maximumValue2(Node *root)
{
    if (root == NULL)
    {
        return -1;
    }
    while (root->right != NULL)
    {
        root = root->right;
    }
    return root->data;
}

Node *deleteNode(Node *root, int key)
{
    if (root == NULL)
    {
        return NULL;
    }

    if (root->data == key)
    {
        // match
        // ab mujhe node delete karna hai
        // cases;

        // 1-> with 0 child
        if (root->left == NULL && root->right == NULL)
        {
            delete root;
            return NULL;
        }

        // 2-> with left child only
        if (root->left != NULL && root->right == NULL)
        {
            Node *curr = root->left;
            root->left = NULL;
            delete root;
            return curr;
        }

        // 3-> with right child only
        if (root->left == NULL && root->right != NULL)
        {
            Node *curr = root->right;
            root->right = NULL;
            delete root;
            return curr;
        }
        // 4-> with both l and r child
        if (root->left != NULL && root->right != NULL)
        {
            int maxVal = maximumValue2(root->left);
            // replaced  root node value with maxVal
            root->data = maxVal;
            // delete actual node of mAXvAL
            root->left = deleteNode(root->left, maxVal);
            return root;
        }
    }
    else
    {
        // no match
        //  left ya right jao
        if (key < root->data)
        {
            root->left = deleteNode(root->left, key);
        }
        else
        {
            root->right = deleteNode(root->right, key);
        }
    }

    return root;
}

int main()
{
    Node *root;
    root = createTree();

    levelOrderTraversal(root);

    // bool ans = searchInBST(root, 150);
    // if (ans)
    // {
    //     cout << "Target Found!" << endl;
    // }
    // else
    // {
    //     cout << "Target Not Found!" << endl;
    // }

    // inOrder(root);
    // minimumValue();
    // maximumValue();

    return 0;
}
