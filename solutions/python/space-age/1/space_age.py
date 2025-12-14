class SpaceAge:
    def __init__(self, s):
        self.s = s

    def on_earth(self):
        s = self.s
        return round(s / 31557600, 2) 

    def on_mercury(self):
        s = self.s
        return round(s / (31557600 * 0.2408467), 2) 
    
    def on_venus(self):
        s = self.s
        return round(s / (31557600 * 0.61519726), 2) 

    def on_mars(self):
        s = self.s
        return round(s / (31557600 * 1.8808158), 2) 

    def on_jupiter(self):
        s = self.s
        return round(s / (31557600 * 11.862615), 2) 

    def on_saturn(self):
        s = self.s
        return round(s / (31557600 * 29.447498), 2) 

    def on_uranus(self):
        s = self.s
        return round(s / (31557600 * 84.016846), 2) 

    def on_neptune(self):
        s = self.s
        return round(s / (31557600 * 164.79132), 2) 



