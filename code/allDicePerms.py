class Dice:
    def __init__(self):
        pass
    
    def diceRolls(self, n):
        combs = []
        
        def backt(n, curr):
            if n == 0:
                combs.append(list(curr))
                return 
            
            for i in range(1, 7):
                curr.append(i)
                backt(n-1, curr)
                curr.pop()
        
        backt(n, [])
        return combs

dice = Dice()
print(dice.diceRolls(2))
print(" ")
print(dice.diceRolls(3))