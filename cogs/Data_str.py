import discord
from discord.ext import commands

col = discord.Color.purple()


class DSA(commands.Cog):
    def __init__(self, bot):                      # required to use bot instance in the cog
        self.bot = bot


# * -------------------------------------------------------------------
# * -------------------------------------------------------------------
    
    @commands.group()
    async def searching(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```{ctx.subcommand_passed} doesn't belong to searching\n\nFor more info on a specific command, use {'*help*'} command```")

    @searching.command()
    async def search_element(self, ctx, ele, *array):
        for i in range(len(array)):
            if array[i] == ele:
                embed = discord.Embed(
                    colour=col,
                    title=f"Element is present at position: ```{i}```"
                )
                embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
                await ctx.send(embed = embed)
        
                return
            
        embed = discord.Embed(
            colour=col,
            title=f"Element ```{ele}``` is not present!"
        )
        
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed)

# * -------------------------------------------------------------------
    
    @searching.command()
    async def linear_search_code(self, ctx, language):
        if(language == "python"):
            ans = """def linear_Search(list1, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  

print("Enter size of the list")
size = int(input())
print("Enter elements: ")
list1 = [input() for i in range(size)]  
print("Enter element to be searched: ")
key = input()
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)  """
        
        if(language == "c++" or language == "cpp"):
            ans = """
#include <iostream>
using namespace std;

int main(){
    int size;
    cout<<"Enter size: "; 
    cin>>size;
    int *arr = new int[size];
    cout<<"Enter elements: ";

    for(int i = 0; i<size; i++) {
        cin>>arr[i];
    }

    cout<<"Enter element to search: ";
    int ele;
    cin>>ele;
    for(int i = 0; i<size; i++) {
        if(arr[i] == ele) {
            cout<<"Index is: "<<i;
            return 0;
        }
    }
    cout<<"Element is not present";
    return 0;
}"""
        
        await ctx.send(f"```{ans}```")


# * -------------------------------------------------------------------
            
    @searching.command()
    async def binary_search_code(self, ctx, language):
        
        if(language == "python"):
            ans = """def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right)//2

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  

    return -1  

print("Enter size of array: ")
size = int(input())
print("Enter elements: ")
arr = [int(input()) for i in range(size)]
print("Enter element to be searched: ")
target = int(input())
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} is not found in the array")"""
    
        if(language == "c++" or language == "cpp"):
            ans = """#include <iostream>
using namespace std;

int main() {
    cout<<"Enter size of array: ";
    int size;
    cin>>size;
    int *arr = new int[size];
    cout<<"Enter elements: ";

    for(int i = 0; i<size; i++) {
        cin>>arr[i];
    }

    cout<<"Enter element to be searched: ";
    int ele;
    cin>>ele;

    if(ele<arr[size/2]) {
        for(int j = 0; j<size/2; j++) {
            if(arr[j] == ele) {
                cout<<"Index is: "<<j;
                return 0;
            }
            else {
                continue;
            }
        }
    }

    else {
        for(int i = size/2; i<size+1; i++) {
            if(arr[i] == ele) {
                cout<<"Index is: "<<i;
                return 0;
            }
            else {
                continue;
            }
        }
    }
}"""
            
        await ctx.send(f"```{ans}```")

# * -------------------------------------------------------------------
# * -------------------------------------------------------------------

    @commands.group()
    async def sorting(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```{ctx.subcommand_passed} doesn't belong to sorting\n\nFor more info on a specific command, use {'*help*'} command```")
    
    
    @sorting.command()
    async def sort(self, ctx, *array):
        array = [int(ele) for ele in array]
        n = len(array)
        for i in range(n):
            for j in range(i+1, n):
                if(array[i]>array[j]):
                    array[i], array[j] = array[j], array[i]
                else: continue
        
        embed = discord.Embed(
            colour=col,
            title=f"Sorted array: ```{array}```"
        )
        
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.display_avatar.url)
        await ctx.send(embed = embed)

# * -------------------------------------------------------------------
        
    @sorting.command()
    async def bubble_sort_code(self, ctx, language):
        if(language == "python"):
            ans = """print("Enter size: ")
size = int(input())
print("Enter elements: ")
array = [int(input()) for i in range(size)]
n = len(array)

for i in range(n):
    for j in range(i+1, n):
        if(array[i]>array[j]):
            array[i], array[j] = array[j], array[i]
        else: continue
    
for i in range(size):
    print(array[i], end=" ") """
        
        
        if(language == "cpp" or language == "c++"):
            ans = """#include <iostream>
using namespace std;

int main() {
    cout<<"Enter size: ";
    int size;
    cin>>size;
    cout<<"Enter elements: ";
    int *arr = new int[size];

    for(int i = 0; i<size; i++) {
        cin>>arr[i];
    }

    for(int k = 0; k<size; k++) {  
        for(int i = 0, j = i+1; j<size; i++, j++) {

            if(arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }

            else{
                continue;
            }
        }
    }

    for(int i = 0; i<size; i++) {
        cout<<arr[i]<<" ";
    }

}"""
            
        await ctx.send(f"```{ans}```")
        
# * -------------------------------------------------------------------    

    @sorting.command()
    async def selection_sort_code(self, ctx, language):
        if(language == "python"):
            ans = """def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


print("Enter size: ")
size = int(input())
print("Enter elements: ")
arr = [int(input()) for i in range(size)]
    
selection_sort(arr)
    
print("Sorted array:", arr)
"""
        
    
        if(language == "c++" or language == "cpp"):
            ans = """#include <iostream>
using namespace std;


int main() {

    cout<<"Enter size: ";
    int size;
    cin>>size;
    cout<<"Enter elements: ";
    int *arr = new int[size];

    for(int i = 0; i<size; i++) {
        cin>>arr[i];
    }

    for(int i = 0; i<size; i++) {

        int min = arr[i];
        int min_index = i;
        
        for(int j = i+1; j<size; j++) {
            if(arr[j]<min) {
                int temp = arr[j];
                arr[j] = min;
                min = temp;
                min_index = j;
            }
        }

        int temp1 = arr[i];
        arr[i] = min;
        arr[min_index] = temp1;
    
    }

    for(int i = 0; i<size; i++) {
        cout<<arr[i]<<" ";
    }

}
"""
            
        await ctx.send(f"```{ans}```")
    
# * -------------------------------------------------------------------

    @sorting.command()
    async def insertion_sort_code(self, ctx, language):
        if(language == "python"):
            ans = """def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and key < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

print("Enter size: ")
size = int(input())
print("Enter elements: ")
array = [int(input()) for i in range(size)]

insertion_sort(array)

print("Sorted array: ", array)"""    
        
        if(language == "cpp" or language == "c++"):
            ans = """#include <iostream>
using namespace std;

int main() {
    int size;
    cin>>size;
    int *arr = new int[size];

    for(int i = 0; i<size; i++) {
        cin>>arr[i];
    }

    for(int i = 1; i<size; i++) {
        for(int j = 0; j<=i-1; j++) {
            if(arr[i]<arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
            else {
                continue;
            }
        }
    }

    for(int i = 0; i<size; i++) {
        cout<<arr[i]<<" ";
    }

}
"""
        
        await ctx.send(f"```{ans}```")

# * -------------------------------------------------------------------    

    @sorting.command()
    async def quick_sort_code(self, ctx, language):
        if(language == "python"):
            ans = """def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high] 
   for j in range(low , high):
      if arr[j] <= pivot:
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )

def quickSort(arr,low,high):
   if low < high:
      pi = partition(arr,low,high)
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)


print("Enter size: ")
n = int(input())
print("Enter elements: ")
arr = [int(input()) for i in range(n)]

quickSort(arr,0,n-1)
print ("Sorted array is: ")
for i in range(n):
   print (arr[i],end=" ")
   """
   
        if(language == "cpp" or language == "c++"):
            ans = """#include <iostream>
using namespace std;

int partition(int *arr, int start, int end) {
    int pivot = arr[start];
    int count = 0;

    for(int i = start+1; i<=end; i++) {
        if(arr[i]<=pivot) {
            count++;
        }
    }

    int pivotindex = start+count;
    swap(arr[pivotindex], arr[start]);

    int s = start, e = end;
    while(arr[s]<pivot) {
        s++;
    }

    while(arr[e]>=pivot) {
        e--;
    }

    while(pivotindex>s && pivotindex<e) {
        swap(arr[s], arr[e]);
        s++;
        e--;
    }

    return pivotindex;

}

void sorting(int *arr, int start, int end) {
    if(start<end) {
        int p = partition(arr, start, end);
        sorting(arr, start, p-1);
        sorting(arr, p+1, end);
    }
}

int main() {
    cout<<"Enter size: ";
    int size;
    cin>>size;
    cout<<"Enter elements: "<<endl;
    int *arr = new int[size];

    for(int i = 0; i<size; i++) {
        cin>>arr[i];
    }

    sorting(arr,0,size-1);
    cout<<"Sorted array: ";
    
    for(int i = 0; i<size; i++) {
        cout<<arr[i]<<" ";
    }
}

"""
        
        await ctx.send(f"```{ans}```")

# * -------------------------------------------------------------------  

    @sorting.command()
    async def merge_sort_code(self, ctx, language):
        if(language == "python"):
            ans = """def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]
 
        mergeSort(sub_array1)
        mergeSort(sub_array2)
         
        i = j = k = 0
 
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1
 
        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1

print("Enter size: ")
n = int(input())
print("Enter elements: ")
arr = [int(input()) for i in range(n)]

mergeSort(arr)

print(arr)"""

        if(language == "cpp" or language == "c++"):
            ans = """#include <iostream>
using namespace std;

    void merge(int *arr, int s, int e) {

    int mid = (s+e)/2;

    int len1 = mid - s + 1;
    int len2 = e - mid;

    int *first = new int[len1];
    int *second = new int[len2];

    // copying values
    int mainarrayindex = s;
    for(int i = 0; i<len1; i++) {
        first[i] = arr[mainarrayindex++];
    }

    for(int i = 0; i<len2; i++) {
        second[i] = arr[mainarrayindex++];
    }

    // merge sorted arrays
    int index1 = 0;
    int index2 = 0;

    mainarrayindex = s;

    while(index1 < len1 && index2 < len2) {
        if(first[index1] < second[index2]) {
            arr[mainarrayindex] = first[index1];
            index1++;
        }

        else {
            arr[mainarrayindex] = second[index2];
            index2++;
        }
        mainarrayindex++;
    }

    while(index1 < len1) {
        arr[mainarrayindex] = first[index1];
        index1++;
        mainarrayindex++;
    }
    
    while(index2 < len2) {
        arr[mainarrayindex] = second[index2];
        index2++;
        mainarrayindex++;
    }
    
}

void mergesort(int *arr, int s, int e) {

    if(e <= s) return;

    int mid = (s+e)/2;

    // Sorting left part 
    mergesort(arr,s,mid); // Ex: In an array of 7 elements, we'll apply merge sort on first 4 elements (0,1,2,3)

    // Sorting right sort
    mergesort(arr, mid+1, e);

    // Merge
    merge(arr, s, e);
}


int main() {
    cout<<"Enter size: ";
    int size;
    cin>>size;

    cout<<"Enter elements: ";
    int *arr = new int[size];

    for(int i = 0; i<size; i++) {
        cin>>arr[i];
    }

    mergesort(arr,0,size-1);
    cout<<"Sorted array: ";

    for(int i = 0; i<size; i++) {
        cout<<arr[i]<<" ";
    }

}"""
        
        await ctx.send(f"```{ans}```")
  
# * -------------------------------------------------------------------    
# * -------------------------------------------------------------------

    @commands.group()
    async def linked_list(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```{ctx.subcommand_passed} doesn't belong to linked_list\n\nFor more info on a specific command, use {'*help*'} command```")

# * -------------------------------------------------------------------

    @linked_list.command()
    async def head_insertion_code(self, ctx, language):
        if language == "python":
            ans = """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_head(3)
    linked_list.insert_at_head(2)
    linked_list.insert_at_head(1)

    linked_list.display()
"""
    
        if(language == "cpp" or language == "c++"):
            ans = """#include <iostream>
using namespace std;

class Node{
    public:
    int data;
    Node* next;
};

Node* InsertAtBeg(Node* head, int data) {
    Node* node1 = new Node();
    node1 -> data = data;
    node1 -> next = NULL;

    if(head == NULL) {
        head = node1;                 
    }
    else {
        node1 -> next = head;
        head = node1;
    }
    return head;
}

void print(Node* head) {
    Node* temp = head;
    if(temp == NULL) {
        return;
    }

    while(temp!=NULL) {
        cout<<temp->data<<" ";
        temp = temp -> next;
    }
    cout<<endl;
}

int main() {
    Node* head = NULL;
    Node* tail = NULL;
    
    head = InsertAtBeg(head, 10);
    head = InsertAtBeg(head, 20);
    head = InsertAtBeg(head, 30);
    head = InsertAtBeg(head, 40);
    head = InsertAtBeg(head, 50);

    print(head);
}"""
    
        await ctx.send(f"```{ans}```")

# * -------------------------------------------------------------------

    @linked_list.command()
    async def tail_insertion_code(self, ctx, language):
        if language == "python":
            ans = """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, data):
        new_node = Node(data)
        
        # If the linked list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_tail(1)
    linked_list.insert_at_tail(2)
   

"""

        if(language == "cpp" or language == "c++"):
            ans = """#include <iostream>
using namespace std;

class Node{
    public:
    int data;
    Node* next;
};

Node* InsertAtEnd(Node* tail, int data) {
    Node* node = new Node();

    node -> data = data;
    node -> next = NULL;

    if(tail == NULL) {
        tail = node;
    }
    else {
        tail -> next = node;
        tail = tail -> next;
    }
    return tail;
}

void print(Node* head) {
    Node* temp = head;
    if(temp == NULL) {
        return;
    }

    while(temp!=NULL) {
        cout<<temp->data<<" ";
        temp = temp -> next;
    }
    cout<<endl;
}

int main() {
    Node* head = NULL;
    Node* tail = NULL;

    tail = InsertAtEnd(tail, 10);
    head = tail;
    tail = InsertAtEnd(tail, 20);
    tail = InsertAtEnd(tail, 30);
    tail = InsertAtEnd(tail, 40);
    tail = InsertAtEnd(tail, 50);

    print(head);
}
"""
            
        await ctx.send(f"```{ans}```")

# * -------------------------------------------------------------------

    @linked_list.command()
    async def position_insertion_code(self, ctx, language):
        if language == "python":
            ans = """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, position):
        new_node = Node(data)

        # If inserting at the head
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        prev = None

        while current and count < position:
            prev = current
            current = current.next
            count += 1

        if count == position:
            prev.next = new_node
            new_node.next = current
        else:
            print("Invalid position. The list has fewer elements.")

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_position(1, 0)
    linked_list.insert_at_position(3, 1)
    linked_list.insert_at_position(2, 1)

    linked_list.display()

"""

        if(language == "cpp" or language == "c++"):
            ans = """#include <iostream>
using namespace std;

class Node{
    public:
    int data;
    Node* next;

    Node(int data) {
        this -> data = data; 
        this -> next = NULL; 
    }
};

void InsertAtHead(Node* &head, int data) {
    Node* temp = new Node(data);
    temp -> next = head;
    head = temp;
}

void InsertAtTail(Node* &tail, int data) {
    Node* temp = new Node(data);
    tail -> next = temp;
    tail = tail -> next;
}

void InsertAtPosition(Node* &head, Node* &tail, int position, int data) {
    Node* temp = head;
    int count = 1;

    if(position == 1) {
        InsertAtHead(head, data);
        return;
    }

    while(count<position - 1) {
        count++;
        temp = temp -> next;
    }

    if(temp == NULL) {
        InsertAtTail(tail, data);
    }

    Node* XXX = new Node(data);
    XXX -> next = temp -> next;
    temp -> next = XXX;

}

void print(Node* &head) {
    Node* temp = head;
    while(temp != NULL) {                           
        cout<<temp -> data <<" ";
        temp = temp -> next; 
    }
    cout<<endl;
}

int main() {

    Node* node1 = new Node(1);
    Node* node2 = node1 -> next = new Node(2);
    Node* node3 = node1 -> next -> next = new Node(3);
    Node* node4 = node1 -> next -> next -> next = new Node(4);
    Node* node5 = node1 -> next -> next -> next -> next = new Node(5);

    Node *head = node1;
    Node *tail = node5;

    print(head);

    InsertAtPosition(head, tail, 3, 69);
    print(head);

}
"""
        
        await ctx.send(f"```{ans}```")

# * -------------------------------------------------------------------

    @linked_list.command()
    async def deletion_at_beginning(self, ctx, language):
        if language == "python":
            ans = """# A complete working Python3 program to
# demonstrate deletion in singly 
# linked list with class 

# Node class 
class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 

	# Function to initialize head 
	def __init__(self): 
		self.head = None

	# Function to insert a new node at the beginning 
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	def deleteNode(self, key): 
		temp = self.head 

		if (temp is not None): 
			if (temp.data == key): 
				self.head = temp.next
				temp = None
				return
 
		while(temp is not None): 
			if temp.data == key: 
				break
			prev = temp 
			temp = temp.next

		if(temp == None): 
			return

		prev.next = temp.next

		temp = None

	def printList(self): 
		temp = self.head 
		while(temp): 
			print (" %d" %(temp.data)), 
			temp = temp.next

llist = LinkedList() 
llist.push(7) 
llist.push(1) 
llist.push(3) 
llist.push(2) 

print ("Created Linked List: ")
llist.printList() 
llist.deleteNode(1) 
print ("Linked List after Deletion of 1:")
llist.printList() 
"""

        if(language == "cpp" or language == "c++"):
            ans = """#include<iostream>
using namespace std;
int main(){
class node{
   public:
      int data;
      node*next;
      node(int d){
         data=d;
         node*next=NULL;
      }
};
void insertAtFirstNode(node*&head, int data){
   node*n= new node(data);
   n->next= head;
   head=n;
}
void print(node*head){
   while(head!=NULL){
      cout<<head->data<<"->";
      head=head->next;
   }
   cout<<endl;
}
void deleteAtFirst(node*&head){
   if(head==NULL){
      return;
   }
   node*temp=head;
   head= head->next;
   delete temp;
   return;
}
int main(){
   node*head= NULL;
   insertAtFirstNode(head,1);
   insertAtFirstNode(head,2);
   insertAtFirstNode(head,3);
   insertAtFirstNode(head,4);
   deleteAtFirst(head);
   print(head);
}"""
        
        await ctx.send(f"```{ans}```")

# * -------------------------------------------------------------------

    @linked_list.command()
    async def deletion_at_end(self, ctx, language):
        if language == "python":
            ans = """class Node:  
    def __init__(self,data):  
        self.data = data;  
        self.next = None;  
          
class DeleteEnd:   
    def __init__(self):  
        self.head = None;  
        self.tail = None;  

    def addNode(self, data):    
        newNode = Node(data);  
          
        if(self.head == None):  
            self.head = newNode;  
            self.tail = newNode;  
        else:  
            self.tail.next = newNode;   
            self.tail = newNode;  
               
    def deleteFromEnd(self):  
        if(self.head == None):  
            print("List is empty");  
            return;  
        else:  
            if(self.head != self.tail):  
                current = self.head;  
                while(current.next != self.tail):  
                    current = current.next;   
                self.tail = current;  
                self.tail.next = None;  
                  
            else:  
                self.head = self.tail = None;  
                  
    #display() will display all the nodes present in the list  
    def display(self):    
        current = self.head;  
        if(self.head == None):  
            print("List is empty");  
            return;  
        while(current != None):  
            #Prints each node by incrementing pointer  
            print(current.data),  
            current = current.next;  
   
sList = DeleteEnd();  
   
#Adds data to the list  
sList.addNode(1);  
sList.addNode(2);  
sList.addNode(3);  
sList.addNode(4);  
   
print("Original List: ");  
sList.display();  
   
while(sList.head != None):  
    sList.deleteFromEnd();   
    print("Updated List: ");  
    sList.display();  """

        if(language == "cpp" or language == "c++"):
            ans = """#include<iostream>
using namespace std;
class node{
   public:
   int data;
   node*next;
   node(int d){
      data=d;
      node*next= NULL;
   }
};
void insertAtFirst(node*&head, int data){
   node*n= new node(data);
   n->next= head;
   head=n;
}
void printNode(node*head){
   while(head!=NULL){
      cout<<head->data<<"->";
      head=head->next;
   }
   cout<<endl;
}
void deleteatTail(node*head){
   node*prev= NULL;
   node*temp= head;
   while(temp->next!=NULL){
      prev= temp;
      temp=temp->next;
   }
   delete temp;
   prev->next= NULL;
   return;
}
int main(){
   node*head= NULL;
   insertAtFirst(head,5);
   insertAtFirst(head,4);
   insertAtFirst(head,3);
   insertAtFirst(head,2);
   insertAtFirst(head,1);
   deleteatTail(head);
   printNode(head);
}"""
        
        await ctx.send(f"```{ans}```")

# * -------------------------------------------------------------------

    @linked_list.command()
    async def deletion_at_position(self, ctx, language):
        if language == "python":
            ans = """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev

    def printList(self):
        temp = self.head
        while(temp):
            print (" %d " % (temp.data),end=" ")
            temp = temp.next

llist = LinkedList()
llist.push(7)
llist.push(2)
llist.push(5)
llist.push(1)

print ("Created Linked List: ")
llist.printList()
llist.deleteNode(2)
print ("\nLinked List after Deletion at position 4: ")
llist.printList()"""

        if(language == "cpp" or language == "c++"):
            ans = """#include <bits/stdc++.h>
using namespace std;
struct Node {
   int data;
   struct Node *next;
};
void insertNode(struct Node** head_ref, int new_data) {
   struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
   new_node->data = new_data;
   new_node->next = (*head_ref);
   (*head_ref) = new_node;
}
void deleteNode(struct Node **head_ref, int position) {
   if (*head_ref == NULL) {
      return;
   }
   struct Node* temp = *head_ref;
   if (position == 1) {
      *head_ref = temp->next;
      free(temp);
      return;
   }
   for (int i = 2; temp != NULL && i < position - 1; i++) {
      temp = temp->next;
   }
   if (temp == NULL || temp->next == NULL) {
      return;
   }
   struct Node *next = temp->next->next;
   free(temp->next);
   temp->next = next;
}
void printLinkedList(struct Node *node) {
   while (node != NULL) {
      cout << node->data << "->";
      node = node->next;
   }
}
int main() {
   struct Node* head = NULL;
   insertNode(&head, 1);
   insertNode(&head, 2);
   insertNode(&head, 3);
   insertNode(&head, 4);
   insertNode(&head, 5);
   cout << "Linked list before deletion:" << endl;
   printLinkedList(head);
   deleteNode(&head, 1);
   cout << "\nLinked list after deletion:" << endl;
   printLinkedList(head);
   return 0;
}"""
        
        await ctx.send(f"```{ans}```")

# * -------------------------------------------------------------------

    @linked_list.command()
    async def reversal_code(self, ctx, language):
        if language == "python":
            ans = """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def insert_at_tail(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_tail(1)
    linked_list.insert_at_tail(2)
    linked_list.insert_at_tail(3)

    print("Original linked list:")
    linked_list.display()

    linked_list.reverse()

    print("\nReversed linked list:")
    linked_list.display()
"""

        if(language == "cpp" or language == "c++"):
            ans = """#include <iostream>
using namespace std;

struct Node {
    int data;
    struct Node* next;

    Node(int data) {
        this -> data = data;
        this -> next = NULL;
    }
};

Node* reverse(Node* head) {
    Node* prev = head;
    Node* current = head -> next;

    while(current!=NULL) {
        Node* after = current -> next;
        current -> next = prev;
        prev = current;
        current = after;
    }
    head -> next = NULL;
    head = prev;
    return prev;
}

Node* InserAtHead(Node* head, int data) {
    Node* temp = new Node(data);
    if(head == NULL) {
        head = temp;
    }
    else {
            temp -> next = head;
            head = temp;
    }
    return head;
}

Node* InserAtTail(Node* tail, int data) {
    Node* temp = new Node(data);
    if(tail == NULL) {
        tail = temp;
    }

    else {
        tail -> next = temp;
        tail = tail -> next;
    }
    return tail;
}

void print(Node* head) {
    Node* temp = head;
    if(head == NULL) {
        return;
    }
    while(temp!=NULL) {
        cout<<temp -> data<<" ";
        temp = temp -> next;
    }
    cout<<endl;
}

int main() {
    Node* head = NULL;
    Node* tail = NULL;

    head = InserAtHead(head, 1);
    head = InserAtHead(head, 2);
    head = InserAtHead(head, 3);
    head = InserAtHead(head, 4);
    head = InserAtHead(head, 5);
    print(head);
    head = reverse(head);
    print(head);

    cout<<endl;

    tail = InserAtTail(tail, 1);
    head = tail;
    tail = InserAtTail(tail, 2);
    tail = InserAtTail(tail, 3);
    tail = InserAtTail(tail, 4);
    tail = InserAtTail(tail, 5);
    print(head);
    head = reverse(head);
    print(head);
}
"""
    
        await ctx.send(f"```{ans}```")

# * -------------------------------------------------------------------
# * -------------------------------------------------------------------

    @commands.group()
    async def stack(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```{ctx.subcommand_passed} doesn't belong to stack\n\nFor more info on a specific command, use {'*help*'} command```")

# * -------------------------------------------------------------------

    @stack.command()
    async def implement(self, ctx, language):
        
        if(language == "python"):
            ans = """class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Stack is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  # Stack is empty

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack:", stack.items)

    popped_item = stack.pop()
    print("Popped item:", popped_item)

    peeked_item = stack.peek()
    print("Peeked item:", peeked_item)

    print("Is the stack empty?", stack.is_empty())
    print("Stack size:", stack.size())
"""
        
        if(language == "cpp" or language == "c++"):
            ans = """#include <iostream>
using namespace std;

int Stack[100];
int size = 100;
int top = -1;

void push(int val) {
    if(top>=size-1) {
        cout<<"Stack is full";
    }
    else {
        top = top + 1;
        Stack[top] = val;
    }
}

void pop() {
    if(top<=-1) {
        cout<<"No element";
    }
    else {
        cout<<"element is: "<<Stack[top];
        top--;    
    }
}

void display() {
    if(top>=0) {
        cout<<"Elements are: ";
        for(int i = top; i>=0; i--) {
            cout<<Stack[i]<<" ";
        }
    }
    else {
        cout<<"Empty";
    }
}

int main() {
    while(1) {
        int val;
        int choice;
        cout<<endl<<"1. Push"<<endl<<"2. Pop"<<endl<<"3. Display"<<endl<<"4. Exit"<<endl;;
        cout<<"Enter the choice: ";
        cin>>choice;

        switch(choice) {

            case 1:
            cout<<"Enter value to push: ";
            cin>>val;
            push(val);
            break;

            case 2:
            pop();
            break;

            case 3:
            display();
            break;

            case 4:
            cout<<"EXITING"<<endl;
            exit(0);
            
            default:
            cout<<"Invalid";
        }
    }
    return 0;
}
"""
            
        await ctx.send(f"```{ans}```")
            
# * -------------------------------------------------------------------

    @stack.command()
    async def reverse(self, ctx, language):
        if(language == "python"):
            ans = """class Stack:
    def __init__(self, size):
        self.size = size
        self.items = []

    def push(self, item):
        if len(self.items) < self.size:
            self.items.append(item)
        else:
            print("Stack is full. Cannot push item:", item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Stack is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  # Stack is empty

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

    def get_size(self):
        return len(self.items)

def reverse_stack(stack):
    temp_container = Stack(stack.get_size())

    while not stack.is_empty():
        temp_container.push(stack.pop())

    while not temp_container.is_empty():
        stack.push(temp_container.pop())

if __name__ == "__main__":
    size = int(input("Enter the size of the stack: "))
    stack = Stack(size)

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack:", stack.items)

    popped_item = stack.pop()
    print("Popped item:", popped_item)

    peeked_item = stack.peek()
    print("Peeked item:", peeked_item)

    print("Is the stack empty?", stack.is_empty())
    print("Is the stack full?", stack.is_full())
    print("Stack size:", stack.get_size())

    reverse_stack(stack)

    print("Reversed Stack:", stack.items)
"""

        if(language == "cpp" or language == "c++"):
            ans = """include <iostream>
using namespace std;

int *Stack;  // Dynamic stack array
int size;    // Size of the stack
int top = -1;

void initializeStack(int customSize) {
    size = customSize;
    Stack = new int[size];
}

void push(int val) {
    if (top >= size - 1) {
        cout << "Stack is full" << endl;
    } else {
        top = top + 1;
        Stack[top] = val;
    }
}

void pop() {
    if (top <= -1) {
        cout << "No element" << endl;
    } else {
        cout << "Element is: " << Stack[top] << endl;
        top--;
    }
}

void display() {
    if (top >= 0) {
        cout << "Elements are: ";
        for (int i = top; i >= 0; i--) {
            cout << Stack[i] << " ";
        }
        cout << endl;
    } else {
        cout << "Empty" << endl;
    }
}

void reverse() {
    int *tempStack = new int[size];
    int tempTop = top;

    for (int i = 0; i <= tempTop; i++) {
        tempStack[i] = Stack[tempTop - i];
    }

    for (int i = 0; i <= tempTop; i++) {
        Stack[i] = tempStack[i];
    }

    delete[] tempStack;
}

int main() {
    int customSize;
    cout << "Enter the size of the stack: ";
    cin >> customSize;
    initializeStack(customSize);

    while (1) {
        int val;
        int choice;
        cout << endl << "1. Push" << endl << "2. Pop" << endl << "3. Display" << endl << "4. Reverse" << endl << "5. Exit" << endl;
        cout << "Enter the choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter value to push: ";
                cin >> val;
                push(val);
                break;

            case 2:
                pop();
                break;

            case 3:
                display();
                break;

            case 4:
                reverse();
                cout << "Stack reversed." << endl;
                break;

            case 5:
                cout << "EXITING" << endl;
                delete[] Stack; // Free allocated memory
                exit(0);

            default:
                cout << "Invalid" << endl;
        }
    }

    return 0;
}
"""
        
        await ctx.send(f"```{ans}```")

# * -------------------------------------------------------------------
# * -------------------------------------------------------------------

    @commands.group()
    async def queue(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f"```{ctx.subcommand_passed} doesn't belong to queue\n\nFor more info on a specific command, use {'*help*'} command```")

# * -------------------------------------------------------------------

    @queue.command()
    async def implement(self, ctx, language):
        
        if(language == "python"):
            ans = """queue = [0] * size
n = size
front = -1
rear = -1

def Insert():
    global front, rear
    val = 0

    if rear == n - 1:
        print("Queue Overflow")
    else:
        if front == -1:
            front = 0
        val = int(input("Insert the element in queue: "))
        rear += 1
        queue[rear] = val

def Delete():
    global front
    if front == -1 or front > rear:
        print("Queue Underflow")
    else:
        print("Element deleted from queue is:", queue[front])
        front += 1

def Display():
    if front == -1:
        print("Queue is empty")
    else:
        print("Queue elements are:", end=" ")
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print()

while True:
    print("1) Insert element to queue")
    print("2) Delete element from queue")
    print("3) Display all the elements of queue")
    print("4) Exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        Insert()
    elif ch == 2:
        Delete()
    elif ch == 3:
        Display()
    elif ch == 4:
        print("Exit")
        break
    else:
        print("Invalid choice")
"""
        
        if(language == "cpp" or language == "c++"):
            ans = """#include <iostream>
using namespace std;
int queue[size], n = size, front = - 1, rear = - 1;

void Insert() {
    int val;

    if (rear == n - 1)
        cout<<"Queue Overflow"<<endl;

    else {
        if (front == - 1)
        front = 0;
        cout<<"Insert the element in queue : "<<endl;
        cin>>val;
        rear++;
        queue[rear] = val;
    }
}

void Delete() {
    if (front == - 1 || front > rear) {
        cout<<"Queue Underflow ";
        return ;
    } 
    
    else {
        cout<<"Element deleted from queue is : "<<queue[front]<<endl;
        front++;
    }
}

void Display() {
    if (front == - 1) {
        cout<<"Queue is empty"<<endl; }
    else {
        cout<<"Queue elements are :";
        for (int i = front; i <= rear; i++)
            cout<<queue[i]<<" ";
            cout<<endl;
        }
}

int main() {
    int ch;
    cout<<"1) Insert element to queue"<<endl;
    cout<<"2) Delete element from queue"<<endl;
    cout<<"3) Display all the elements of queue"<<endl;
    cout<<"4) Exit"<<endl;
do {
    cout<<"Enter your choice : "<<endl;
    cin>>ch;
    switch (ch) {

    case 1: Insert();
    break;
    case 2: Delete();
    break;
    case 3: Display();
    break;
    case 4: cout<<"Exit"<<endl;
    break;
    default: cout<<"Invalid choice"<<endl;
    }
} while(ch!=4);
    return 0;
}
"""
            
        await ctx.send(f"```{ans}```")
            
# * -------------------------------------------------------------------

    @queue.command()
    async def reverse(self, ctx, language):
        if(language == "python"):
            ans = """size = int(input("Enter the size of the queue: "))
queue = [0] * size
n = size
front = -1
rear = -1

def Insert():
    global front, rear
    val = 0

    if rear == n - 1:
        print("Queue Overflow")
    else:
        if front == -1:
            front = 0
        val = int(input("Insert the element in queue: "))
        rear += 1
        queue[rear] = val

def Delete():
    global front
    if front == -1 or front > rear:
        print("Queue Underflow")
    else:
        print("Element deleted from queue is:", queue[front])
        front += 1

def Display():
    if front == -1:
        print("Queue is empty")
    else:
        print("Queue elements are:", end=" ")
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print()

def Reverse():
    if front == -1:
        print("Queue is empty. Nothing to reverse.")
    else:
        reversed_queue = []
        for i in range(rear, front - 1, -1):
            reversed_queue.append(queue[i])
        
        # Copy reversed elements back to the original queue
        for i in range(len(reversed_queue)):
            queue[front + i] = reversed_queue[i]

while True:
    print("1) Insert element to queue")
    print("2) Delete element from queue")
    print("3) Display all the elements of queue")
    print("4) Reverse the queue")
    print("5) Exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        Insert()
    elif ch == 2:
        Delete()
    elif ch == 3:
        Display()
    elif ch == 4:
        Reverse()
        print("Queue reversed.")
    elif ch == 5:
        print("Exit")
        break
    else:
        print("Invalid choice")
"""

        if(language == "cpp" or language == "c++"):
            ans = """
void Reverse(queue<int>& q) {
    stack<int> s;

    while (!q.empty()) {
        s.push(q.front());
        q.pop();
    }

    while (!s.empty()) {
        q.push(s.top());
        s.pop();
    }

    cout << "Queue reversed." << endl;
}

"""
        
        await ctx.send(f"```{ans}```")

# * -------------------------------------------------------------------

    @search_element.error
    @sort.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("```Invalid arguments are provided!\n\nFor more info on a specific command, use {'*help*'} command```")


async def setup(bot):
    await bot.add_cog(DSA(bot)) 
