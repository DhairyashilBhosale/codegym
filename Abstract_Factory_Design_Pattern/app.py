from furniture_factory import FurnitureFactory



if __name__ == "__main__":
	
	furniture_type = "MediumTable"
	furniture = FurnitureFactory.get_furniture(furniture_type)
	
	print(furniture.get_info())
