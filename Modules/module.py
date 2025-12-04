##normal way of importing
import my_module
print(my_module.a)
print(my_module.area_of_square(4))
 



 ##importing with a custom name
import my_module as m
print(m.a)
print(m.area_of_square(4))





##importing specific functions
from my_module import calculator, a, area_of_square
print(a)
print(area_of_square(4))
calculator(3, 2)