#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dboo_RMT as RMT

if __name__ == '__main__':
	R1 = RMT.Relation()
	E1 = RMT.E_Relation('Mobile') 
	E1.add_P_Relation(['Name', 'ID', 'Model'])
	#print(E1.Property_list)
	#E1.modify_P_Relation('ID', 'id_num')
	R1.Kernel_Entity.append(E1.Entity_name)

	E2 = RMT.E_Relation('Employee')
	# print(E2.Entity_name)
	# print(E2.Property_list)
	E2.add_P_Relation(['Job', 'Salary'])
	# print(E2.Property_list)
	R1.Kernel_Entity.append(E2.Entity_name)

	E3 = RMT.E_Relation('Order')
	R1.Kernel_Entity.append(E3.Entity_name)

	R1.set_C_Relation(E1, E2)
	R1.set_A_Relation([E1, E2, E3])

	R1.show_E_Relation(R1.Kernel_Entity)
	R1.show_P_Relation(E1)
	R1.show_P_Relation(E2)

	R1.show_C_Relation(R1.C_Relation)
	# print(R1.A_Relation)
	R1.show_A_Relation(R1.A_Relation)