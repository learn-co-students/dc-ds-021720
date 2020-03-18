import statsmodels.api as sm

Xconst = sm.add_constant(X)

model = sm.OLS(y, Xconst, hasconst= True)

fitted_model = model.fit()

fitted_model.summary()