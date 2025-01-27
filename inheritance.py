# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self._brand = brand  # Protected attribute
        self._model = model
        self._price = price

    def show_details(self):
        return f"{self._brand} {self._model} costs ${self._price}"

    def call(self, number):
        return f"Calling {number} using {self._brand} {self._model}..."

# Derived class: GamingSmartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, refresh_rate, cooling_system):
        super().__init__(brand, model, price)
        self.refresh_rate = refresh_rate
        self.cooling_system = cooling_system

    def show_details(self):
        base_details = super().show_details()
        return f"{base_details} with a refresh rate of {self.refresh_rate}Hz and {self.cooling_system} cooling system."

    def play_game(self, game_name):
        return f"Playing {game_name} on {self._brand} {self._model} at {self.refresh_rate}Hz."

# Example usage
phone = Smartphone("Apple", "iPhone 14", 999)
gaming_phone = GamingSmartphone("ASUS", "ROG Phone 7", 1199, 165, "Advanced Vapor Chamber")

print(phone.show_details())
print(phone.call("123-456-7890"))
print(gaming_phone.show_details())
print(gaming_phone.play_game("PUBG"))
