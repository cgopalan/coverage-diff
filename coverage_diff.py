"""
    Determines the difference in statistics between two coverage files,
    the first arg being the existing coverage file and the second being
    the new coverage files.
    Prints the following:
    As a result of the new coverage file,
    1. What modules have increased coverage
    2. What modules have decreased coverage.
    3. What modules have been added.
    4. What modules have been removed.

    Things to do:
    Coverage threshold checks.
"""


from pandas.io.parsers import read_fwf
import sys


def get_coverage_dfs(f_cov_exist, f_cov_new):
    """ Gives differential info between two coverage files. """

    kwargs = {'widths': [69, 5, 7, 6], 'header': 0,
              'names': ['Name', 'Stmts', 'Miss', 'Cover'],
              'skipfooter': 6,
              'index_col': 'Name'}

    kwargs['skiprows'] = get_first_valid_line(f_cov_exist)
    df_exist = read_fwf(f_cov_exist, **kwargs)

    kwargs['skiprows'] = get_first_valid_line(f_cov_new)
    df_new = read_fwf(f_cov_new, **kwargs)
    import ipdb; ipdb.set_trace()
    return (df_exist, df_new)


def get_first_valid_line(f_cov):
    """ Get the first line that has valid data. """
    with open(f_cov) as f:
        for line_no, line in enumerate(f):
            if line.startswith('-'*98):
                return line_no
        else:
            return 0


def print_stats(f_cov_exist, f_cov_new):
    df_exist, df_new = get_coverage_dfs(f_cov_exist, f_cov_new)
    print("\n")
    print(" --------- Printing Coverage Diff Stats -------- ")
    print("\n")
    print("The following modules have INCREASED coverage now.")
    print(df_new[df_new.Cover - df_exist.Cover > 0])
    print("\n")
    print("The following modules have DECREASED coverage now.")
    print(df_new[df_new.Cover - df_exist.Cover < 0])
    print("\n")
    added = df_new.index -df_exist.index
    if len(added) > 0:
        print("The following modules have been added.")
        for x in added:
            print(df_new.ix[x])
        print("\n")
    removed = df_exist.index - df_new.index
    if len(removed) > 0:
        print("The following modules have been removed.")
        for x in removed:
            print(df_exist.ix[x])
        print("\n")


if __name__ == '__main__':
    #df_exist, df_new = get_coverage_dfs(sys.argv[1], sys.argv[2])
    print_stats(sys.argv[1], sys.argv[2])
