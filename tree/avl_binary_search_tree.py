from binary_tree import NodeBT, BinaryTree


class NodeAVL(NodeBT):
    def __init__(self, value=None, height=1):
        self.value = value
        self.height = height  # 높이(height)는 +1로 계산한다.
        self.left = None
        self.right = None

    def insert(self, value):
        # 1) 이진 탐색 트리 노드 삽입
        new_node = NodeAVL(value)
        if value < self.value:
            self.left = self.left and self.left.insert(value) \
                or new_node
        elif value > self.value:
            self.right = self.right and self.right.insert(value) \
                or new_node
        else:
            raise Exception("중복 노드를 허용하지 않습니다.")

        # 회전 메서드에서 높이를 설정한다.
        return self.rotate(value)

    def rotate(self, value):
        # 2) (조상) 노드의 높이를 갱신한다.
        self.height = 1 + max(self.get_height(self.left),
                              self.get_height(self.right))

        # 3) 균형도(왼쪽 트리 높이 - 오른쪽 트리 높이)
        balance = self.get_balance()

        # 4) 트리의 균형이 맞지 않을 경우 회전한다.
        if balance > 1:
            # [케이스 1] LL - Left Left
            if value < self.left.value:
                return self.right_rotate()

            # [케이스 2] LR - Left Right
            elif value > self.left.value:
                self.left = self.left.left_rotate()
                return self.right_rotate()

        elif balance < -1:
            # [케이스 3] RR - Right Right
            if value > self.right.value:
                return self.left_rotate()

            # [케이스 4] RL - Right Left
            elif value < self.right.value:
                self.right = self.right.right_rotate()
                return self.left_rotate()

        return self

    def left_rotate(self):
        """
        여기서 self는 y다.
               x                  [y]
             /   \               /   \
            y     T3   <----    T1    x
           / \       (왼쪽 회전)     / \
          T1  T2                    T2  T3
        """
        x = self.right
        T2 = x.left

        # 회전한 후,
        x.left = self
        self.right = T2

        # 높이를 갱신한다.
        self.height = 1 + max(self.get_height(self.left),
                              self.get_height(self.right))
        x.height = 1 + max(self.get_height(x.left),
                           self.get_height(x.right))

        # 새 루트 노드를 반환한다.
        return x

    def right_rotate(self):
        """
        여기서 self는 x다.
              [x]                    y
             /   \                 /   \
            y     T3    ---->     T1    x
           / \       (오른쪽 회전)     / \
          T1  T2                      T2  T3
        """
        y = self.left
        T2 = y.right

        y.right = self
        self.left = T2

        self.height = 1 + max(self.get_height(self.left),
                              self.get_height(self.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def get_height(self, node):
        if not node:
            return 0

        return node.height

    def get_balance(self):
        return self.get_height(self.left) - self.get_height(self.right)

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node

        return self.get_min_value_node(node.left)

    def delete(self, value):
        # 1) 이진 탐색 트리 노드 삭제
        if value < self.value:
            self.left = self.left and self.left.delete(value)
        elif value > self.value:
            self.right = self.right and self.right.delete(value)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            temp = self.get_min_value_node(self.right)
            self.value = temp.value
            self.right = self.right and self.right.delete(temp.value)

        if self is None:
            return None

        return self.rotate(value)


class AVLTree(BinaryTree):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = NodeAVL(value)
        else:
            self.root = self.root.insert(value)

    def delete(self, value):
        self.root = self.root.delete(value)


def preorder(root):
    if root:
        print("({0}, {1}) ".format(root.value, root.height-1), end="")
        if root.left:
            preorder(root.left)
        if root.right:
            preorder(root.right)


if __name__ == "__main__":
    myTree = AVLTree()
    for i in range(10, 100, 10):
        myTree.insert(i)

    print("트리의 높이는? ", myTree.get_height())
    print("이진 탐색 트리입니까? ", myTree.is_bst())
    print("균형 트리입니까? ", myTree.is_balanced())
    preorder(myTree.root)
    print()