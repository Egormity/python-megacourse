import pandas as pd

PATH = r"C:\Users\kotla\Desktop\python-megacourse\012-hotel-booking\hotels.csv"
df = pd.read_csv(PATH)

class Hotel:
    #
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    
    # 
    def is_available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        return availability == "yes"
    
    # 
    def book(self):
        if self.is_available():
            df.loc[df["id"] == self.hotel_id, "available"] = "no"
            df.to_csv(PATH, index=False)

    # 
    def view(self):
        pass

class ReservationTicket:
    # 
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object

    # 
    def generate(self):
        return f"""
        Generated reservation ticket:
        Customer name: {self.customer_name}
        Hotel name: {self.hotel_object.name}
        Check-in date: TODO:
        Check-out date: TODO:
        """

if __name__ == "__main__":
    print(df)

    hotel_id = input("Enter hotel id to book: ")
    hotel = Hotel(int(hotel_id))

    if hotel.is_available():
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(name, hotel)
        reservation_ticket.generate()
    else:
        print(f"Hotel {hotel_id} is not available")
