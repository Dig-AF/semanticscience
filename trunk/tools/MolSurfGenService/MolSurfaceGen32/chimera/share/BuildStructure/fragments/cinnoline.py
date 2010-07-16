from BuildStructure.Fragment import Fragment, RING66
frag = Fragment("cinnoline", [
	("C", (4.83333, -3.67431, -0.377505)),
	("H", (3.89461, -3.12582, -0.377494)),
	("C", (4.82983, -5.06471, -0.377533)),
	("H", (3.88935, -5.61016, -0.377664)),
	("C", (6.04093, -5.76248, -0.377348)),
	("H", (6.03389, -6.85, -0.377464)),
	("C", (7.26349, -5.09877, -0.376724)),
	("N", (8.41926, -5.78484, -0.375783)),
	("N", (9.62485, -5.13221, -0.374415)),
	("C", (9.64784, -3.78873, -0.37448)),
	("H", (10.6326, -3.33678, -0.373148)),
	("C", (8.49482, -3.03175, -0.375792)),
	("H", (8.55863, -1.94932, -0.375912)),
	("C", (7.26349, -3.69233, -0.376724)),
	("C", (6.04636, -2.98722, -0.377354)),
	("H", (6.03764, -1.89959, -0.377413)),
	], [
	((0,1), None),
	((0,2), (6.04624, -4.37997, -0.377198)),
	((2,3), None),
	((2,4), None),
	((4,5), None),
	((4,6), (6.04624, -4.37997, -0.377198)),
	((6,7), None),
	((8,7), (8.45229, -4.42144, -0.375653)),
	((9,8), None),
	((9,10), None),
	((11,9), (8.45229, -4.42144, -0.375653)),
	((11,12), None),
	((13,11), None),
	((13,14), (6.04624, -4.37997, -0.377198)),
	((14,15), None),
	((0,14), None),
	((6,13), None),
	])

fragInfo = [RING66, frag]