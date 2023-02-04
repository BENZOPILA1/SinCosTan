import math

# Запрашиваем у пользователя значения углов
angle1 = float(input("First angle: "))
angle2 = float(input("Second angle: "))

# Вычисляем синус, косинус, тангенс указанных углов
sin1 = math.sin(angle1)
cos1 = math.cos(angle1)
tan1 = math.tan(angle1)
sin2 = math.sin(angle2)
cos2 = math.cos(angle2)
tan2 = math.tan(angle2)

 # Вычисляем произведения соответствующих трigonomertricheskih funkciy po dannomu uglov:
proizv_sin_cos = sin1 * cos2   # Sin*Cos   (для 1-go i 2-go uglov)  
proizv_sin_tan = sin1 * tan2   # Sin*Tan   (для 1-go i 2-go uglov)  
proizv_cos_tan = cos1 * tan2   # Cos*Tan   (для 1-go i 2-go uglov)  

 # Выводим рeзyltat na ekran:  
print('Sin*Cos=', proizv_sin_cos)                    
print('Sin*Tan=', proizv_sin_tan)            
print('Cos*Tan=', proizv_cos_tan) 
