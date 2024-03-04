from scipy.signal import butter, filtfilt, lfilter
'''
A Butterworth low-pass filter is a type of filter that is used to remove high frequency noise from a dataset. 
It is most commonly used in machine learning in order to improve the accuracy of the model. The filter works by removing any data points above a certain threshold frequency, 
while still preserving the underlying pattern of the data. By doing so, it helps to reduce the effect of noise on the model, which can lead to better results.
'''

# Source: Hoogendoorn, M., & Funk, B. (2018). Machine learning for the quantified self. On the art of learning from sensory data. In 2018 International Conference of Machine Learning (ICML) (pp. 1-8).
# https://github.com/mhoogen/ML4QS/tree/master

class LowPassFilter:
    def __init__(self):
        pass  # If there are any initializations required, they can be added here

    def apply_low_pass_filter(self, data_table, column, sampling_frequency, cutoff_frequency, order=5, phase_shift=True):
        """
        Apply a low-pass filter to the specified column of the dataset.

        Args:
            data_table (DataFrame): The input dataset.
            column (str): The column name to filter.
            sampling_frequency (float): The sampling frequency of the data.
            cutoff_frequency (float): The cutoff frequency for the filter.
            order (int): The order of the filter. Defaults to 5.
            phase_shift (bool): Whether to apply phase shift. Defaults to True.

        Returns:
            DataFrame: The dataset with the filtered column added.
        """
        # Calculate the Nyquist frequency
        nyquist_frequency = 0.5 * sampling_frequency

        # Calculate the normalized cutoff frequency
        normalized_cutoff = cutoff_frequency / nyquist_frequency

        # Design the Butterworth filter
        b, a = butter(order, normalized_cutoff, btype="low", output="ba", analog=False)

        # Apply the filter
        if phase_shift:
            filtered_column = filtfilt(b, a, data_table[column])
        else:
            filtered_column = lfilter(b, a, data_table[column])

        # Add the filtered column to the dataset
        data_table[column + "_lowpass"] = filtered_column

        return data_table
