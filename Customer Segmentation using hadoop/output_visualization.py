import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Load the output file directly into a DataFrame
output_file = 'C:/Users/Lenovo/Desktop/cleaning/output.txt'
df = pd.read_csv(output_file, sep='\t', header=None, names=['Service_Combination', 'Customer_IDs', 'Cluster'])

# Expand DataFrame and split service combination into separate columns
df_expanded = df['Service_Combination'].str.split(',', expand=True)
df_expanded.columns = ['Phone_Service', 'Multiple_Lines', 'Internet_Service', 'Online_Security',
                       'Online_Backup', 'Device_Protection', 'Tech_Support', 'Streaming_TV', 'Streaming_Movies']
df_expanded['Customer_IDs'] = df['Customer_IDs']
df_expanded['Cluster'] = df['Cluster']

# Encode categorical variables
df_encoded = pd.get_dummies(df_expanded.drop(['Customer_IDs', 'Cluster'], axis=1))

# Apply PCA to reduce dimensions
pca = PCA(n_components=2)
pca_components = pca.fit_transform(df_encoded)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=5)
clusters = kmeans.fit_predict(pca_components)

# Plot scatter plot of PCA components with cluster labels
plt.figure(figsize=(10, 6))
sns.scatterplot(x=pca_components[:, 0], y=pca_components[:, 1], hue=clusters, palette='viridis', s=100)
plt.title('Customer Segments Based on Service Usage (PCA + K-Means)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend(title='Cluster')

# Show the scatter plot
plt.show()

# Simplify column names for better visualization
df_encoded.columns = df_encoded.columns.str.replace('True', '').str.replace('False', '')

# Plot heatmap of service usage by each cluster
plt.figure(figsize=(12, 8))
sns.heatmap(df_encoded.assign(Cluster=clusters).groupby('Cluster').mean(), cmap='coolwarm', annot=True, fmt=".2f")

# Customize plot for readability
plt.title('Service Usage by Cluster')
plt.xlabel('Services')
plt.ylabel('Cluster')
plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotate x-axis labels for better readability

# Show the heatmap
plt.show()
