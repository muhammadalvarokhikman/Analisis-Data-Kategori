import math

# Data diambil dari tabel kontingensi
a = 14
b = 6
c = 6
d = 24

# Menghitung Q Yule
Q_yule = (a * d - b * c) / (a * d + b * c)
print("Q Yule:", Q_yule)

# Menghitung relative risk ke-1
RR = (a / (a + b)) / (c / (c + d))
SE_ln_RR = math.sqrt((1/a) - (1/(a+b)) + (1/c) - (1/(c+d)))
upper_limit_RR = math.exp(math.log(RR) + 1.96 * SE_ln_RR)
lower_limit_RR = math.exp(math.log(RR) - 1.96 * SE_ln_RR)
print("Relative Risk (RR):")
print(RR)
print("Rentang kepercayaan 95% untuk RR:")
print("(", lower_limit_RR, "-", upper_limit_RR, ")")

# Menghitung relative risk ke-2
a = 6
b = 20 - a
c = 24
d = 30 - c

RR = (a / (a + b)) / (c / (c + d))
SE_ln_RR = math.sqrt((1/a) - (1/(a+b)) + (1/c) - (1/(c+d)))
upper_limit_RR = math.exp(math.log(RR) + 1.96 * SE_ln_RR)
lower_limit_RR = math.exp(math.log(RR) - 1.96 * SE_ln_RR)
print("Relative Risk (RR):")
print(RR)
print("Rentang kepercayaan 95% untuk RR:")
print("(", lower_limit_RR, "-", upper_limit_RR, ")")

# Menghitung odds ratio
a = 14
b = 6
c = 6
d = 24
OR = (a * d) / (b * c)
SE_ln_OR = math.sqrt((1/a) + (1/b) + (1/c) + (1/d))
upper_limit_OR = math.exp(math.log(OR) + 1.96 * SE_ln_OR)
lower_limit_OR = math.exp(math.log(OR) - 1.96 * SE_ln_OR)
print("Odds Ratio (OR):")
print(OR)
print("Rentang kepercayaan 95% untuk OR:")
print("(", lower_limit_OR, "-", upper_limit_OR, ")")
