import numpy as np
import math
import autograd.numpy as anp
from pymoo.model.problem import Problem

class CIBN1(Problem):

    def __init__(self):

        # define lower and upper bounds -  1d array with length equal to number of variable
        xl = 0 * anp.ones(10)
        xu = 1 * anp.ones(10)

        super().__init__(n_var=10, n_obj=2, n_constr=1, xl=xl, xu=xu, elementwise_evaluation=True)

    def _evaluate(self, x, out, *args, **kwargs):
        n=10
        t = [x[i]-x[0]**2 for i in range(n)]
        val = 0
        for i in range (1,n):
            val += abs(-0.9*(t[i]**2)+abs(math.sin(0.5*math.pi*t[i])))
        g = 0.03*val
        if x[0]>0.5:
            flag=True
        else:
            flag=False
        if flag==True and g>0.01:
            G = 1+10*g
        else:
            G = 0
        g1 = G
        
        f1 = (1+g)*x[0]
        f2 = (1+15*g)*(1-x[0])

        out["F"] = anp.column_stack([f1,f2])
        out["G"] = anp.column_stack([g1])
        
class CIBN2(Problem):

    def __init__(self):

        # define lower and upper bounds -  1d array with length equal to number of variable
        xl = 0 * anp.ones(10)
        xu = 1 * anp.ones(10)

        super().__init__(n_var=10, n_obj=2, n_constr=1, xl=xl, xu=xu, elementwise_evaluation=True)

    def _evaluate(self, x, out, *args, **kwargs):
        n=10
        t = [x[i]-x[0]**2 for i in range(n)]
        val = 0
        for i in range (1,n):
            val += abs(-0.9*(t[i]**2)+abs(math.sin(0.5*math.pi*t[i])))
        g = 0.02*val
        if x[0]<0.2 or x[0]>0.8:
            flag=True
        else:
            flag=False
        if flag==True and g>0.005:
            G = 1+10*g
        else:
            G = 0
        g1 = G
        
        f1 = (1+g)*x[0]
        f2 = (1+2.5*g)*(1-x[0]**0.5)

        out["F"] = anp.column_stack([f1,f2])
        out["G"] = anp.column_stack([g1])
        
class CIBN3(Problem):

    def __init__(self):

        # define lower and upper bounds -  1d array with length equal to number of variable
        xl = 0 * anp.ones(10)
        xu = 1 * anp.ones(10)

        super().__init__(n_var=10, n_obj=2, n_constr=1, xl=xl, xu=xu, elementwise_evaluation=True)

    def _evaluate(self, x, out, *args, **kwargs):
        n=10
        t = [x[i]-math.sin(0.5*math.pi*x[0]) for i in range(n)]
        val = 0
        for i in range (1,n):
            val += abs(-0.9*(t[i]**2)+abs(math.sin(0.5*math.pi*t[i])))
        g = 0.035*val
        if x[0]>0.8 or x[0]<0.2:
            flag=True
        else:
            flag=False
        if flag==True and g>0.005:
            G = 1+10*g
        else:
            G = 0
        g1 = G
        
        f1 = (1+0.9*g)*math.cos(0.5*math.pi*x[0])
        f2 = (1+1.7*g)*math.sin(0.5*math.pi*x[0])

        out["F"] = anp.column_stack([f1,f2])
        out["G"] = anp.column_stack([g1])
        
class CIBN4(Problem):

    def __init__(self):

        # define lower and upper bounds -  1d array with length equal to number of variable
        xl = 0 * anp.ones(10)
        xu = 1 * anp.ones(10)

        super().__init__(n_var=10, n_obj=3, n_constr=1, xl=xl, xu=xu, elementwise_evaluation=True)

    def _evaluate(self, x, out, *args, **kwargs):
        n=10
        t = [x[i]-(x[0]+x[1]+x[2])/3 for i in range(n)]
        val = 0
        for i in range (3,n):
            val += abs(-0.9*(t[i]**2)+abs(math.sin(0.5*math.pi*t[i])))
        g = 0.05*val
        if x[0]>0.8:
            flag=True
        else:
            flag=False
        if flag==True and g>0.005:
            G = 1+10*g
        else:
            G = 0
        g1 = G
        
        f1 = (1+0.8*g)*x[0]*x[1]
        f2 = (1+1.1*g)*x[0]*(1-x[1])
        f3 = (1+2.2*g)*(1-x[0])

        out["F"] = anp.column_stack([f1,f2,f3])
        out["G"] = anp.column_stack([g1])

class CIBN5(Problem):

    def __init__(self):

        # define lower and upper bounds -  1d array with length equal to number of variable
        xl = 0 * anp.ones(10)
        xu = 1 * anp.ones(10)

        super().__init__(n_var=10, n_obj=3, n_constr=1, xl=xl, xu=xu, elementwise_evaluation=True)

    def _evaluate(self, x, out, *args, **kwargs):
        n=10
        t = [x[i]-x[0]*x[1] for i in range(n)]
        val = 0
        for i in range (2,n):
            val += abs(-0.9*(t[i]**2)+abs(math.sin(0.5*math.pi*t[i])))
        g = 0.01*val
        s1,s2 = x[0]+1,x[1]+1
        if x[0]>0.8 or x[0]<0.2:
            flag=True
        else:
            flag=False
        if flag==True and g>0.001:
            G = 10*g
        else:
            G = 0
        g1 = G
        
        f1 = (1+g)*(1+math.sin(0.5*math.pi*s1)*math.cos(-0.5*math.pi*s2))
        f2 = (1+g)*(1+math.sin(0.5*math.pi*s1)*math.sin(-0.5*math.pi*s2))
        f3 = (1+g)*(1+math.cos(0.5*math.pi*s1))

        out["F"] = anp.column_stack([f1,f2,f3])
        out["G"] = anp.column_stack([g1])