from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, wear):
        self.wear = wear

    def needs_service(self):
        return sum(self.wear) >= 3.0
