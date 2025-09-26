def main():
    num_cases = int(input().strip())

    for case in range(num_cases):
        # X and Y length between 1 and 1000
        X, Y = list(input().strip()), list(input().strip())

        # print(X)
        # print(Y)

        # from https://leetcode.com/problems/longest-common-subsequence/solutions/4622129/beats-100-dynamic-programming-c-java-python-js-explained-with-video
        # Get the lengths of both input strings
        len_X, len_Y = len(X), len(Y)

        # Initialize a 2D array (list of lists) with zeros for dynamic programming
        # The array has (len_X + 1) rows and (len_Y + 1) columns
        dp_matrix = []
        for _ in range(len_X + 1):
            dp_matrix.append([0] * (len_Y + 1))

        # Loop through each character index of X and Y
        for i in range(1, len_X + 1):
            for j in range(1, len_Y + 1):
                # If the characters match, take the diagonal value and add 1
                if X[i - 1] == Y[j - 1]:
                    dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
                else:
                    # If the characters do not match, take the maximum of the value from the left and above
                    dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])

        print(f"Case {case+1}: {dp_matrix[len_X][len_Y]}")


if __name__ == '__main__':
    main()