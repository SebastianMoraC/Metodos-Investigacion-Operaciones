import sympy as sp
x, y = sp.var('x,y',real=True);
f = input()
f = eval(f)
g = input()
g = eval(g)

"""Definición de función Lagrangniana"""

lam = sp.symbols('lambda', real = True)
L = f - lam* g

gradL = [sp.diff(L,c) for c in [x,y]] 
KKT_eqs = gradL + [g]
KKT_eqs

stationary_points = sp.solve(KKT_eqs, [x, y, lam], dict=True) 
stationary_points

[f.subs(p) for p in stationary_points]

