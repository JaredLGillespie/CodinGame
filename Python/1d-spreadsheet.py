# https://www.codingame.com/training/easy/1d-spreadsheet


def add_dependency(cell, arg_cell, in_deps, out_deps):
    if cell not in out_deps: out_deps[cell] = set()
    out_deps[cell].add(arg_cell)

    if arg_cell not in in_deps: in_deps[arg_cell] = set()
    in_deps[arg_cell].add(cell)


def remove_dependency(cell, in_deps, out_deps):
    rc = []
    if cell not in in_deps: return rc
    for o in in_deps[cell]:
        if cell in out_deps[o]:
            out_deps[o].remove(cell)

        if not out_deps[o]:
            rc.append(o)

    return rc


def evaluate_dependencies(cells, in_deps, out_deps, cell_operations):
    ready_cells = set()
    evaluated_cells = set()

    for cell in out_deps:
        if not out_deps[cell]:
            ready_cells.add(cell)

    while ready_cells:
        cell = ready_cells.pop()
        evaluated_cells.add(cell)
        perform_operation(cell=cell, **cell_operations[cell], cells=cells)
        rc = remove_dependency(cell, in_deps, out_deps)

        ready_cells.update([o for o in rc if o not in evaluated_cells])

    for cell in cells:
        print(cell)


def get_arg_val(arg, cells):
    if '$' in arg:
        return cells[int(arg[1:])]
    elif '_' in arg:
        return 0
    else:
        return int(arg)


def perform_operation(cell, operation, arg1, arg2, cells):
    val1 = get_arg_val(arg1, cells)
    val2 = get_arg_val(arg2, cells)

    if operation == 'VALUE':
        cells[cell] = val1
    elif operation == 'ADD':
        cells[cell] = val1 + val2
    elif operation == 'SUB':
        cells[cell] = val1 - val2
    else:
        cells[cell] = val1 * val2


def solution():
    num_cells = int(input())
    in_deps = {}
    out_deps = {}
    cells = [0] * num_cells
    cell_operations = [{} for _ in range(num_cells)]

    for cell in range(num_cells):
        operation, arg1, arg2 = input().split()
        cell_operations[cell] = {
            'operation': operation,
            'arg1': arg1,
            'arg2': arg2
        }

        if cell not in out_deps: out_deps[cell] = set()
        if '$' in arg1: add_dependency(cell, int(arg1[1:]), in_deps, out_deps)
        if '$' in arg2: add_dependency(cell, int(arg2[1:]), in_deps, out_deps)

    evaluate_dependencies(cells, in_deps, out_deps, cell_operations)


solution()
