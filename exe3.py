# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:54:57 2018

@author: Aluno
"""

from mpi4py import MPI
import numpy as np
import sys


comm=MPI.COMM_WORLD
rank=comm.Get_rank()
procs=comm.Get_size() 
escravos=procs-1
if escravos==0:
    print("Utilizar pelomenos 2 bobos")
    exit()

  
if len(sys.argv)==1:
    print("tamanho do vetor")
    exit()    
if rank==0:
    tamvet=int(sys.argv[1])
    vet=np.arange(tamvet)
    tamsubvet=tamvet//escravos
    resto=tamvet-tamsubvet*escravos 
    
    for i in range(escravos):
        pos=i*tamsubvet
        if (i==escravos-1):
            comm.Send([vet[pos:],tamsubvet+resto,MPI.INT],i+1)
        else:
            comm.Send([vet[pos:],tamsubvet,MPI.INT],i+1)
        soma=comm.recv(source=i+1)  
        print("soma=",soma)
        
        
else:
    status=MPI.Status()#pega o tamanho do vetor
    comm.Probe(MPI.ANY_SOURCE,MPI.ANY_TAG,status)
    tamsubvet=status.Get_elements(MPI.INT)##converte o numero de posicoes do vetor pra int
    vet=np.empty(tamsubvet,dtype=np.int)
    comm.Recv(vet)
    resultado=sum(vet)
    
    print("[%d] recebeu:"%(rank),vet)   
    comm.send(resultado,dest=0)     
     
    