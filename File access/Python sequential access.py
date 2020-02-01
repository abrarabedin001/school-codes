import pickle
class CarRecord:
 # dec l ar i ng a class wi t h out othe r methods
    def __init__(self) :
         # constructor
        self.VehicleID = ""
        self.Registration= " "
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.PurchasePrice = 0.00


Car = [""] * 100
for r in range(100):
    Car[r] = CarRecord()

for r in range(100):
    Car[r].Registration= str(r)+"Registration"
    print(Car[r].Registration)


CarFile = open( 'Cars.DAT','wb') # open file for binary write
for i in range (100): # loop for each array element
    print(Car[i].Registration)
    pickle.dump (Car[i], CarFile) # write a whole record to the binary file

CarFile.close()
 # close file
CarFile = open ( 'Cars.DAT','rb')
 # open file for binary read
Car = []
 # start with empty list
while True:
 # check for end of file
    try:
        Car.append (pickle.load(CarFile) )
    except:
        print("life is fun")
        break
 # append record from file to end of list
CarFile. close ()

print(Car[1].Registration)
