# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:05:31 2018

@author: Aluno
"""

from mpi4py import MPI

comm=MPI.COMM_WORLD
rank=comm.Get_rank()
if rank==0:
    dados=["marcos",1.8,45]
    comm.send(dados,dest=1)
else:
    dados=comm.recv(source=0)
    print("[%d] Recebeu:"%(rank),dados)