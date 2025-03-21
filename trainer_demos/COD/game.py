#! /usr/bin/env python3
# Author: DCameron
# Description: This is an ultra realistic online game with Tanks!
"""
    Tank Game!
"""
import sys
import tank

def main():
    # Create/instantiate 3 new Tank objects
    david_tank = tank.Tank('german', 'tiger')
    rohit_tank = tank.Tank('american', 'sherman')
    john_tank = tank.Tank('british', 'churchill')

    # And the game begins..
    david_tank.accel(59)
    rohit_tank.accel(32)

    john_tank.rotate_right(289)
    john_tank.accel(27)
    john_tank.shoot()

    # And success..
    david_tank.take_damage(65)
    rohit_tank.take_damage(40)

    # and now for some visuals - print statements!
    # print(f"Health of David's tank is {david_tank._health}") # POOR CODE!

    # Example of operator overloading
    print(f"Health of David's and Rohit's tank = {david_tank + rohit_tank}")

    # David has received a HEALTH BOOST!
    # david_tank._health = 100 # POOR CODE!
    # print(f"New health of David's Tank is {david_tank._health}") # POOR CODE!
    david_tank.set_health(101) # Example of a SETTER method. GOOD!
    print(f"Newhealth of David's tank = {david_tank.get_health()}") # GETTER method! GOOD!

    david_tank.tank_health = 102
    print(f"Newhealth of David's tank = {david_tank.tank_health}")

    print(f"Status of David's Tank: {david_tank}")


    return None

# Namespace trick
if __name__ == "__main__":
    main()
    sys.exit(0)