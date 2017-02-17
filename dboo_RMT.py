import xlwt
import xlrd

#############################################################################################################################
class E_Relation:
	Property_list = []

	def __init__(self, Entity_name):
		self.Entity_name = Entity_name
		print("An entity is created!")

	def __del__(self):
		class_name = self.__class__.__name__
		#print(class_name,"is deleted")

	def add_P_Relation(self, P_list):
		Property_list += P_list

	def modify_P_Relation(self, old_P_name, new_P_name):
		if '' == new_P_name:
			print("Error: new_P_name can not be empty!")
			break

		for p in Property_list:
			if old_P_name == p:
				p = new_P_name
			else:
				print("Error: old_P_name not corrected!")
				break 

	def delete_P_Relation(self, P_name):
		if '' == P_name:
			print("Error: P_name can not be empty!")
			break

		for p in Property_list:
			if P_name == p:
				Property_list.remove(P_name)
			else:
				print("Error: P_name not corrected!")
				break
############################################################################################################################
def set_C_Relation(E1, E2):	#C_Relation: Characteristic Relation
	C_dic = {'SUB': None, 'SUP': None}
	C_dic['SUB'] = E1.Entity_name
	C_dic['SUP'] = E2.Entity_name
	C_Relation.append(C_dic)

def set_A_Relation(E_list): #A_Relation: Associative Relation
	A_Relation.append(E_list)

def show(R): 



	


if __name__ == '__main__':
	C_Relation = []
	# [ {
	#	 'SUB': 'Mobile',
	#	 'SUP': 'Name'
	#	},
	#	{
	#	 'SUB': 'Mobile',
	#	 'SUP': 'ID'
	#	} 
	#	]
	A_Relation = []	
	# [
	# 	['Mobile', 'Name', 'ID'],
	# 	['Employee', 'Job', 'Salary']
	# ]


	E1 = E_Relation('Mobile') 
	E1.add_P_Relation(['Name', 'ID'])
	E1.modify_P_Relation('ID', 'id_num')
	E2 = E_Relation('Employee')
	E2.add_P_Relation(['Job', 'Salary'])
	E3 = E_Relation('Order')
	set_C_Relation(E1, E2)
	set_A_Relation([E1, E2, E3])




