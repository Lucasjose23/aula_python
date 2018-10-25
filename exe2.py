# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:30:50 2018

@author: Aluno
"""


from mpi4py import MPI
import numpy as np


comm=MPI.COMM_WORLD
rank=comm.Get_rank()

if rank==0:
    vet=np.random.randint(10,100,100)
    comm.Send([vet,5,MPI.INT],dest=1)
else:
    v=np.empty(5,dtype=np.int)
    comm.Recv(v,source=0)
    print("[%d] Recebeu:"%(rank),v)    
    
    
    
    