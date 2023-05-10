from djitellopy import Tello
import time


def initialize_tello():
    drone = Tello()
    drone.connect()
    drone.for_back_velocity = 0
    drone.left_right_velocity = 0
    drone.up_down_velocity = 0
    drone.yaw_velocity = 0
    drone.speed = 0
    drone.set_speed(80)
    print(f"Bateria: {drone.get_battery()}%")
    return drone


def takeoff(drone):
    drone.takeoff()
    time.sleep(1)


def land(drone):
    drone.land()
    time.sleep(1)


def move(drone, direction, distance):
    if direction == 'forward':
        drone.move_forward(distance)
    elif direction == 'backward':
        drone.move_back(distance)
    elif direction == 'left':
        drone.move_left(distance)
    elif direction == 'right':
        drone.move_right(distance)
    elif direction == 'up':
        drone.move_up(distance)
    elif direction == 'down':
        drone.move_down(distance)
    time.sleep(1)


def main():
    drone = initialize_tello()
    takeoff(drone)
    move(drone, 'backward', 100)
    move(drone, 'up', 100)
    move(drone, 'down', 100)
    land(drone)
    drone.end()


if __name__ == '__main__':
    main()
