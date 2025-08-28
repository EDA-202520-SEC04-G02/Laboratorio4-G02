from DataStructures.List import single_linked_list as sl

def new_queue():
    """
    Crea una nueva cola
    """
    queue = sl.new_list()

    return queue

def enqueue(queue, element):
    """
    Agrega un elemento a la cola
    """
    sl.add_last(queue['elements'], element)
    queue['size'] += 1
    return queue
