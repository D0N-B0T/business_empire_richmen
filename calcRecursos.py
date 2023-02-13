pbuilders = 2650
pmetal = 1171
pwood = 324
pconcrete = 47
    
# cantidad de recursos para privatehouse
nbuilders =  4
nmetal = 4
nwood = 50
nconcrete = 170 

def privateHouse():
    return nbuilders*pbuilders + nmetal*pmetal + nwood*pwood + nconcrete*pconcrete

def calculadora(budget):
    ronda = 0
    while budget > 0:
        budget = budget - privateHouse()
        ronda = ronda + 1
        
        co = 0
        bui = 0
        me = 0
        woo = 0
        for i in range(ronda):
            co = co + 170
            bui = bui + 4
            me = me + 4
            woo = woo + 50
            
            
        if budget <= 39474:
            print("N° casas: ", ronda)
            print("Dinero sobrante: ", budget)
            print("\nMateriales a comprar::\nConcreto: ", co, "\nBuilders: ", bui, "\nMetal: ", me, "\nWood: ", woo, "\n")
            break

        

    
calculadora(2624360)


    
