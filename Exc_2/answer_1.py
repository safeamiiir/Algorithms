number = int(input('Enter number of creators in OEX:\n'))
positions = [int(item) for item in input('Enter position of creators in OEX:\n').split(' ')]
speeds = [int(item) for item in input('Enter speed of creators in OEX:\n').split(' ')]
city = dict(zip(positions, speeds))
sortedCity = {k: v for k, v in sorted(city.items(), key=lambda item: item[0])}
cityArr = list(sortedCity.values())
opt = 0
for i, iValue in enumerate(cityArr):
    for j, jValue in enumerate(cityArr):
        if( i < j): # to check only after iValue
            if( iValue > jValue ):
                pass # DO Nothing
            else:
                opt += j - i
print(opt)