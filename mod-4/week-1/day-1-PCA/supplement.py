Xpca = pca.transform(X)

plt.scatter(Xpca[:,0], Xpca[:,1])
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.show()

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(X)


pca = PCA(n_components=1)
pca.fit(X)
Xpca = pca.transform(X)
X_new = pca.inverse_transform(Xpca)
plt.scatter(X[:, 0], X[:, 1])
plt.scatter(X_new[:, 0], X_new[:, 1], alpha=0.6)
plt.axis('equal');

## After Standard Scaling
## Note that in general using PCA with StantardScaler is a good idea
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

X = ss.fit_transform(X)

plt.scatter(X[:,0], X[:,1])
plt.show()