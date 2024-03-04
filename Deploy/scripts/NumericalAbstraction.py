import numpy as np

'''
Temporal abstraction using rolling windows and aggregation functions.
'''
# Source: Hoogendoorn, M., & Funk, B. (2018). Machine learning for the quantified self. On the art of learning from sensory data. In 2018 International Conference of Machine Learning (ICML) (pp. 1-8).
# https://github.com/mhoogen/ML4QS/tree/master

class NumericalAbstraction:
    def __init__(self):
        pass  # If there are any initializations required, they can be added here

    def aggregate_value(self, aggregation_function):
        """
        Return the numpy function corresponding to the specified aggregation function.

        Args:
            aggregation_function (str): The aggregation function name ('mean', 'max', 'min', 'median', 'std').

        Returns:
            function: The numpy aggregation function.
        """
        # Map aggregation functions to numpy functions
        aggregation_mapping = {
            "mean": np.mean,
            "max": np.max,
            "min": np.min,
            "median": np.median,
            "std": np.std
        }
        # Return the corresponding numpy function, or np.nan if not found
        return aggregation_mapping.get(aggregation_function, np.nan)

    def abstract_numerical(self, data_table, cols, window_size, aggregation_function):
        """
        Abstract numerical columns in the dataset using a rolling window and specified aggregation function.

        Args:
            data_table (DataFrame): The input dataset.
            cols (list of str): The list of column names to abstract.
            window_size (int): The size of the rolling window.
            aggregation_function (str): The aggregation function to use ('mean', 'max', 'min', 'median', 'std').

        Returns:
            DataFrame: The dataset with abstracted numerical columns added.
        """
        # Iterate over each column to abstract
        for col in cols:
            # Generate the new column name based on aggregation function and window size
            new_col_name = f"{col}_temp_{aggregation_function}_ws_{window_size}"
            # Apply the rolling window and aggregation function, and store the result in a new column
            data_table[new_col_name] = (
                data_table[col]
                .rolling(window_size)
                .apply(self.aggregate_value(aggregation_function))
            )

        return data_table
