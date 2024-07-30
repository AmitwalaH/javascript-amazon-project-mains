#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node(int value)
    {
        this->data = value;
        this->next = NULL;
    }
};

Node *insertAtHead(int value, Node *&head, Node *&tail)
{
    // dooo condition ho sakti hai
    if (head == NULL && tail == NULL)
    {
        Node *newNode = new Node(value);
        head = newNode;
        tail = newNode;
    }
    else
    {
        Node *newNode = new Node(value);
        newNode->next = head;
        head = newNode;
    }
    return head;
}

Node *insertAtTail(int value, Node *&head, Node *&tail)
{
    // dooo condition ho sakti hai
    if (head == NULL && tail == NULL)
    {
        Node *newNode = new Node(value);
        head = newNode;
        tail = newNode;
    }
    else
    {
        Node *newNode = new Node(value);
        tail->next = newNode;
        tail = newNode;
    }
    return tail;
}


int len(Node *head)
{
    Node *temp = head;
    int length = 0;
    while (temp != NULL)
    {
        length++;
        temp = temp->next;
    }
    return length;
    // cout << length;
}

void insertAtPosition(int pos, int value, Node *&head, Node *&tail)
{
    int length = len(head);
    if (pos == 1)
    {
        head = insertAtHead(value, head, tail);
    }
    else if (pos == length + 1)
    {
        tail = insertAtTail(value, head, tail);
    }
    else
    {
        Node *temp = head;
        for (int i = 0; i < pos - 2; i++)
        {
            temp = temp->next;
        }
        Node *newNode = new Node(value);
        newNode->next = temp->next;
        temp->next = newNode;
    }
}

void print(Node *head)
{
    Node *temp = head;
    while (temp != NULL)
    {
        cout << temp->data << "->";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}


int main()
{
    Node *head = NULL;
    Node *tail = NULL;

    // insertAtHead(101, head, tail);
    // insertAtHead(102, head, tail);
    // insertAtHead(103, head, tail);
    // print(head);

    // cout << endl;

    insertAtTail(101, head, tail);
    insertAtTail(102, head, tail);
    insertAtTail(103, head, tail);
    insertAtTail(105, head, tail);
    insertAtTail(106, head, tail);
    print(head);

    insertAtPosition(1, 104, head, tail);
    insertAtPosition(4, 108, head, tail);
    insertAtPosition(8, 109, head, tail);

    print(head);
    len(head);
    cout << endl;

    return 0;
}