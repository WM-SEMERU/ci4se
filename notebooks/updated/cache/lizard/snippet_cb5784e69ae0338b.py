def binaryTree_depthFirstNumbers(binaryTree, labelTree=True, dontStopAtID=True
    ):
    traversalIDs = {}

    def traverse(binaryTree, mid=0, leafNo=0):
        if binaryTree.internal and (dontStopAtID or binaryTree.iD is None):
            midStart = mid
            j, leafNo = traverse(binaryTree.left, mid, leafNo)
            mid = j
            j, leafNo = traverse(binaryTree.right, j + 1, leafNo)
            traversalIDs[binaryTree] = TraversalID(midStart, mid, j)
            return j, leafNo
        traversalID = TraversalID(mid, mid, mid + 1)
        traversalID.leafNo = leafNo
        traversalIDs[binaryTree] = traversalID
        return mid + 1, leafNo + 1
    traverse(binaryTree)
    if labelTree:
        for binaryTree in traversalIDs.keys():
            binaryTree.traversalID = traversalIDs[binaryTree]
    return traversalIDs