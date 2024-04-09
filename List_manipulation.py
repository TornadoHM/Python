# Crea la lista areas
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Corrige el área de bathroom

areas[-1] = 10.50

# Cambia "living room" a "chill zone"

areas[-6] = "chill zone"

print(areas)

# Crea la lista areas y realiza algunos cambios.
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Agrega datos de poolhouse a areas, la nueva lista es areas_1

areas_1 = areas + ["poolhouse", 24.5]

# Agrega los datos de garage a areas_1, la nueva lista es areas_2

areas_2 = areas_1 + ["garage", 15.45]

print(areas_2)
