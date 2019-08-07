library(MatchIt)

mydata <- na.omit(sig_vars_periph2)
attach(sig_vars_periph_na)
sig_vars_periph_na[1:10,]

m.out = matchit(group2 ~ age, data = sig_vars_periph_na, method = "nearest", ratio = 1)
summary(m.out)
plot(m.out, type = "jitter")
plot(m.out, type = "hist")

detach(sig_vars_periph_na)

mydata <- na.omit(sig_vars)
warnings()
attach(mydata)
mydata[1:10,]
m.out = matchit(group ~ age, data = sig_vars, method = "nearest", ratio = 1)
summary(m.out)
plot(m.out, type = "hist")


mydata <- na.omit(sig_vars_loose)
warnings()
attach(mydata)
mydata[1:10,]
m.out = matchit(group ~ age, data = sig_vars, method = "nearest", ratio = 1)
summary(m.out)
plot(m.out, type = "hist")
