#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dboo_RMT as RMT

if __name__ == '__main__':
	# init Relation object
	R1 = RMT.Relation()	
	# new Entity
	E1 = RMT.Entity('Mobile')
	E2 = RMT.Entity('Order')
	E3 = RMT.Entity('AfterSales')
	# add to Kernel_Entity list
	R1.Kernel_Entity.append(E1.Entity_name)
	R1.Kernel_Entity.append(E2.Entity_name)
	R1.Kernel_Entity.append(E3.Entity_name)
	# add P_Relation
	E1.add_P_Relation(['IMEI', 'Name'])
	E2.add_P_Relation(['Date', 'Price'])
	E3.add_P_Relation(['ID', 'Year'])
	# modify P_Relation
	#E1.modify_P_Relation('ID', 'id_num')
	
	# set Relations
	R1.set_C_Relation(E2, E1)
	R1.set_C_Relation(E3, E2)
	R1.set_A_Relation([E1, E2, E3])
	# show P Relation
	R1.show_Entity(R1.Kernel_Entity)
	R1.show_P_Relation(E1)
	R1.show_P_Relation(E2)
	# PG Relation
	R1.show_PG_Relaion(E1)
	R1.show_PG_Relaion(E2)

	# CG_Relation
	R1.show_CG_Relation(R1.C_Relation)
	 
	R1.show_A_Relation(R1.A_Relation)

	E1.delete_Entity(R1)

#####################################################################################################
# class Entity():
	
# 	__del__()
# 	add_P_Relation(P_Name_List)
# 	modify_P_Relation(old_P_name, new_P_name)
# 	delete_P_Relation(P_name)

# class Relation():

# 	set_C_Relation(SUB_E, SUP_E)
# 	set_A_Relation(E_list)
# 	show_Entity(K_list)
# 	show_P_Relation(E)
# 	show_PG_Relaion(E)
# 	show_CG_Relation(C_list)
# 	show_A_Relation(A_list)
