class shirt_details:

    def __init__(self, brand, model, color, size, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.size = size
        self.price = price

    def getDetails(self):
        print("Brand : " + self.brand)
        print("Model : " + self.model)
        print("Color : " + self.color)
        print("Size : " + self.size)
        print("Price : " + self.price)

# Creating an instance of Shirt
shirt_1 = shirt_details("Lee", "Button Down", "Blue", "Large", "29.99")
shirt_2 = shirt_details("Levis", "T-Shirt", "Green", "X-Large", "24.99")


# Print the details of Shirt added
shirt_1.getDetails()
shirt_2.getDetails()
