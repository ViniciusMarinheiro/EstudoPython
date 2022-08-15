from numba import jit
import numpy as np
from timeit import default_timer as timer   
  
# Função normal com execução pelo CPU - i7 2600
def func(a):                                
    for i in range(100000000):
        a[i]+= 1      
  
# Função otimizada com execução pela GPU - RTX 2060 6GB
@jit()                      
def func2(a):
    for i in range(100000000):
        a[i]+= 1
        
if __name__=="__main__":
    n = 100000000                            
    a = np.ones(n, dtype = np.float64)
    b = np.ones(n, dtype = np.float32)
    lista1 = []
    lista = np.array([])
    
    start = timer()
    func(a)
    print("Sem GPU:", timer()-start)    
      
    start = timer()
    func2(a)
    print("Com GPU:", timer()-start)