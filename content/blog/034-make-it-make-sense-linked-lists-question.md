+++
title = 'A question on linked lists: make it make sense!'
date = 2025-04-08T13:18:28+05:00
Categories = ["Computers", "Programming"]
draft = false
+++

I'm new to linked lists, so this question drove me up the wall! The question (in question) is from an A Level computer science past paper (from summer 2021 variant 42).

The main demands of this question aren't anything too complicated. They were:
1. create a node class
2. write a procedure to output the nodes in the linked list
3. write a function that adds a node to the linked list

# Foreword
This exam wanted you to implement the linked list as an array of node objects, with your null pointers represented as a -1.

# 1. Create a node class
I chose the long route to do this, where a node's pointer defaults to -1. My class definition looked as such:

{{< highlight python "linenos=inline, style=arduino" >}}
class Node:
  def __init__(self, data):
    self.data = data
    self.next_node = -1
{{< /highlight >}}

Then I created a list of nodes. The values and the pointers were given in the exam.

{{< highlight python "linenos=inline, style=arduino" >}}
linked_list = [
    Node(1),
    Node(5),
    Node(6),
    Node(7),
    Node(2),
    Node(0),
    Node(0),
    Node(56),
    Node(0),
    Node(0),
]

# linking the list
linked_list[0].next_node = 1
linked_list[1].next_node = 4
linked_list[2].next_node = 7
linked_list[3].next_node = -1
linked_list[4].next_node = 2
linked_list[5].next_node = 6
linked_list[6].next_node = 8
linked_list[7].next_node = 3
linked_list[8].next_node = 9
linked_list[9].next_node = -1
{{< /highlight >}}

The exam tells you to declare a variable that points to the next free space in the list and another that points to its start ("start_pointer") with the values 5 and 0 respectively.

What I found rather upsetting about this question is that it doesn't tell you that a free space in this list is denoted by a 0! It also tells you to delcare a variable called "empty_list" but doesn't tell you what that is for! I figured both of these things out only by looking at the mark scheme! "empty_list" is supposed to denote the index of the next free space in the list. They could have at least given that variable a decent name, like "next_free_space"! Preposterous!

{{< highlight python "linenos=inline, style=arduino" >}}
empty_list = 5
start_pointer = 0
{{< /highlight >}}

# 2. Write a procedure to output the nodes in the linked list

Fairly simple logic here: we want to print the data in all nodes *until* the node points to a -1. Or, print the data in nodes *while* the node's pointer is *not* -1.

For clarity and testing purposes, I also printed the node's pointer along with its data.

{{< highlight python "linenos=inline, style=arduino" >}}
def output_nodes(ll, current_pointer):
    while current_pointer != -1:
        print(ll[current_pointer].data, " points to index", ll[current_pointer].next_node)
        current_pointer = ll[current_pointer].next_node
{{< /highlight >}}

# 3. Write a function that adds a node to the linked list

Here's the logic:
1. check if there is a free space available
2. find the "last" node (a.k.a. the *linked* node that points to a -1)
3. make this "last" node point to the free space
4. insert value at the free space
5. update the "empty_list" pointer to point to the next available free space

The question also wants us to return True if there is a free space and False if there isn't.

Being new to linked lists, I found this rather tricky! But here's the solution I found:

{{< highlight python "linenos=inline, style=arduino" >}}
def add_node(ll, current_pointer, input_data):
  # ll is short for linked list
  global empty_list

  # check if there is a free space available
  if ll[empty_list].data == 0:
    for node in ll:
      # make the "last" node point to the empty space if it points to -1 
      if node.next_node == -1:
        node.next_node = empty_list
        break
        
    # add data to the free space and make it point to -1
    ll[empty_list].data = input_data
    ll[empty_list].next_node = -1

    # determine the next free space
    for i in range(len(ll)):
      if ll[i].data == 0:
        empty_list = i
        break

    return True
  else:
    return False
{{< /highlight >}}

# Testing

We'll add 5 items to the linked list (even though there are only 4 free spaces) and then run `output_nodes()`.
{{< highlight python "linenos=inline, style=arduino" >}}
print(add_node(linked_list, start_pointer, 5))
print(add_node(linked_list, start_pointer, 6))
print(add_node(linked_list, start_pointer, 7))
print(add_node(linked_list, start_pointer, 8))
print(add_node(linked_list, start_pointer, 9))
output_nodes(linked_list, start_pointer)
{{< /highlight >}}

Here's the output I got:
{{< highlight bash "linenos=inline, style=arduino" >}}
True
True
True
True
False
1 points to index 1
5 points to index 4
2 points to index 2
6 points to index 7
56 points to index 3
7 points to index 5
5 points to index 6
6 points to index 8
7 points to index 9
8 points to index -1
{{< /highlight >}}

We can see that 9 wasn't added to the list!

# Conclusion

I did NOT like this question for the reasons I stated in the first section, but being new to linked lists and after having bashed my head against the wall for a while, I'm happy I was able to do this!
