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
    Node* insert(int value, Node* &head)
    {
        if (head == NULL)
        {
            Node *newNode = new Node(value);
            head = newNode;
        }
        else
        {
            Node *newNode = new Node(value);
            newNode->next = head;
            head = newNode;
        }
        return head;
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

    int middleValue(Node*head){
        Node* temp = head;
        int len = 0;
        while (temp != NULL)
        {
            len++;
            temp = temp->next;
        }

        cout<<len;

        int middle = len / 2;

        temp = head;

        for(int i = 0; i < middle; i++)
        {
           temp = temp->next; 
        }
            return temp->data; 
    }

int main()
{
    Node* head = NULL;
    insert(102,head);
    insert(103,head);
    insert(104,head);
    insert(105,head);
    insert(106,head);
    insert(107,head);
    print(head);
    int mid = middleValue(head);
    cout << mid << endl;
    return 0;
}