import numpy as np
from sklearn.decomposition import PCA

class PrincipalComponentAnalysis:
    def __init__(self):
        self.pca = PCA()

    def determine_pc_explained_variance(self, data_table, cols):
        # Normalize the data
        dt_norm = self._normalize_dataset(data_table, cols)

        # Perform PCA
        self.pca.fit(dt_norm[cols])

        # Return explained variances
        return self.pca.explained_variance_ratio_

    def apply_pca(self, data_table, cols, number_comp):
        # Normalize the data
        dt_norm = self._normalize_dataset(data_table, cols)

        # Perform PCA
        self.pca = PCA(n_components=number_comp)
        new_values = self.pca.fit_transform(dt_norm[cols])

        # Add new PCA columns
        for comp in range(number_comp):
            data_table[f'pca_{comp+1}'] = new_values[:, comp]

        return data_table

    def _normalize_dataset(self, data_table, cols):
        # Assuming you have a separate normalization method
        # Here we are just using a placeholder method
        return data_table  # Placeholder for normalization
