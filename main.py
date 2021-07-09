from scipy.optimize import linprog
from tabulate import tabulate
from numpy import copy

##########################################################################
# VALORES
##########################################################################

# The coefficient of the linear objective function to be minimized.
c_input = input("Ingrese los coeficientes de la funcion objetivo: ")
c_input = c_input.split(",")
c = [float(value) for value in c_input]
variables = len(c)
#c = [70, 80, 85]
#c = [-200, -150 ]

# The inequality constraint matrix. Each row of A_ub specifies the coefficients of a linear inequality
# constraint on x.
restr = input("Cuantas restricciones quiere agregar?: ")
A_ub = []

for _ in range(int(restr)):
    A_input = input("Ingrese los coeficientes de las restricciones: ")
    A_input = A_input.split(",")
    A = [float(value) for value in A_input]
    A_ub.append(A)
#A_ub = [[1, 2], [3, 2]]

# The inequality constraint vector. Each element represents an upper bound on the corresponding
# value of A_ub @ x.
b_input = input("Ingrese los resultados de las restricciones: ")
b_input = b_input.split(",")
b_ub = [float(value) for value in b_input]
#b_ub = [80, 120]

# The equality constraint matrix. Each row of A_eq specifies the coefficients of a linear equality constraint on x.
#A_eq = [[1, 1, 1]]

# The equality constraint vector. Each element of A_eq @ x must equal the corresponding element of b_eq.
#b_eq = [999]

# A sequence of (min, max) pairs for each element in x, defining the minimum and maximum values of that decision
# variable. Use None to indicate that there is no bound. By default, bounds are (0, None) (all decision variables
# are non-negative). If a single tuple (min, max) is provided, then min and max will serve as bounds for all
# decision variables.
bounds = (0, None)

print(f"Sistema a resolver:" )

print("Cj:", end="\t")
for _ in c:
    print(_, end="\t")

print("")
vars = ["x" + str(value+1) for value in range(variables)]
vars.append("R")
vars.insert(0, "Base")
# for _ in vars:
#     print(_, end="\t\t")
# print("")

# for i, value in enumerate(A_ub):
#     for _ in value:
#         print(_, end="\t\t")
#     print(b_ub[i])

matrix = A_ub
A_ub = copy(A_ub)

for i, value in enumerate(matrix):
    value.append(b_ub[i])
    value.insert(0, "S" + str(i+1))

z = [str(value*(-1)) for value in c]
z.insert(0, "Z")
z.append("0")

matrix.insert(0, vars)
matrix.append(z)
print(tabulate(matrix, headers="firstrow"))
input("")
# for _ in z:
#     print(_, end="\t\t")

# callback
# fun: The current value of the objective function c @ x.
# x: The current solution vector.
def mostrar(solucion):
    print(f"\nIteración {solucion.nit+1}")
    print(f"---------------")
    print(f"Valor optimo: {solucion.fun:.2f}")

    for i, value in enumerate(solucion.x):
        print(f"\tx{i+1}: {value:.2f}")

    message = {
        0: "Iteracion exitosa",
        1: "Se alcanzo el limite de iteraciones",
        2: "El problema no tiene solucion",
        3: "La solucion no esta acotada",
        4: "Hubo un problema"
    }

    print(f"Estado: {message[solucion.status]}")
    input("")
    print(f"")

#solv = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds, callback=mostrar)
solv = linprog(c, A_ub, b_ub, bounds=bounds, callback=mostrar)


