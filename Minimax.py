class Minimax:
    def __init__(self, nimState, minMaxLevel):
        self.state=nimState
        self.level=minMaxLevel
        self.child=None
        self.sibling=None
        

def build_tree(parent_node):

    current_node = parent_node
    index = 0
    for j in parent_node.state:
    
        i = j

        if i > 2:

            while i > j//2+1:
              
              i -=1 

              if i == j-1:

                  new = list(parent_node.state)

                  new.pop(index)

                  new += [i,j-i]

                  current_child = Minimax(sorted(new),'')

                  current_node.child = current_child  

                  print('parent: %d  child: '%(j)+str(current_child.state))

                  build_tree(current_child)

                  current_node = current_child 


              else :

                  new = list(parent_node.state)

                  new.pop(index)

                  new += [i,j-i]

                  siblings_node = Minimax(sorted(new),'')

                  current_node.sibling = siblings_node

                  print('parent: %d  sibling_child: '%(j) +str(siblings_node.state))

                  build_tree(siblings_node)

                  current_node = siblings_node

        index+=1



def printTree(indentation, last, node):
    print(indentation,end="")
    if last:
        print ('\-',end="")
        indentation += "  "
    else:
        print('+',end="")
        indentation += "| "

    print (node.state,end="")
    if last:
        print(node.level,end="")

    current_node = node.child

    while current_node!=None:

            last = False

            print("")

            if current_node.sibling == None:
                last = True
            
            printTree(indentation,last,current_node)

            current_node = current_node.sibling


def main():


    number = input('Please enter a number: ')
    
    minOrmax = input('Please enter min or max: ')

    root = Minimax([int(number)],minOrmax)
    
    build_tree(root)

    printTree("",True,root)

    print ("")




main()

