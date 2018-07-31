def get_cheapest_cost(rootNode):
    #If root node has no children, return root node cost as the cheapest cost
    n = len(rootNode.children)
    if n == 0:
        return rootNode.cost
    else:
        #set variable to biggest possible input
        least_cost = 10000
        for child_node in rootNode.children:
            #storage will keep track of the total sum of each branch
            storage = 0
            #store total sum of a branch in temp_value
            temp_value = recursive_calculate(child_node, storage, least_cost)
            #compare value of branch to least_cost, store the lesser value
            least_cost = min(least_cost, temp_value)
        return least_cost + rootNode.cost


def recursive_calculate(child, storage, least_cost):
    #keep adding the node's cost to storage as we go deeper in a branch
    storage += child.cost
    #if no more children, we've reached the end of the branch, so return storage
    if len(child.children)  == 0:
        return storage
    else:
        #If node has children, keep going deeper
        for x in child.children:
            #store total sum of the sub-branch in temp_storage
            temp_storage = recursive_calculate(x, storage, least_cost)
            #store the lesser of the two values
            least_cost = min(least_cost, temp_storage)
        return least_cost

# A Constructor to create a new node
class Node(object):
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
 



node_a = Node(0)
node_b = Node(5)
node_c = Node(4)
node_d = Node(3)
node_e = Node(0)
node_f = Node(10)
node_g = Node(2)
node_h = Node(1)
node_i = Node(1)
node_j = Node(6)
node_k = Node(1)
node_l = Node(5)

node_a.children.append(node_b)
node_a.children.append(node_d)
node_a.children.append(node_j)

node_b.children.append(node_c)

node_d.children.append(node_e)
node_d.children.append(node_g)

node_j.children.append(node_k)
node_j.children.append(node_l)

node_e.children.append(node_f)

node_g.children.append(node_h)

node_h.children.append(node_i)
                        
#Should return 7
print(get_cheapest_cost(node_a))




