class CircularListNode:
    def __init__(self, value):
        # Here we store the actual data or value in this node
        self.value = value

        # 'next_node', is an attribute of type pointer that will point to the next node in the list
        # Initially, when the  node is created, we don't know the next node, so we set it to None, or null
        self.next_node = None

        # Will also have 'previous_node', which is an attribute that will point to the previous node in the list
        # Initially, we set it to None, since Llist is empty at this point
        self.previous_node = None

class CircularDoublyLinkedList:
    def __init__(self):
        # We need to tell the compiler about the first chainlink, or the first node of our LList which is the head
        # Here in this code, the 'start_node' attribute will be our head and it will keep track of the first node in the list (the head)
        # If the list is empty, 'start_node' will be None
        self.start_node = None

    # Insert at the End 
    #       (this method will insert a new node with the given 'value' at the end of the circular doubly linked list)
    def insert_at_end(self, value):
        # First, create a new node object with the given value
        new_node = CircularListNode(value)
        # Secondly, check if the Llist is empty, where it is fulfilled by this condition:
        if self.start_node is None:
            #We only enter this block if the Llist is empty
            # Since the list is empty, this new node will be the only node in our list
            # Then, for a circular list, this node points to itself in both directions
            new_node.next_node = new_node # The next node after new_node is itself
            new_node.previous_node = new_node # The previous node before new_node is itself

            # We also need to update the start_node to point to this new node
            self.start_node = new_node
        else:
            # Here in the else clause, the list has items, so it's not empty so we need to add the new node at the end    
            # 'last_node' is the node that currently comes before the start_node,
            # Keep in mind that this is a Circular Boubly Linked List
            # We access it by following the 'previous_node' pointer of the start_node

# Now we have a special concept called Chained Attribute Access or Attribute Chaining.

            #Here it is: 'self.start_node.previous_node' means:
            # 1. 'self.start_node' gives us the first node in the list
            # 2. '.previous_node' accesses the node that comes before the start_node

            # In context:
# You're navigating object references through chained attributes - essentially, following links (pointers) between objects.
# In Data Structures (like linked Lists), this is also described as:
     # 1. Poiner Traversal in OOP.           
     # 2. Link following in node-based structures.
# So, self.start_node.previous_node is an example of pointer traversal via attribute chaining in a linked structure.

            # This works because the list is circular, so the node before the first node is the last node
            last_node = self.start_node.previous_node

            # Now we linkt he new_node into the list:
            # First, the current last_node's next_node should point to the new_node
            last_node.next_node = new_node

            # Secondly, the new_node's 'previous_node' should point back to the last_node
            new_node.previous_node =  last_node

            # Thirdly, the new_node's 'next_node' should point to the start_node to maintain circularity
            new_node.next_node = self.start_node

            # Lastly, the start_node's previous_node should now point to the new_node, which is the new last node
            self.start_node.previous_node = new_node

    # Insert at the Beginning
    #       (this method will insert a new node with the given 'value'-passed as a parameter- at the beginning of the circular doubly linked list)
    def insert_at_beginning(self, value):

        # To optimize our code, we are going to reuse the insert_at_end method to add the node at the end fist

        self.insert_at_end(value)

        # After adding the new node at the end, we move the start_node pointer backward to the new node
        # Here is the mark down;
            # 1. 'self.start_node' is currently the first node
            # 2. 'self.start_node.previous_node' is the node just added at the end
        # By setting start_node to start_node.previous_node, we simply make the new node the first node
        self.start_node = self.start_node.previous_node

    # Remove a given value from the Linked List
    #      (this method will remove the first node witht he specified value)
    def remove_value(self, value):     

        # If the list is empty, then we can't remove anything
        if self.start_node is None:
            print("The list is empty. Cannot remove any node.")
            return
        
        # If not, we start by searching from the start_node
        current_node = self.start_node

        # We will iterate through the LList until we come back to the start_node, since it's a circularly linked list
        while True:
            if current_node.value == value:

                # We only enter this block if we found the node to be removed

                # After finding the node to remove, there are a few cases we need to consider,
                # Case 1: If the node to remove is the only node in the list
                if current_node.next_node == current_node:
                    # Since it's the only node, removving it makes the list empty
                    self.start_node = None
                else:
                    # Case 2: If the list has multiple nodes
                    # So, in order to remove current_node, we need to announce our intentions to our neighbours, by updating their links

                    # Remember the pointer traversal via traversal chaining, in as that 'current_node.previous_node.next_node = current_node.next_node' means:
                    # -The node before current_node should now point forward to the node after current_node
                    current_node.previous_node.next_node = current_node.next_node

                    # 'current_node.next_node.previous_node = current_node.previous_node' implies that:
                    # -The node after after current_node should now point backward to the node before current_node
                    current_node.next_node.previous_node = current_node.previous_node

                    # If we are removing the start_node, move the start_node pointer forward
                    if current_node == self.start_node:
                        self.start_node = current_node.next_node

                    # By this point, the node is removed, and we can peacefully exit the method
                return
            #Move to the next node in the list
            current_node = current_node.next_node
            # If we by any chance have managed looped back to the start_node, it means the value is not in the list
            if current_node == self.start_node:
                print(f"Value {value} not found in the list.")
                break

     # Show list forwar-wise
     # (Dispaly the values of the nodes in the list starting from the start_node and moving forward)
    def show_list_forward(self):

        # We start by checking  if the list is empty, and if so, print a message and exit the method using return
        if self.start_node is None:
            print("The list is empty.")
            return
        
        # Set a temporary attribute to aid us loop by assigning it to the start_node
        current_node = self.start_node

        # Then we create an empty list to collect/ gather the string representations(which means we convert the strart part of the node to string) of node values
        values_list = []

        # Traverse through the Llist until we come back to the start_node
        while True:
            # Add the current node's value to the list as a string
            values_list.append(str(current_node.value)) # Here str() is an inbuilt method that converts a given value to a string

            # Then we do our incrementation here by utilizing the pointers
            current_node = current_node.next_node

            # We then check a condition where we have completed a full circle, and if so, we MAKE A STOP
            if current_node == self.start_node:
                break

                ## We can Format output, but it's not a must, however we shall do it otherwise, bcoz, why not?

        # Here's how to do it, we Join all the values in 'values_list' into a single string separated by ' -> '

        #Explanation of join inbuilt method:
        # - ' -> ' is a string separator
        # - '.join(values_list)' takes all elements in 'values_list' and concatenates them into one string,
        #   putting ' -> ' between each element
        #  For example, if values_list = ['5', '10', '15'], the result will be '5 -> 10 -> 15'    
        output_string = " -> ".join(values_list)

        # Print the resulting string to show the list contents
        print(output_string)

    # Show list backward
        # (Here we attempt to display the values of the nodes in the list starting form the last node and moving backward)
    def show_list_backward(self):

        # If the list is empty, print a message and exit the method via (return)
        if self.start_node is None:
            print("The list is empty.")
            return
        
        # Here, the last node is the one before the start_node (because the list is circular)
        last_node = self.start_node.previous_node
# If you're wondering why not store a self.last_node separately,
# it's because it adds redundancy and risk de-synchronization,
# Instead, just access what we need throught the links.

        # Now for the printing part, start from the last node
        current_node = last_node

        # Create an empty list to collect the string representations of node values
        values_list = []

        # Traverse the list backward until we come back to the last_node
        while True:
            # Add the current node's value to the list as a string
            values_list.append(str(current_node.value))

            # Move to the previous node
            current_node = current_node.previous_node

            # Stop if we have completed a full circle
            if current_node == last_node:
                break

        # Join all the values in 'values_list' into a single string separated by ' <- '
        # - ' <- ' is a our separator that now indicates backward direction
        # = .join(values_list)concatenates all elements in 'values_list' with ' <- ' between them
        # e.g if values_list = ['30', '20', '10'], the result will be '30 <- 20 <- 10'

        output_string = " <- ".join(values_list)

        # Print the resulting string to show the list contents backward
        print(output_string)

# First we prepped the ingredients and cooked the meal in the class definition, now it's time to taste it
#     (Inside the main block)        
if __name__ == '__main__':
    # Create a node by Instantiating the class via the creating of an object
    my_circular_list = CircularDoublyLinkedList()

    # Then insert values by calling the insertion method we created
    my_circular_list.insert_at_end("QUICK")
    my_circular_list.insert_at_end("BROWN")
    my_circular_list.insert_at_end("FOX") 

    print("List after inserting at the end:")
    # Call the print forward method
    my_circular_list.show_list_forward()

    my_circular_list.insert_at_beginning("THE")
    print("List after inserting at the beginning:")
    my_circular_list.show_list_forward()

    print("List diplayed backward:")
    my_circular_list.show_list_backward()

    my_circular_list.remove_by_value("QUICK")
    print("List after removing QUICK:")
    my_circular_list.show_list_forward()

    my_circular_list.remove_by_value("QUICK") # Not found
    my_circular_list.remove_by_value("SLOW") # Not found

    my_circular_list.remove_by_value("BROWN")
    print("List after removing BROWN:")
    my_circular_list.show_list_forward()

    # Attempting to empty the LList by removing the remaining elements
    my_circular_list.remove_by_value("THE")
    my_circular_list.remove_by_value("FOX")
    print("List after removing all:")

    my_circular_list.show_list_forward()

# N/B: A circular doubly linked list ensures that the last node links back to the first, and vice versa.
