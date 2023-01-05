class Solution:
    def intToRoman(self, num: int) -> str:
        i=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        r=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        val=num
        p=len(i)-1
        rom=''
        while val!=0 and p>=0:
            if val-i[p]>=0:
                val=val-i[p]
                rom=rom+r[p]
            else:
                p=p-1
        return rom
            
        
        
        
        