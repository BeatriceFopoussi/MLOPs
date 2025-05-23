#! ==================== IMPORTS ====================
import os
import sys
import time
import random
import math
import pygame
import pandas as pd

# ==================== CLASS ====================

# %% 
class dog:
    pass

# %%
# ==================== INSTANCES/OBJECTS ====================
# %%  
name_dog = dog()
type(name_dog)

# § ==================== Attributs ====================

# %%
class dog:
    def __init__(self, name,race):
        self.name = name
        self.race = race

name_dog=dog("pipo","labrador")
print(name_dog.name)
print(name_dog.race)

# %%
# ==================== Methode ====================

# %%
class dog:
    def __init__(self, name, race):
        self.name = name
        self.race= race
    def bark(self):
        print(f"{self.name} bark!")


# %%
rex=dog("Rex","berger")
print(rex.bark())
# %%
