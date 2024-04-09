def get_longest_valid_orders2(orders):
    seenPick, seenDel = {}, {}  # Track order status: (pickup_count, delivery_seen)
    longest_subarray = (0, 0)
    subLen = 0
    
    left, right = 0, 0
    
    while right < len(orders):
        order = orders[right]
        otype, onum = order[0], order[1:]
        if otype == "P":
            if onum not in seenPick:
                seenPick[onum] = right
                right += 1
            else:
                if onum in seenDel:
                    left = seenDel[onum] + 1
                    right = seenDel[onum] + 1
                else:
                    left = right
                seenDel, seenPick = {}, {}
        else:
            if onum not in seenPick:
                left = right + 1
                right += 1
                continue
            
            if onum not in seenDel:
                if isValid(orders, left, right):
                    if right - left + 1 > subLen:
                        subLen = right - left + 1
                        longest_subarray = (left, right)
                
                seenDel[onum] = right
                right += 1
            else:
                seenDel, seenPick = {}, {}
                left = right + 1
                right += 1
    
    for num in list(seenPick.keys()):
        if num not in seenDel:
            del seenPick[num]
    if len(seenPick) > 0 and len(seenPick) == len(seenDel):
        left = min(seenPick.values())
        right = max(seenDel.values())
        if right - left + 1 > subLen and isValid(orders, left, right):
            return orders[left: right + 1]
    
    return orders[longest_subarray[0]: longest_subarray[1] +1] if subLen > 0 else []
    
    
def isValid(orders, left, right):
    pick, deliv = set(), set()
    start = left
    while start <= right:
        order = orders[start]
        if order[0] == "P":
            if order[1:] in pick:
                return False
            pick.add(order[1:])
        else:
            if order[1:] not in pick or order[1:] in deliv:
                return False
            deliv.add(order[1:])
        start += 1
    
    return len(pick) == len(deliv)

print(" ")
# print(['P1', 'D1', 'P1', 'P2', 'P3', 'D1', 'D2', 'D3'])
print(get_longest_valid_orders2(['P1', 'D1', 'P1', 'P2', 'P3', 'D1', 'D2', 'D3']))
print(get_longest_valid_orders2(['P1', 'D1', 'P1', 'D1', 'P2', 'D2']))
print(get_longest_valid_orders2(['P1', 'P2', 'D1', 'P3', 'D2']))
print(get_longest_valid_orders2(['P1','P2','D2','D3']))
print(get_longest_valid_orders2(['P1','P2','D1','D2']))
print(get_longest_valid_orders2(['P1','P2','D2','D1']))
print(get_longest_valid_orders2(['P1','D2']))
print(get_longest_valid_orders2(['P1','D1', 'D1']))
print(get_longest_valid_orders2(['P1','D1', 'P1']))



