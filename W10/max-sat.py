def main():
    # NUMBER OF VARIABLES AND NUMBER OF CLAUSES RESPECTIVELY.
    n, m = map(int, input().strip().split())

    # Read clauses and weights
    clauses = []
    weights = []
    for i in range(m):
        line = input().strip().split()

        length = int(line[0]) # no need this time, but it's good to have more info
        weight = int(line[1])

        clause = []

        for j in range(2, len(line)):
            clause.append(int(line[j]))

        clauses.append(clause)
        weights.append(weight)

    # we want to check via brute-force, for every assignment to variables (tau), if it is satisfiable.
    found = False  # have we found satisfying assignment?
    max_weight = 0
    for tau in range(1 << n):  # all 2^n assignments

        total_weight = 0 # keep track of total_weight for current tau
        sat = True  # does tau satisfy all the clauses so far?

        for idx, clause in enumerate(clauses):

            # check if tau satisfies current clause
            cl_sat = False

            for lit in clause:

                # checks if literal is satisfied
                # variable i corresponds to position (i-1) in tau, due to indexing differences
                var_index = abs(lit) - 1
                var_value = (tau >> var_index) & 1  # 1 if true, 0 if false

                # if literal appears positively, it is satisfied when corresponding variable is set to true in tau
                if lit > 0 and var_value == 1:
                    cl_sat = True
                    break

                # if literal appears negatively, it is satisfied when corresponding variable is set to false in tau
                if lit < 0 and var_value == 0:
                    cl_sat = True
                    break

            # end of lit loop

            if cl_sat:
                total_weight += weights[idx]

            # this tau does not satisfy all clauses
            if not cl_sat:
                sat = False
                # break # DO NOT BREAK, WE STILL NEED TO VERIFY THE REMAINING CLAUSES

        # end of clause loop

        # see if this tau's total weight is higher than max weight seen so far
        if total_weight > max_weight:
            max_weight = total_weight

        # found satisfying assignment
        if sat:
            found = True
            break

    # end of tau loop

    # output result
    if found:
        print("satisfiable")
    else:
        print(f'not satisfiable {max_weight}')


if __name__ == "__main__":
    main()