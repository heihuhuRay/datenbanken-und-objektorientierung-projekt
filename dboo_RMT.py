#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import xlwt
# import xlrd

from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys
 

############################################################################################################################
class E_Relation(object):
	#Property_list = []

	def __init__(self, Entity_name, Property_list = []):
		self.Entity_name = Entity_name
		self.Property_list = [] # ?????????????????????
		print("An entity is created!")
		print(self.Property_list)

	def __del__(self):
		class_name = self.__class__.__name__
		#print(class_name,"is deleted")

	def add_P_Relation(self, P_list):
		#self.P_list = P_list
		self.Property_list += P_list

	def modify_P_Relation(self, old_P_name, new_P_name):
		if '' == new_P_name:
			print("Error: new_P_name can not be empty!")
		is_correct_old_name = False
		for p in self.Property_list:
			if old_P_name == p:
				p = new_P_name
				is_correct_old_name = True
		if False == is_correct_old_name:
			print("Error: old_P_name not corrected!")

	def delete_P_Relation(self, P_name):
		if '' == P_name:
			print("Error: P_name can not be empty!")
		is_correct_P_name = False
		for p in self.Property_list:
			if P_name == p:
				self.Property_list.remove(P_name)
				is_correct_P_name = True
		if False == is_correct_P_name:
			print("Error: P_name not corrected!")

############################################################################################################################
class Relation(object):
	"""docstring for Relation"""
	def __init__(self, Kernel_Entity = [], C_Relation = [], A_Relation = []):
		self.Kernel_Entity = Kernel_Entity
		self.C_Relation = C_Relation
		self.A_Relation = A_Relation
		
	def set_C_Relation(self, E1, E2):	#C_Relation: Characteristic Relation
		C_dic = {'SUB': None, 'SUP': None}
		C_dic['SUB'] = E1.Entity_name
		C_dic['SUP'] = E2.Entity_name
		self.C_Relation.append(C_dic)

	def set_A_Relation(self, E_list): #A_Relation: Associative Relation
		E_name_list = []
		for e in E_list:
			E_name_list.append(e.Entity_name)
		self.A_Relation.append(E_name_list)
	###########################################################################################################################
	def show_E_Relation(self, K_list): 
		app 	= QApplication(sys.argv)
		table 	= QTableWidget()
		tableItem 	= QTableWidgetItem()
		# initiate table
		table.setWindowTitle("E Relation")
		table.resize(400, 250)
		table.setRowCount(2*len(K_list))
		table.setColumnCount(1)
		# set data
		for k in K_list:
			table.setItem(2*K_list.index(k), 0, QTableWidgetItem(k+u'\u00a2')) # u'\u00a2' : ¢
		#hide labels
		table.verticalHeader().setVisible(False)
		table.horizontalHeader().setVisible(False)
		# show table
		table.show()
		return app.exec_()

	def show_P_Relation(self, E):
		app 	= QApplication(sys.argv)
		table 	= QTableWidget()
		tableItem 	= QTableWidgetItem()
		# initiate table
		table.setWindowTitle("P Relation")
		table.resize(400, 250)
		table.setRowCount(2)
		table.setColumnCount(len(E.Property_list)+1)
		# set data
		table.setItem(0, 0, QTableWidgetItem(E.Entity_name+u'\u00a2'))
		for p in E.Property_list:
			table.setItem(0, E.Property_list.index(p)+1, QTableWidgetItem(p)) # u'\u00a2' : ¢
		#hide labels
		table.verticalHeader().setVisible(False)
		table.horizontalHeader().setVisible(False)
		# show table
		table.show()
		return app.exec_()

	def show_C_Relation(self, C_list):
		app 	= QApplication(sys.argv)
		table 	= QTableWidget()
		tableItem 	= QTableWidgetItem()

		# initiate table
		table.setWindowTitle("Characteristic Graph Relation")
		table.resize(400, 250)
		table.setRowCount(len(C_list)+1)
		table.setColumnCount(2)

		# set data
		table.setItem(0,0, QTableWidgetItem('SUB'))
		table.setItem(0,1, QTableWidgetItem('SUP'))
		for c in C_list:
			table.setItem(C_list.index(c)+1, 0, QTableWidgetItem(c['SUB']))
			table.setItem(C_list.index(c)+1, 1, QTableWidgetItem(c['SUP']))

		#hide labels
		table.verticalHeader().setVisible(False)
		table.horizontalHeader().setVisible(False)

		# show table
		table.show()
		return app.exec_()

	def show_A_Relation(self, A_list):
		app 	= QApplication(sys.argv)
		table 	= QTableWidget()
		tableItem 	= QTableWidgetItem()

		# initiate table
		table.setWindowTitle("Associative Graph Relation")
		table.resize(400, 250)
		table.setRowCount(2)
		table.setColumnCount(3)

		# set data
		for a in A_list:
			for n in a:
				table.setItem(0, a.index(n), QTableWidgetItem(n))
		# table.setItem(0,0, QTableWidgetItem("Item (1,1)"))
		# table.setItem(0,1, QTableWidgetItem("Item (1,2)"))
		# table.setItem(1,0, QTableWidgetItem("Item (2,1)"))
		# table.setItem(1,1, QTableWidgetItem("Item (2,2)"))
		# table.setItem(2,0, QTableWidgetItem("Item (3,1)"))
		# table.setItem(2,1, QTableWidgetItem("Item (3,2)"))
		# table.setItem(3,0, QTableWidgetItem("Item (4,1)"))
		# table.setItem(3,1, QTableWidgetItem("Item (4,2)"))
		#hide labels
		table.verticalHeader().setVisible(False)
		table.horizontalHeader().setVisible(False)
		# show table
		table.show()
		return app.exec_()


	


# if __name__ == '__main__':
	# [ {
	#	 'SUB': 'Mobile',
	#	 'SUP': 'Name'
	#	},
	#	{
	#	 'SUB': 'Mobile',
	#	 'SUP': 'ID'
	#	} 
	#	]
	
	# [
	# 	['Mobile', 'Name', 'ID'],
	# 	['Employee', 'Job', 'Salary']
	# ]
	# Kernel_Entity = [] 
	# C_Relation = []
	# A_Relation = []	

	# E1 = E_Relation('Mobile') 
	# E1.add_P_Relation(['Name', 'ID'])
	# print(E1.Property_list)
	# E1.modify_P_Relation('ID', 'id_num')
	# Kernel_Entity.append(E1.Entity_name)

	# E2 = E_Relation('Employee')
	# E2.add_P_Relation(['Job', 'Salary'])
	# Kernel_Entity.append(E2.Entity_name)

	# E3 = E_Relation('Order')
	# Kernel_Entity.append(E3.Entity_name)
	# set_C_Relation(E1, E2)
	# set_A_Relation([E1, E2, E3])

	# # show_E_Relation(Kernel_Entity)
	# show_P_Relation(E1)
	# # show_C_Relation(C_Relation)
	# print(A_Relation)
	# show_A_Relation(A_Relation)




