#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dboo_RMT as RMT

if __name__ == '__main__':
#########################################################################################################
	###############
	## Section 2 ##
	###############
	# init Relation object
	R1 = RMT.Relation()	
	# new Entity
	E1 = RMT.Entity('Mobile', R1)
	E2 = RMT.Entity('Order', R1)
	E3 = RMT.Entity('AfterSales', R1)
	# add Property
	E1.add_P_Relation(['IMEI', 'Name'])
	E2.add_P_Relation(['Date', 'Price', '1111'])
	E3.add_P_Relation(['ID', 'Years'])
	# # modify P_Relation
	# E1.modify_P_Relation('ID', 'id_num') # Error : name not match!
	# E2.delete_P_Relation('1111')
	# E3.modify_P_Relation('Years', 'Year') # modify_P_Relation(old_P_name, new_P_name)
	# show P_Relation
	R1.show_P_Relation(E1)
	R1.show_P_Relation(E2)
	R1.show_P_Relation(E3)