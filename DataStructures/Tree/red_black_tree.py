from DataStructures.Tree import rbt_node as rbt

def put(my_rbt, key, val):
    my_rbt['root'] = rbt.insert_node(my_rbt['root'], key, value)
    return my_rbt