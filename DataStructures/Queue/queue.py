from DataStructures.List import single_linked_list as sl

def new_queue():
    return sl.new_list()

def is_empty(queue):
    return sl.is_empty(queue)

def size(queue):
    return sl.size(queue)

def enqueue(queue, element):
    queue = sl.add_last(queue, element)
    return queue

def dequeue(queue):
    queue = sl.remove_first(queue)
    return queue

def peek(queue):
    return sl.get_element(queue, 0)

