from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def print_most_correlated_to(attr, correlation_values, data):
    columns = list(data.columns)
    columns = [c.strip() for c in columns]
    index_of_attr = columns.index(attr)
    attr_row = correlation_values[index_of_attr]
    max_correlation_attr = np.amax(np.absolute(attr_row))
    max_correlation_attr_index = np.where(np.absolute(attr_row) == max_correlation_attr)[0][0]
    correlated_column_name = data.columns[max_correlation_attr_index].strip()
    max_correlation_value = correlation_values[index_of_attr, max_correlation_attr_index]
    print("{} most correlated to {} : {}".format(attr, correlated_column_name, max_correlation_value))

def print_correlation(abs_correlation_value, correlation_values, message):
    correlation_index = np.where(np.absolute(correlation_values) == abs_correlation_value)[0]
    correlated_column_name_0 = data.columns[correlation_index[0]].strip()
    correlated_column_name_1 = data.columns[correlation_index[1]].strip()
    correlation_value = correlation_values[correlation_index[0], correlation_index[1]]
    print("{} {}-{} : {}".format(message, correlated_column_name_0, correlated_column_name_1, correlation_value))

if __name__ == "__main__":
    #read the data
    data = pd.read_csv("HW_PCA_SHOPPING_CART_v892.csv")
    #removing id
    data = data.drop(columns=["ID"])
    #compute the correlation matrix
    correlation_matrix = data.corr()
    #plot the correlation matrix as a color map
    plt.matshow(correlation_matrix)
    plt.xticks(range(len(data.columns)), data.columns)
    plt.yticks(range(len(data.columns)), data.columns)
    plt.colorbar()
    plt.show()
    correlation_values = correlation_matrix.values
    np.fill_diagonal(correlation_values, 0)
    # strongest correlated attribute with attr
    print_most_correlated_to("Fish", correlation_values, data)
    print_most_correlated_to("Meat", correlation_values, data)
    print_most_correlated_to("Beans", correlation_values, data)
    #Get unique absolute correlation values sorted ignoring diagonals
    correlation_values_flat=np.absolute(correlation_values.flatten())
    correlation_values_flat.sort()
    correlation_values_flat = np.unique(correlation_values_flat)[1:]
    #max correlated
    max_correlation = correlation_values_flat[-1]
    print_correlation(max_correlation, correlation_values, "Highest correlated")
    #min correlated
    min_correlation = correlation_values_flat[0]
    print_correlation(min_correlation, correlation_values, "Least correlated")
    #second min correlated
    second_min_correlation = correlation_values_flat[1]
    print_correlation(second_min_correlation, correlation_values, "Second Least correlated ")