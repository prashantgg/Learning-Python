class Train:
    train_name = "Indian Railways"

    def __init__(self, fare, seats) :
        self.fare = fare
        self.seats = seats

    def bookTicket(self):
        if self.seats>0:
            print (f"The seat is booked in {self.train_name}")
            self.seats = self.seats-1
        else:
            print ("Sorry the seat is not available")
        
    def getStatus(self):
        print (f"The no of seats available in {rail.train_name} is {self.seats}")

    def getFareInfo(self):
        print (f"The price of seat in {rail.train_name} is {self.fare}")

    
    def cancelTicket(self, seatNo):
        pass

 
rail = Train(20,2)
rail.bookTicket()
rail.getStatus()
rail.getFareInfo()
rail.bookTicket()
rail.getStatus()
rail.bookTicket()
rail.getStatus()
