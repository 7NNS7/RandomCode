'''
Returns all the dates in a year | list of strings
'''
def GenerateDates():
    year = [i for i in range(2010,2021)]
    month = [i for i in range(1,13)]
    day = [i for i in range(1,32)]
    dates = []
    for i in year:
        for j in month:
            for k in day :
                if (k > 28 and j == 2) or (k == 31 and j in [2,4,6,9,11]):
                    pass
                else:
                    dates.append(str(i)+"-"+str(j)+"-"+str(k))
    return dates