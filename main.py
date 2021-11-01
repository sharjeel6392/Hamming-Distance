class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bitx = bin(x).replace("0b","")
        bity = bin(y).replace("0b","")
        lenX = len(bitx)
        lenY = len(bity)
        if lenX < lenY:
            bitx = "0"*(lenY-lenX) + bitx

        elif lenY < lenX:
            bity = "0"*(lenX-lenY) + bity
         
        length = len(bitx)
        count = 0
        for i in range(length):
            if (bool(int(bitx[i])) ^ bool(int(bity[i]))):
                count += 1
                
        return count
