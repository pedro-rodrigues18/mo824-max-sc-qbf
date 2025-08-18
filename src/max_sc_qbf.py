from gurobipy import Model, GRB, quicksum


class MaxSetCoverQBF:
    def __init__(self, path):
        self.path = path
        self.x = []  # Binary variables
        self.subsets = []  # Subsets to cover all elements (variables)
        self.coefficients = []  # Upper triangle values from matrix A

        self._initialize()

    def _read_data(self) -> str | None:
        print(f"Reading data from {self.path}")
        with open(self.path, "r") as file:
            try:
                data = file.read()
            except Exception as e:
                print(f"Error reading {self.path}: {e}")
                return None
        return data

    def _initialize(self) -> None:
        """
        Initialize the Max Set Cover QBF problem instance by reading data from the input file.
        """
        data = self._read_data()
        if data is None:
            return

        lines = data.splitlines()
        n = int(lines[0])  # number of variables (subsets)
        self.x = [0] * n

        sizes = list(map(int, lines[1].split()))

        # Subsets
        self.subsets = []
        for i in range(n):
            subset = list(map(int, lines[2 + i].split()))
            assert (
                len(subset) == sizes[i]
            ), f"Erro: tamanho inconsistente no subconjunto {i}"
            self.subsets.append(subset)

        #   Triangular matrix coefficients
        self.coefficients = []
        for line in lines[2 + n :]:
            coeffs = list(map(float, line.split()))
            self.coefficients.append(coeffs)

    def solve(self, full_path) -> None:
        model = Model("MaxSetCoverQBF")
        model.setParam("TimeLimit", 900)
        model.setParam("LogFile", f"logs/{full_path}")

        n = len(self.subsets)

        # Variables
        x = model.addVars(n, vtype=GRB.BINARY, name="x")

        # Auxiliary variables for linearization
        y = {}
        for i in range(n):
            for j in range(i + 1, n):
                y[i, j] = model.addVar(
                    vtype=GRB.CONTINUOUS, lb=0, ub=1, name=f"y[{i},{j}]"
                )

        model.update()

        # Linearization constraints
        for i in range(n):
            for j in range(i + 1, n):
                model.addConstr(y[i, j] <= x[i])
                model.addConstr(y[i, j] <= x[j])
                model.addConstr(y[i, j] >= x[i] + x[j] - 1)

        # Set cover constraints
        u = set(range(1, n + 1))
        for k in u:
            expr = quicksum(x[i] for i in range(n) if k in self.subsets[i])
            model.addConstr(expr >= 1, name=f"cover_{k}")

        # Objective function
        obj = 0
        for i in range(n):
            obj += self.coefficients[i][0] * x[i]
            for j, aij in enumerate(self.coefficients[i][1:], start=i + 1):
                obj += aij * y[i, j]

        model.setObjective(obj, GRB.MAXIMIZE)

        model.optimize()

        if model.status == GRB.OPTIMAL:
            print("Optimal solution found:")
            for i in range(n):
                print(f"x[{i+1}] = {x[i].X}")
            # Selected subsets
            selected_subsets = [i + 1 for i in range(n) if x[i].X > 0.5]
            print(f"Selected subsets: {selected_subsets}")
            print(f"Objective value: {model.ObjVal}")
        else:
            print("No optimal solution found.")
