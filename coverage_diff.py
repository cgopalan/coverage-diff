"""
    Determines the difference in statistics between two coverage files.
    1. For each module in file 1, check the coverage percentage in file2.
    2. If the module exists, add the coverage percentage of file2.
    3. If module does not exist, add it to removed modules list.
    4. If there are modules remaining in file2, add it to new modules list.
    5. Calculate the diff of the percentages as a new column.
    6. If diff column is positive, add to increased coverage list.
    7. If diff column is negative add to decreased coverage list.
"""

from pandas.io.parsers import read_fwf
import sys


def get_coverage_dfs(f_cov_exist, f_cov_new):
    """ Gives differential info between two coverage files. """
    skiprows = get_first_valid_line(f_cov_exist)
    kwargs = {'widths': [69,5,7,6], 'header': 0,
              'names': ['Name', 'Stmts', 'Miss', 'Cover'],
              'skiprows': skiprows,
              'skipfooter': 6}
    return (read_fwf(f_cov_exist, **kwargs),
            read_fwf(f_cov_new, **kwargs))


def get_first_valid_line(f_cov):
    """ Get the first line that has valid data. """
    with open(f_cov) as f:
        for line_no, line in enumerate(f):
            if line.startswith('-------'):
                return line_no
        else:
            return 0

def print_stats(f_cov_exist, f_cov_new):
    df_exist, df_new = get_coverage_dfs(f_cov_exist, f_cov_new)


if __name__ == '__main__':
    df_exist, df_new = get_coverage_dfs(sys.argv[1], sys.argv[2])
    #print_stats(sys.argv[1], sys.argv[1])
