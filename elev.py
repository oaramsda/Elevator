class Elevator:

	'''
	curr_floor
	'''

	to_floor_q = []
	move_dir = 0	# 0: stationary, 1: going up, -1: going down

	def __init__(self, name, start_floor):
		self.curr_floor = start_floor
		self.name = name

	def getCurrFloor(self):
		return self.curr_floor

	def appendToQ(self, floor):
		self.to_floor_q.append(floor)
		return
	def popFirstQ():
		return self.to_floor_q.pop(0)

	def optimizeQ():
		#TODO
		pass

	def moveToFloor(self, floor):
		#if len(self.to_floor_q) == 0:
		if self.curr_floor < floor:
			move_dir = 1
			print(self.name + " moving up")
		elif self.curr_floor > floor:
			move_dir = -1
			print(self.name + " moving down")

			#Some timer thing to time the travel time. Possible need of threads.
			# Need the possibility of getting floor requests while moving up and down

		self.curr_floor = floor
		print(self.name + " reached floor " + str(floor))
		move_dir = 0
		#else:
		#	self.to_floor_q.append(floor)
		

def requestCar(from_floor, to_floors, dir_str):
	elev_car1.appendToQ(from_floor)
	for floor in to_floors:
		elev_car1.appendToQ(floor)

	return

elev_car1 = Elevator("Elevator1", 1)
requestCar(6, [1], "down")
requestCar(1, [4, 5], "up")
requestCar(6, [1], "down")
#print(elev_car1.to_floor_q.pop(0))

while len(elev_car1.to_floor_q) > 0:
	next_floor = elev_car1.to_floor_q.pop(0)
	elev_car1.moveToFloor(next_floor)
print("Done!")

'''
def main():

if __name__ == "__main__":
	main()
'''