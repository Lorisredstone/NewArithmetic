from __future__ import annotations
from src.Exceptions import *

class Number:
    def __init__(self:Number, value:int) -> None:
        self.value = value
        self.str_representation = str(value)
        self.numbers = set(self.str_representation)
    
    def __repr__(self:Number) -> str:
        return f"Number({self.value})"
    
    def __add__(self:Number, nb1:Number) -> Number:
        return Number(self.value + nb1.value)
    
    def __sub__(self:Number, nb1:Number) -> Number:
        computed_value = self.value - nb1.value
        if computed_value < 0:
            raise BelowZeroNotSupported(f"Subtraction result is below zero ({self.value} - {nb1.value} = {computed_value} < 0)")
        return Number(computed_value)
    
    def __eq__(self:Number, nb1:Number) -> bool:
        return self.value == nb1.value
    
    def __gt__(self:Number, nb1:Number) -> bool:
        if self.numbers.issubset({'8',}) and nb1.numbers.issubset({'8',}):
            return len(self.str_representation) > len(nb1.str_representation)
        if self.numbers.issubset({'8','1'}) and nb1.numbers.issubset({'8','1'}):
            
            return