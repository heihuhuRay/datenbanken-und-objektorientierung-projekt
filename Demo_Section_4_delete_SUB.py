#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dboo_RMT as RMT

if __name__ == '__main__':
#########################################################################################################
	###############
	## Section 4 ##
	###############
	# init Relation object
	R1 = RMT.Relation()	
	# new Entity
	E1 = RMT.Entity('Mobile', R1)
	E2 = RMT.Entity('Order', R1)
	E3 = RMT.Entity('AfterSales', R1)
	E4 = RMT.Entity('Maf', R1)
	E5 = RMT.Entity('Processor', R1)

	# add Property
	E1.add_P_Relation(['IMEI', 'Name'])
	E2.add_P_Relation(['Date', 'Price'])
	E3.add_P_Relation(['ID', 'Year'])
	# set Relations
	R1.set_C_Relation(E2, E1)
	R1.set_C_Relation(E3, E2)
	R1.set_A_Relation([E4, E5, E1])
	# CG_Relation
	#R1.show_CG_Relation(R1.C_Relation)
	# show E Relation
	R1.show_Entity(R1.Kernel_Entity)
	E3.delete_Entity(R1)
	R1.show_Entity(R1.Kernel_Entity)