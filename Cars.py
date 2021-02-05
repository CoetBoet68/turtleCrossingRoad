import car
from random import randint


class cars():
    maxCars = 3
    xDiffMin = -5
    xDiffMax = 3
    yMax = 250
    yMin = -200
    speedMin = 4
    speedMax = 11
    allCars = []

    def startLevel(self, max_cars):
        self.maxCars = max_cars
        for j in range(4):
            self.createBatch()
            for i in range(8):
                self.moveBatches()
                self.removeCars()

    def createBatch(self):
        carAmount = randint(1, self.maxCars)
        batchCars = []
        for i in range(carAmount):
            xDiff = randint(self.xDiffMin, self.xDiffMax)
            yValue = randint(self.yMin, self.yMax)
            speed = randint(self.speedMin, self.speedMax)
            batchCars.append(car.Car(xDiff, yValue, speed))
        self.allCars.append(batchCars)

    def moveBatches(self):
        for batch in self.allCars:
            for batchCar in batch:
                batchCar.move()

    def removeCars(self):
        batchesToDelete = []
        batchIndexesD = []
        for index, batch in enumerate(self.allCars):
            carCounter = 0
            carsToDelete = []
            carIndexesD = []
            for indexC, batchCar in enumerate(batch):
                carCounter += 1
                if batchCar.xPosition() < -300:
                    carsToDelete.append(batchCar)
                    carIndexesD.append(indexC)
            if carCounter == 0:
                batchesToDelete.append(batch)
                batchIndexesD.append(index)
            else:
                for dCars in carsToDelete:
                    dCars.deleteCar()
                    del dCars
                for i in range(len(carIndexesD)-1, -1, -1):
                    self.allCars[index].pop(carIndexesD[i])
        for dBatches in batchesToDelete:
            del dBatches
        for i in range(len(batchIndexesD) - 1, -1, -1):
            self.allCars.pop(batchIndexesD[i])

    def checkTurtleCrash(self,pPos):
        for batch in self.allCars:
            for batchCar in batch:
                if batchCar.tooClose(pPos):
                    return True
        return False

    def deleteAll(self):
        for batch in self.allCars:
            for batchCar in batch:
                batchCar.deleteCar()
        del self