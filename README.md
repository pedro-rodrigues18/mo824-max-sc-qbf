# mo824-max-sc-qbf

#### Students: Pedro H. R. Pereira, Pedro P. Gomes do Carmo, Mauricio P. Lopes.

Implementation of the **MAX-QBF** problem using a **Set Cover** modeling approach with the **Gurobi** solver.

## Requirements

* Python 3.11+
* [Poetry](https://python-poetry.org/) for dependency management
* [Gurobi Optimizer](https://www.gurobi.com/) with a valid license
* `gurobipy` package

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/pedro-rodrigues18/mo824-max-sc-qbf.git
   cd mo824-max-sc-qbf
   ```

2. Create and activate the virtual environment with **Poetry**:

   ```bash
   poetry install
   poetry shell
   ```

3. Manually install `gurobipy`:

   ```bash
   python -m pip install gurobipy
   ```

⚠️ **Important**: A valid Gurobi license is required to run the solver.
More details: [Gurobi License Instructions](https://www.gurobi.com/documentation/).

---

## Running the Code

### Run the main model

```bash
python src/main.py
```

* In `main.py` you will find the following flag:

  ```python
  debug = False
  ```

  * If `debug = True`, the program will run **a single instance**, defined by:

    ```python
    instance_name = "your_instance_name"
    ```
  * If `debug = False`, the program will run in **batch mode**, processing all instances available in the `input/` folder.

    * For each processed instance, the **Gurobi log** is saved in the `logs/` folder with the same name as the instance.

---

### Generate instances

To create new problem instances:

```bash
python src/generate_instances.py
```

* Generated instances are saved in the `input/` folder.
* ⚠️ Existing files will **not be overwritten**. New files will be created sequentially.

---

## Project Structure

```
├── input/                     # Input instances
├── logs/                      # Gurobi execution logs
├── src/
│   ├── main.py                # Main script
|   ├── max_sc_qbf.py          # Gurobi model
│   └── generate_instances.py  # Instance generator
└── pyproject.toml             # Poetry configuration file
```

---

## References

* [Gurobi Documentation](https://www.gurobi.com/documentation/)
* [Poetry Documentation](https://python-poetry.org/)
