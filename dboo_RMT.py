import xlwt
import xlrd

class E_Relation:
	def __init__(self, Entity_name):
		self.Entity_name = Entity_name
		print("An entity is created!")

	def __del__(self):
		class_name = self.__class__.__name__
		#print(class_name,"is deleted")

	def add_P_Relation(Property_list):
		print(Property_list[0])
		print(Property_list[1])
	



	
E1 = E_Relation("Mobile")
l = ["Name", "ID"]
E1.add_P_Relation(l)





