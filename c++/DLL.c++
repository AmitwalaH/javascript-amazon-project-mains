#include <iostream>
using namespace std;

class Node
{

public:
    int data;
    Node *next;
    Node *prev;

    Node(int value)
    {
        this->data = value;
        this->next = NULL;
        this->prev = NULL;
    }
};

Node *insertAtHead(int value, Node *&head, Node *&tail)
{

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
        head->prev = newNode;
        head = newNode;
    }

    return head;
}

Node *insertAtTail(int value, Node *&head, Node *&tail)
{
    if (head == NULL && tail == NULL)
    {
        Node *newNode = new Node(value);
        head = newNode;
        tail = newNode;
    }
    else
    {
        Node *newNode = new Node(value);
        newNode->prev = tail;
        tail->next = newNode;
        tail = newNode;
    }
    return tail;
}

int getLength(Node *&head)
{
    Node *temp = head;
    int count = 0;
    while (temp != NULL)
    {
        count++;
        temp = temp->next;
    }
    return count;
}

Node *insertAtPosition(int pos, int value, Node *&head, Node *&tail)
{
    int l = getLength(head);
    if (pos == 1)
    {
        head = insertAtHead(value, head, tail);
    }
    else if (pos == l + 1)
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
        Node *forward = temp->next;
        temp->next = newNode;
        newNode->prev = temp;
        newNode->next = forward;
        forward->prev = newNode;
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

void print1(Node *tail)
{
    Node *temp = tail;
    while (temp != NULL)
    {
        cout << temp->data << "->";
        temp = temp->prev;
    }
    cout << "NULL" << endl;
}

int main()
{

    Node *head = NULL;
    Node *tail = NULL;

    insertAtTail(101, head, tail);
    insertAtTail(102, head, tail);
    insertAtTail(103, head, tail);
    insertAtTail(104, head, tail);
    insertAtTail(105, head, tail);
    print(head);
    print1(tail);

    insertAtPosition(4, 106, head, tail);
    print(head);
    print1(tail);

    return 0;
}