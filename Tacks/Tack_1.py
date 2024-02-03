class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def reverse_list(self):
    prev = None
    current = self.head
    while current:
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev

  def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list

  def sorted_insert(self, sorted_list, new_node):
        if sorted_list is None or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            return new_node

        current = sorted_list
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return sorted_list  
  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged_list = LinkedList()

    # Merge the two lists into a single list
    current_list1 = list1.head
    current_list2 = list2.head

    while current_list1 or current_list2:
        if current_list1 and current_list2:
            if current_list1.data < current_list2.data:
                merged_list.insert_at_end(current_list1.data)
                current_list1 = current_list1.next
            else:
                merged_list.insert_at_end(current_list2.data)
                current_list2 = current_list2.next
        elif current_list1:
            merged_list.insert_at_end(current_list1.data)
            current_list1 = current_list1.next
        elif current_list2:
            merged_list.insert_at_end(current_list2.data)
            current_list2 = current_list2.next

    # Perform insertion sort on the merged list
    merged_list.insertion_sort()

    return merged_list



if __name__ =="__main__":
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()
    


    print("\nПідзавдання №1 реверсування списку:")
    llist.reverse_list()
    llist.print_list() 
    
    print("\nПідзавдання №2 сортування списку:")
    llist.insertion_sort()
    llist.print_list()
    
    
    llist2 = LinkedList()
    llist2.insert_at_end(22)
    llist2.insert_at_end(4)
    llist2.insert_at_end(0)
    llist2.insert_at_end(2)            

    print("Другий список:")
    llist2.print_list()

    merged_list = merge_sorted_lists(llist, llist2)

    print("Підзавдання №3 Об'єднаний відсортований список:")
    merged_list.print_list()    
