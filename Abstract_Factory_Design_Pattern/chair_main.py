from chair_factory import ChairFactory



if __name__ == "__main__":

	chair = ChairFactory.get_chair_details("SmallChair")
	print(chair.get_info())
