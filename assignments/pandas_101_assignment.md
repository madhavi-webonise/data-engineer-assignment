# Pandas 101 Assignment

Source: [MachineLearningPlus - 101 Pandas Exercises for Data Analysis (Interactive)](https://machinelearningplus.com/python/101-pandas-exercises-python-interactive/)

This assignment is adapted from the linked Pandas exercise set. The current interactive page exposes 75 exercises, so this repository assignment follows those 75 prompts while keeping the original Pandas 101 theme.

## Objective

Practice core pandas skills needed for day-to-day data work:

- creating and transforming `Series` and `DataFrame` objects
- handling text, dates, missing values, and indexing
- importing data and reshaping tabular datasets
- applying grouping, joining, correlation, and feature-engineering patterns

## Instructions

1. Solve the exercises in order in a Jupyter notebook or Python script.
2. Use `pandas` and `numpy` unless a prompt clearly requires another standard-library helper.
3. Keep your code readable and add short notes only where your approach is not obvious.
4. Validate your output against the source exercise page when an example result is provided.

## Suggested Deliverables

1. A notebook such as `solutions/pandas_101_solutions.ipynb`, or a script such as `solutions/pandas_101_solutions.py`.
2. Clear section headers matching the exercise numbers below.
3. A short note at the end listing the exercises you completed independently vs. the ones that needed references.

## Exercise List

### Part 1: Series Basics

1. How to import pandas and check the version?
2. How to create a series from a list, numpy array and dict?
3. How to convert the index of a series into a column of a dataframe?
4. How to combine many series to form a dataframe?
5. How to assign name to the series' index?
6. How to get the items of series A not present in series B?
7. How to get the items not common to both series A and series B?
8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
9. How to get frequency counts of unique items of a series?
10. How to keep only top 2 most frequent values as it is and replace everything else as `Other`?
11. How to bin a numeric series to 10 groups of equal size?
12. How to convert a numpy array to a dataframe of given shape? (`L1`)
13. How to find the positions of numbers that are multiples of 3 from a series?
14. How to extract items at given positions from a series?
15. How to stack two series vertically and horizontally?
16. How to get the positions of items of series A in another series B?
17. How to compute the mean squared error on a truth and predicted series?
18. How to convert the first character of each element in a series to uppercase?
19. How to calculate the number of characters in each word in a series?
20. How to compute difference of differences between consecutive numbers of a series?

### Part 2: Dates, Text, and Time Series

21. How to convert a series of date-strings to a timeseries?
22. How to get the day of month, week number, day of year and day of week from a series of date strings?
23. How to convert year-month string to dates corresponding to the 4th day of the month?
24. How to filter words that contain at least 2 vowels from a series?
25. How to filter valid emails from a series?
26. How to get the mean of a series grouped by another series?
27. How to compute the euclidean distance between two series?
28. How to find all the local maxima (or peaks) in a numeric series?
29. How to replace missing spaces in a string with the least frequent character?
30. How to create a `TimeSeries` starting `2000-01-01` and 10 weekends (Saturdays) after that with random numbers as values?
31. How to fill an intermittent time series so all missing dates show up with values of previous non-missing date?
32. How to compute the autocorrelations of a numeric series?

### Part 3: Importing and Inspecting Data

33. How to import only every nth row from a CSV file to create a dataframe?
34. How to change column values when importing CSV to a dataframe?
35. How to create a dataframe with rows as strides from a given series?
36. How to import only specified columns from a CSV file?
37. How to get the `nrows`, `ncolumns`, datatype, summary stats of each column of a dataframe? Also get the array and list equivalent.
38. How to extract the row and column number of a particular cell with given criterion?
39. How to rename a specific columns in a dataframe?
40. How to check if a dataframe has any missing values?
41. How to count the number of missing values in each column?
42. How to replace missing values of multiple numeric columns with the mean?
43. How to use `apply()` function on existing columns with global variables as additional arguments?
44. How to select a specific column from a dataframe as a dataframe instead of a series?
45. How to change the order of columns of a dataframe?
46. How to set the number of rows and columns displayed in the output?
47. How to format or suppress scientific notations in a pandas dataframe?

### Part 4: Row and Column Transformations

48. How to format all the values in a dataframe as percentages?
49. How to filter every nth row in a dataframe?
50. How to create a primary key index by combining relevant columns?
51. How to get the row number of the nth largest value in a column?
52. How to find the position of the nth largest value greater than a given value?
53. How to get the last n rows of a dataframe with row sum > 100?
54. How to find and cap outliers from a series or dataframe column?
55. How to reshape a dataframe to the largest possible square after removing the negative values?
56. How to swap two rows of a dataframe?
57. How to reverse the rows of a dataframe?
58. How to create one-hot encodings of a categorical variable (dummy variables)?
59. Which column contains the highest number of row-wise maximum values?
60. How to create a new column that contains the row number of nearest column by euclidean distance?
61. How to know the maximum possible correlation value of each column against other columns?
62. How to create a column containing the minimum by maximum of each row?

### Part 5: Advanced DataFrame Operations

63. How to create a column that contains the penultimate value in each row?
64. How to normalize all columns in a dataframe?
65. How to compute the correlation of each row with the succeeding row?
66. How to replace both the diagonals of dataframe with `0`?
67. How to get the particular group of a `groupby` dataframe by key?
68. How to get the nth largest value of a column when grouped by another column?
69. How to compute grouped mean on pandas dataframe and keep the grouped column as another column (not index)?
70. How to join two dataframes by 2 columns so they have only the common rows?
71. How to remove rows from a dataframe that are present in another dataframe?
72. How to get the positions where values of two columns match?
73. How to create lags and leads of a column in a dataframe?
74. How to get the frequency of unique values in the entire dataframe?
75. How to split a text column into two separate columns?

## Completion Tracking

- Foundation complete: Exercises 1-20
- Intermediate complete: Exercises 21-47
- Advanced complete: Exercises 48-75

## Notes

- Follow the source page for example inputs and expected outputs.
- Prefer vectorized pandas solutions over manual Python loops unless the exercise specifically calls for a different approach.
