# This is the library that will do the map and reduce
from mrjob.job import MRJob

#The class that does the task
class MaxTemperatures(MRJob):
    #The temperatures in this dataset is provided in 10th of a degree celsius
    def MakeFahrenheit(self, tenthsOfCelsius):
        celsius = float(tenthsOfCelsius) / 10.0
        fahrenheit = celsius * 1.8 + 32.0
        return fahrenheit
    
    def mapper(self, _, line):
        (location, _, mtype, data, _ , _ , _ , _ ) = line.split(',')
        if mtype == 'TMAX' :
            yield location, self.MakeFahrenheit(data)
            
    def reducer(self, location, data):
        yield location, max(data)
 
if __name__ == '__main__':       
    MaxTemperatures.run()
    
# run using: !python MaxTemperatures.py 1800.csv > MaxTempLocations.txt
