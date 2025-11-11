# 1 for the clause reading part
# 2 for the satisfying assignment search
DEBUG_LEVEL = 0

def print_clause(clause_num: int, clauses: list[list[int]]) -> None:
    print("Clause :", end='')
    for var in clauses[clause_num]:
        print(f" {var}", end='')
    print()

def print_assignment(n: int, tau: int) -> None:
    print(f"assignment corresponding to {tau}")

    for i in range(n):
        print(f"\tx_{i+1}=", end='')

        if tau & (1 << i):
            print("true", end='')
        else:
            print("false", end='')

        print()

def main():
    # NUMBER OF TEST CASES
    t = int(input().strip())

    for zzz in range(t):
        if DEBUG_LEVEL >= 1:
            print(f"Test Case: {zzz + 1}")

        # NUMBER OF VARIABLES AND NUMBER OF CLAUSES RESPECTIVELY.
        n, m = map(int, input().strip().split())

        # Read clauses
        clauses = []
        for i in range(m):
            line = input().strip().split()
            clause = []
            for tok in line:
                if tok[0] == 'v':
                    continue

                sign = 1
                j = 0

                if tok[0] == '~':
                    sign = -1
                    j = 2  # skip '~x'
                else:
                    j = 1  # skip 'x'

                var = int(tok[j:])  # parse digits after 'x'
                clause.append(sign * var)

            clauses.append(clause)
            if DEBUG_LEVEL == 1:
                print_clause(i, clauses)

        # end of clause reading loop

        """
        
        Reminder:
            
            1. << shifts the bits to the left by a given number of positions.
               Given the input, 1 << n would be 1 << 3 and 1 << 3 (because of lines 3 3 and 3 5)
               Therefore, we would have 2^3 assignments
               
            2. >> shifts the bits to the right by a given number of positions.
               It is used in var_value = (tau >> var_index) & 1
               Therefore, this only returns 1 if we have the rightmost bit as 1, and everything else 0 for (tau >> var_index).
               
            3. & is the bitwise AND operator
        
        """

        # we want to check via brute-force, for every assignment to variables (tau), if it is satisfiable.
        # set DEBUG_LEVEL = 2 to see the assignment to variables
        if DEBUG_LEVEL == 2:
            print(clauses)


        found = False # have we found satisfying assignment?
        for tau in range(1 << n):  # all 2^n assignments

            if DEBUG_LEVEL == 2:
                print_assignment(n, tau)

            sat = True # does tau satisfy all the clauses so far?

            for clause in clauses:

                # check if tau satisfies clause 1
                cl_sat = False

                for lit in clause:

                    # checks if literal is satisfied
                    # variable i corresponds to position (i-1) in tau (but why?)
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

                # this tau does not satisfy all clauses
                if not cl_sat:
                    sat = False
                    break

            # end of clause loop

            # found satisfying assignment
            if sat:
                found = True
                break

        # end of tau loop

        # output result
        if found:
            print("satisfiable")
        else:
            print("unsatisfiable")


if __name__ == "__main__":
    main()