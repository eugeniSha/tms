x = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
y = [(3, 3, 3), (2, 2, 2), (1, 1, 1)]
z = [(2, 2, 2), (3, 3, 3), (4, 4, 4)]
# result = [x[0], y[1], z[2]]
result = [i*c*v for i in x[0] for c in y[1] for v in z[2]]
print(result)
