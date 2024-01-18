def create_an_empty_list():
    return []

def create_a_list():
   my_list = ["joe","kain","love","marisa"]
   return my_list

my_list = create_a_list()
print(my_list)


def add_element_to_end_of_list(l, mario):
    my_list.append(mario)
    return my_list


def add_element_to_start_of_list(l,luigi):
    my_list.insert( 0,luigi)
    return my_list

def remove_element_from_end_of_list(l):
    l.pop()
    return (l)


def remove_element_from_start_of_list(l):
    del l [0]
    return (l)

def retrieve_first_element_from_list(l):
    return l [0]

def retrieve_element_from_index(l,index):
    return l[index]


def retrieve_last_element_from_list(l):
    return l [-1]
