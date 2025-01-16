
import matplotlib.pyplot as plt
from vectors import Vector


class Solar_System:
    
    def __init__(self, size):
        
        self.size = size
        self.bodies = []
        
        
    def initialise_figure(self):
        
        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize=(self.size / 50, self.size / 50),
        )
        self.fig.tight_layout()
        
        
    
    def add_body(self, body):
        self.bodies.append(body)
        
        
        
        

class SolarSystemBody:
    
    def __init__(self, 
                  solarsystem, 
                  mass, 
                  position=(0,0,0), 
                  velocity=(0,0,0)):
        self.solarsystem = solarsystem
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        
        self.solarsystem.add_body(self)
        
        
    
    def move_body():
        self.position = (self.position[0] + self.velocity[0],
                         self.position[0] + self.velocity[0],
                         self.position[0] + self.velocity[0])
        
        
        