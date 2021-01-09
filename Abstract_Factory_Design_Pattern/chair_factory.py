from chair_types import SmallChair, MediumChair, LargeChair


class ChairFactory():

	@staticmethod
	def get_chair_details(chair_type):
		
		if chair_type == "SmallChair":
			return SmallChair()
		elif chair_type == "MediumChair":
			return MediumChair()
		elif chair_type == "LargeChair":
			return LargeChair()

