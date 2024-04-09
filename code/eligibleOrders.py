class DLL:
    def __init__(self, index=None, val=None):
        self.index = index
        self.val = val
        self.prev = None
        self.next = None
        
class Eligible:
    def __init__(self):
        self.head, self.tail = DLL(), DLL()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def addToEnd(self, node):
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        
        node.next = self.tail
        self.tail.prev = node
    
    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def isPeak(self, node):
        if node.prev != self.head and node.prev.val > node.val:
            return False
        if node.next != self.tail and node.next.val > node.val:
            return False
        return True
        

    def processOrders(self, orders):
        orderMap = defaultdict(DLL)
        heap = []

        for index, order in enumerate(orders):
            node = DLL(index, order)
            self.addToEnd(node)
            orderMap[index] = node

        
        for i in range(len(orders)):
            if(self.isPeak(orderMap[i])):
                heappush(heap, (orderMap[i].val, i))
        
        res = []
        seen = set()
        while heap:
            val, index = heappop(heap)
            if index in seen:
                continue
            res.append(val)
            seen.add(index)
            
            node = orderMap[index]
            del orderMap[index]
            self.deleteNode(node)
            
            if node.prev != self.head and self.isPeak(node.prev):
                heappush(heap, (node.prev.val, node.prev.index))
            if node.next != self.tail and self.isPeak(node.next):
                heappush(heap, (node.next.val, node.next.index))
        
        return res
            
eligible = Eligible()
initial_orders = [30,10,70,40,20,50,15,16]
print("input: ", initial_orders)
process_sequence = eligible.processOrders(initial_orders)
print("expected:",[16, 30, 50, 70, 40, 20, 15, 10])
print("output: ", process_sequence)

print([30,10,50,40,20,70,15,16],"\n", eligible.processOrders([30,10,50,40,20,70,15,16]))



## WITHOUT DOUBLE LINKED LIST

def process(orders: [int]):
    orders = [float('-inf')] + orders + [float('-inf')]
    
    def isPeak(orderId):
        left, right = neighbors[orderId]
        return orderId > left and orderId > right
    
    neighbors = dict()
    heap = []
    for i in range(1, len(orders) - 1):
        neighbors[orders[i]] = [orders[i-1], orders[i+1]]
        if isPeak(orders[i]):
            heappush(heap, orders[i])
    
    res = []
    while heap:
        order = heappop(heap)
        res.append(order)
        
        left, right = neighbors[order]
        if left != float('-inf'):
            neighbors[left][1] = right
            if isPeak(left):
                heappush(heap, left)
        if right != float('-inf'):
            neighbors[right][0] = left
            if isPeak(right):
                heappush(heap, right)
        
        del neighbors[order]
    
    return res

# --------- driver code ---------
tests = [
    ([3,1,5,4,2], [3,5,4,2,1]),
    ([30,10,70,40,20,50,15,16], [16,30,50,70,40,20,15,10]),
    ([30,10,50,40,20,70,15,16], [16,30,50,40,70,20,15,10])
]

for orders, expected in tests:
    print('actual = {} | expected = {}'.format(process(orders), expected))