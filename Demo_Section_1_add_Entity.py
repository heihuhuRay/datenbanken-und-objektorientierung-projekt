#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dboo_RMT as RMT

if __name__ == '__main__':
#########################################################################################################
	###############
	## Section 1 ##
	###############
	# init Relation object
	R1 = RMT.Relation()	
	# new Entity
	E1 = RMT.Entity('Mobile', R1)
	E2 = RMT.Entity('Order', R1)
	E3 = RMT.Entity('AfterSales', R1)
	# add Property
	E1.add_P_Relation(['IMEI', 'Name'])
	E2.add_P_Relation(['Date', 'Price'])
	E3.add_P_Relation(['ID', 'Year'])
	# show E Relation
	R1.show_Entity(R1.Kernel_Entity)
	# show P_Relation
	R1.show_P_Relation(E1)
	R1.show_P_Relation(E2)
	R1.show_P_Relation(E3)
	# PG Relation
	R1.show_PG_Relaion(E1)
	R1.show_PG_Relaion(E2)
	R1.show_PG_Relaion(E3)