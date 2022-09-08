import random
import queue


# ............................................................................
#                                 N O D E
# ............................................................................

class Node:
    def __init__(self, key, SR):
        self.left = None
        self.right = None
        self.key = key
        self.xcoord = -1
        self.tag = ' '  # one character
        self.SR = SR

    def print(self):
        print("[" + str(self.key) + "]", end="")
        print(str(self.xcoord) + ", ", end="")


# ............................................................................
#                         B I N A R Y   T R E E
# ............................................................................


class BinaryTree:

    # ........................................................................
    #   C O N S T R U C T O R
    def __init__(self, key, SR):
        # super().__init__(key, SR)
        self.root = Node(key, SR)
        self.sum_of_costs = 0
        self.parity_counter = 0
        self.weakly_dominant_counter = 0
        self.l1_tree_counter = 0

        ########
        self.routes = []

    def binaryTree(self, node, depth, rule):
        AL = rule[0]
        AR = rule[1]
        C0 = rule[2]
        CL = rule[3]
        CR = rule[4]
        D = rule[5]
        M = rule[6]
        RK = rule[7]
        RSR = rule[8]

        if depth <= 0 or node.SR < C0:
            self.sum_of_costs += node.key * (D - depth + 1)
            return node

        if C0 <= node.SR < CL:
            key_left = AL * (node.key + 1) % M
            childNode_left_SR = (node.SR * AL) % M
            childNode = Node(key_left, childNode_left_SR)
            childNode.SR = (node.SR * AL) % M
            node.left = self.binaryTree(childNode, depth - 1, rule)
            self.sum_of_costs += node.key * (D - depth + 1)

        if CL <= node.SR < CR:
            key_right = AR * (node.key + 2) % M
            childNode_right_SR = (node.SR * AR) % M
            childNode = Node(key_right, childNode_right_SR)
            childNode.SR = (node.SR * AR) % M
            node.right = self.binaryTree(childNode, depth - 1, rule)
            self.sum_of_costs += node.key * (D - depth + 1)

        if CR <= node.SR < M:
            key_left = AL * (node.key + 1) % M
            key_right = AR * (node.key + 2) % M
            childNode_left_SR = (node.SR * AL) % M
            childNode_right_SR = (node.SR * AR) % M
            childNode_left = Node(key_left, childNode_left_SR)
            childNode_right = Node(key_right, childNode_right_SR)

            node.left = self.binaryTree(childNode_left, depth - 1, rule)
            node.right = self.binaryTree(childNode_right, depth - 1, rule)
            self.sum_of_costs += node.key * (D - depth + 1)

        return node

    # ........................................................................
    #   S E R V I C E   M E T H O D S    (mainly printing)
    def countNodes(self, node):
        if node == None: return 0
        return 1 + self.countNodes(node.left) + self.countNodes(node.right)

    # calculates x coord = node order of in Inorder traversal
    def setXcoord(self, node, x_coord):
        if node == None: return x_coord
        node.xcoord = self.setXcoord(node.left, x_coord) + 1
        # print(node.key, node.setXcoord)
        return self.setXcoord(node.right, node.xcoord)

    def display(self):
        self.setXcoord(self.root, 0)
        qu = queue.Queue()
        prevDepth = -1
        prevEndX = -1
        # in the queue store pairs(node, its depth)
        qu.put((self.root, 0))
        while not qu.empty():
            node, nodeDepth = qu.get()

            LbranchSize = RbranchSize = 0
            if node.left != None:
                LbranchSize = (node.xcoord - node.left.xcoord)
                qu.put((node.left, nodeDepth + 1))
            if node.right != None:
                RbranchSize = (node.right.xcoord - node.xcoord)
                qu.put((node.right, nodeDepth + 1))

            LspacesSize = (node.xcoord - LbranchSize) - 1  # if first on a line
            if prevDepth == nodeDepth:  # not first on line
                LspacesSize -= prevEndX

            # print the node, branches, leading spaces
            if prevDepth < nodeDepth and prevDepth > -1: print()  # next depth occupies new line
            nodelen = 3
            print(" " * nodelen * LspacesSize, end='')
            print("_" * nodelen * LbranchSize, end='')
            # print( "." + ("%2d"%node.key) + node.tag+".", end = '' )
            print(node.tag + ("%2d" % node.key), end='')
            print("_" * nodelen * RbranchSize, end='')

            # used in the next run of the loop:
            prevEndX = node.xcoord + RbranchSize
            prevDepth = nodeDepth
        # end of queue processing

        N = self.countNodes(self.root)
        print("\n" + '-' * N * nodelen)  # finish the last line of the tree

    # task 2
    def sum_of_nodes(self, node):
        if node is not None:
            if node.left:
                left_sum = self.sum_of_nodes(node.left)
            else:
                left_sum = 0

            if node.right is not None:
                right_sum = self.sum_of_nodes(node.right)
            else:
                right_sum = 0

            summ = node.key + left_sum + right_sum

        else:
            summ = 0

        return summ

    def sum_disbalances(self, node):
        elements = []
        if node.left:
            elements += self.sum_disbalances(node.left)

        if node.right:
            elements += self.sum_disbalances(node.right)

        lsum = self.sum_of_nodes(node.left)
        rsum = self.sum_of_nodes(node.right)
        elements.append(abs(lsum - rsum))

        return elements

    # task 3
    def in_left_tree(self, node):
        elements = []

        if node is None:
            elements.append(1)
            return elements

        if node.left:
            elements += self.in_left_tree(node.left)

        if node.right:
            elements += self.in_left_tree(node.right)

        if node.left and node.right or node.left is None and node.right is None:
            elements.append(1)

        # if node.right is None:
        #     elements.append(1)

        return elements

    def in_right_tree(self, node):
        elements = []

        if node is None:
            elements.append(1)
            return elements

        if node.left:
            elements += self.in_right_tree(node.left)

        if node.right:
            elements += self.in_right_tree(node.right)

        if node.left and node.right or node.left is None and node.right is None:
            elements.append(1)

        return elements

    def two_balanced_node(self, node):
        elements = []
        if node.left:
            elements += self.two_balanced_node(node.left)

        if node.right:
            elements += self.two_balanced_node(node.right)

        if node.left is None and node.right is None:
            elements.append(node.key)

        else:
            l_tree = self.in_left_tree(node.left)
            r_tree = self.in_right_tree(node.right)

            if l_tree is not None and r_tree is not None:
                if len(l_tree) == len(r_tree):
                    elements.append(node.key)

        return elements

    # task 4
    def parity_siblings(self, node):
        elements = []
        if node.left:
            elements += self.parity_siblings(node.left)

        if node.right:
            elements += self.parity_siblings(node.right)

        if node.left is not None and node.right is not None:
            l_parity = node.left.key % 2
            r_parity = node.right.key % 2
            if l_parity == r_parity:
                elements.append(node.key)
                self.parity_counter += 1
        if node.left is None and node.right is None:
            pass

        return elements

    # task 5
    def find_min(self, node):
        elements = []

        elements.append(node.key)

        if node.left:
            elements += self.find_min(node.left)

        if node.right:
            elements += self.find_min(node.right)

        return elements

    def locally_minimum(self, node):
        elements = []
        if node.left:
            elements += self.locally_minimum(node.left)

        if node.right:
            elements += self.locally_minimum(node.right)

        min_array = self.find_min(node)

        if min_array[0] == min(min_array):
            elements.append(min_array[0])

        return elements

    # task 6
    def find_leaves(self, node):
        elements = []
        if node.left:
            elements += self.find_leaves(node.left)

        if node.right:
            elements += self.find_leaves(node.right)

        if node.left is None and node.right is None:
            elements.append(node.key)


        return elements

    def weakly_dominant(self, node):
        elements = []
        if node.left:
            elements += self.weakly_dominant(node.left)

        if node.right:
            elements += self.weakly_dominant(node.right)


        if node.left is None and node.right is None:
            pass
        else:
            leaves = self.find_leaves(node)
            if len(leaves) > 0:
                if node.key >= min(leaves):
                    elements.append(node.key)
                    self.weakly_dominant_counter += 1

        return elements

    # task 7
    def check_left_only(self, node):
        elements = []

        if node.left:
            elements += self.check_left_only(node.left)

        if node.right:
            elements += self.check_left_only(node.right)

        if node.left is None and node.right is None:
            pass
        else:
            if node.left and node.right is None:
                if 0 in elements:
                    elements.append(0)
                else:
                    elements.append(1)
                    # elements.append(node.key)
            if node.left is None and node.right:
                elements.append(0)

        return elements

    def l1_tree(self, node):
        elements = []
        if node.left:
            elements += self.l1_tree(node.left)

        if node.right:
            elements += self.l1_tree(node.right)

        mid = self.check_left_only(node)

        if 0 in mid or len(mid) == 0:
            pass
        else:
            elements.append(1)

        return elements

    # task 8
    def find_routes(self, node, route):
        if node is None:
            return

        route.append(node.key)

        self.routes.append(list(route))

        self.find_routes(node.left, route)
        self.find_routes(node.right, route)

        route.pop()

    def all_routes(self, node):
        route = []

        if node is None:
            return
        t.find_routes(node, route)
        t.all_routes(node.left)
        t.all_routes(node.right)


# ............................................................................
#                M A I N   P R O G R A M
# ............................................................................

if __name__ == '__main__':
    # the_rule = [12, 13, 2, 8, 12, 4, 20, 9, 12]
    # the_rule = [11, 12, 7, 15, 23, 5, 31, 28, 26]
    # the_rule =[12, 13, 3, 10, 16, 6, 29, 18, 16]

    user_input = input()
    rule_temp = user_input.split()
    the_rule = list(map(int, rule_temp))

    AL = the_rule[0]
    AR = the_rule[1]
    C0 = the_rule[2]
    CL = the_rule[3]
    CR = the_rule[4]
    D = the_rule[5]
    M = the_rule[6]
    RK = the_rule[7]
    RSR = the_rule[8]

    #####################################
    t = BinaryTree(RK, RSR)
    # create the tree with maximum depth D
    t.binaryTree(t.root, D, the_rule)
    # display the created tree
    # t.display()
    ######################################

    # task 1
    print(t.sum_of_costs)

    # task 2
    elements_to_sum = t.sum_disbalances(t.root)
    # print(elements_to_sum)
    print(sum(elements_to_sum))

    # task 3
    # print(t.two_balanced_node(t.root))
    sum_of_2_balanced_nodes = sum(t.two_balanced_node(t.root))
    print(sum_of_2_balanced_nodes)

    # task 4
    # print(t.parity_siblings(t.root))
    t.parity_siblings(t.root)
    print(t.parity_counter)

    # task 5
    sum_of_locally_minimal = sum(t.locally_minimum(t.root))
    print(sum_of_locally_minimal)

    # task 6  ## the answer is coming out to be INCORRECT for some reason
    t.weakly_dominant(t.root)
    # print(t.weakly_dominant(t.root))
    print(t.weakly_dominant_counter)

    # task 7
    number_of_l1_trees = sum(t.l1_tree(t.root))
    # print(t.l1_tree(t.root))
    print(number_of_l1_trees)

    # task 8
    t.all_routes(t.root)
    mid = []
    for route1 in t.routes:
        if len(route1) >= 2:
            if route1 == sorted(route1):
                mid.append(sum(route1))
    print(max(mid))
