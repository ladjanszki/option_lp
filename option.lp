\Harom vilagallapot, ket ertekpapir, normalizalva
min																						
der:	+1 th0_0	+100 th0_1	+0 th1_0	+0 th1_1	+0 th2_0	+0 th2_1	
																						
subject to																						

onfin1:	-1 th0_0	-200 th0_1	+1 th1_0	+200 th1_1 = -100
onfin2:	-1 th0_0  -50  th0_1	+1 th2_0	+50  th2_1 = 0


nemne3: +1 th1_0	+200 th1_1	>= 0
nemne4: +1 th2_0	+50  th2_1  >= 0

bounds																						
th0_0	free																					
th0_1	free																					

th1_0	free																					
th1_1	free																					

th2_0	free																					
th2_1	free																					

end																						
 
