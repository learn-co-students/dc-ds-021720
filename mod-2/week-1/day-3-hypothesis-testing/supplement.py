seniors = df[df['SeniorCitizen'] == 1]
others = df[df['SeniorCitizen'] == 0]

seniors.shape
others.shape

mailed_checks = df[df.PaymentMethod == "Mailed check"].MonthlyCharges
import scipy.stats as stats
stats.ttest_1samp(mailed_checks, popmean= 70)

stats.ttest_ind(seniors.MonthlyCharges,others.MonthlyCharges,equal_var= False)