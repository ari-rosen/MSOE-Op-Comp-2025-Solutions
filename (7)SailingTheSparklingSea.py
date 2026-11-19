import math

content = ""
with open("SailingTheSparklingSeas.txt", "r") as file:
    content = file.read().strip()

lines = content.split('\n')

x = 0
y = 0
v = 11.112 # km/hr

total_time = 0

for waypoint in lines:
    output = []

    waypoint = waypoint.split()
    reef = True if len(waypoint) > 2 else False

    waypoint_x = float(waypoint.pop(0))
    waypoint_y = float(waypoint.pop(0))

    name = None if not reef else " ".join(waypoint)

    if name is not None:
        output.append(name)
    else:
        output.append("Unnamed Way Point")

    output.append(f"({waypoint_y:.2f} North, {waypoint_x:.2f} East)")

    dx = waypoint_x - x
    dy = waypoint_y - y
    heading = math.degrees(math.atan2(dx, dy))
    if heading < 0:
        heading += 360

    output.append(f"{heading:.2f}°")

    distance = math.dist((waypoint_x, waypoint_y), (x, y))
    time = (distance / v) * 60
    
    snorkel_text = " (+ 3 hours for snorkeling)" if reef else ""
    output.append(f"{time:.2f} minutes traveling at 6 knots{snorkel_text}")
    
    if reef:
        time += 180

    total_time += time

    print("\n".join(output) + "\n")

    x = waypoint_x
    y = waypoint_y

print(f"Total Time: {total_time/60:.2f} hours")

individual_need = 0.00277 # liters / min

total_need = individual_need * 4 * total_time
total_containers = math.ceil(total_need / 25)

print(f"Total Water Canisters: {total_containers}")







