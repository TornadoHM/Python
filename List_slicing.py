# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Imprime el segundo elemento de areas
print(areas[1])

# Imprime el último elemento de areas
print(areas[-1])

# Imprime el área de la sala
print(areas[5])

# -----------------------------------------------------------

# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Suma del área de kitchen y bedroom: eat_sleep_area

eat_sleep_area = areas[3] + areas[-3]

# Imprime la variable eat_sleep_area

print(eat_sleep_area)

# -----------------------------------------------------------

# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Subdivide areas para crear downstairs
downstairs = areas[0:6]

# Subdivide areas para crear upstairs

upstairs = areas[6:10]

# Imprime downstairs y upstairs

print(downstairs)
print(upstairs)

                      #ALTERNATIVE ALTERNATIVE

areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Corte alternativo para crear downstairs

downstairs = areas[:6]

# Corte alternativo para crear upstairs

upstairs = areas[6:]


