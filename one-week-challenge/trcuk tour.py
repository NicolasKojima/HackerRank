def truckTour(petrolpumps):
    tank = startingIndex = 0
    
    for i in range(len(petrolpumps)):
        tank += petrolpumps[i][0]
                
        if tank >= petrolpumps[i][1]:
            tank -= petrolpumps[i][1]
        else:
            tank = 0
            startingIndex = i + 1
    
    return startingIndex