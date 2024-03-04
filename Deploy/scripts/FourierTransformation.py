import numpy as np

# Source: Hoogendoorn, M., & Funk, B. (2018). Machine learning for the quantified self. On the art of learning from sensory data. In 2018 International Conference of Machine Learning (ICML) (pp. 1-8).
# https://github.com/mhoogen/ML4QS/tree/master
class FourierTransformation:
    def __init__(self):
        pass  # If there are any initializations required, they can be added here

    def find_fft_transformation(self, data, sampling_rate):
        """
        Perform Fast Fourier Transformation to find the amplitudes of different frequencies.

        Args:
            data (array-like): The input data array.
            sampling_rate (float): The sampling rate (samples per second) of the data.

        Returns:
            tuple: A tuple containing the real and imaginary parts of the transformation.
        """
        transformation = np.fft.rfft(data, len(data))
        return transformation.real, transformation.imag

    def abstract_frequency(self, data_table, cols, window_size = 14, sampling_rate = 5):
        """
        Abstract frequency information from numerical columns using Fast Fourier Transformation.

        Args:
            data_table (DataFrame): The input dataset.
            cols (list of str): The list of column names to abstract frequency information from.
            window_size (int): The size of the window to compute frequencies over.
            sampling_rate (float): The sampling rate (samples per second) of the data.

        Returns:
            DataFrame: The dataset with frequency-related columns added.
        """
        freqs = np.round((np.fft.rfftfreq(int(window_size)) * sampling_rate), 3)

        # Iterate over each column to compute frequency information
        for col in cols:
            # Add new columns for frequency data
            data_table[col + "_max_freq"] = np.nan
            data_table[col + "_freq_weighted"] = np.nan
            data_table[col + "_pse"] = np.nan
            for freq in freqs:
                data_table[col + f"_freq_{freq}_Hz_ws_{window_size}"] = np.nan

        # Iterate over the dataset to compute frequency values
        for i in range(window_size, len(data_table.index)):
            for col in cols:
                real_ampl, _ = self.find_fft_transformation(
                    data_table[col].iloc[i - window_size : min(i + 1, len(data_table.index))],
                    sampling_rate,
                )
                for j, freq in enumerate(freqs):
                    data_table.loc[
                        i, col + f"_freq_{freq}_Hz_ws_{window_size}"
                    ] = real_ampl[j]

                # Select the dominant frequency and compute other frequency-related metrics
                max_freq_index = np.argmax(real_ampl[0 : len(real_ampl)])
                data_table.loc[i, col + "_max_freq"] = freqs[max_freq_index]
                data_table.loc[i, col + "_freq_weighted"] = np.sum(freqs * real_ampl) / np.sum(real_ampl)
                PSD = np.square(real_ampl) / float(len(real_ampl))
                PSD_pdf = PSD / np.sum(PSD)
                data_table.loc[i, col + "_pse"] = -np.sum(np.log(PSD_pdf) * PSD_pdf)

        return data_table
