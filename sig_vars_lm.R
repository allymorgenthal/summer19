no.na.data <- na.omit(sig_vars)
fitall <- glm(group ~ ., data = no.na.data, family=binomial(link='logit'))
fitstart <- glm(group ~ 1, data = no.na.data, family=binomial(link='logit'))
step(fitstart, direction = "forward", scope=formula(fitall))

outcome <- "group"
variables <- c("age", "rfm", "Volume_of_grey_matter_in_Occipital_Pole_(right)", "rfmri.25.edge.130", 
               "rfmri.100.edge.920", "gender", "rfmri.25.edge.101", "Mean_FA_in_cingulum_hippocampus_on_FA_skeleton_.right.", 
               "delta1.deconf", "delta1")
f <- as.formula(
  paste(outcome, 
        paste(variables, collapse = " + "), 
        sep = " ~ "))
print(f)

model <- lm(f, data = no.na.data)
print(model)


no.na.data <- na.omit(sig_vars_periph)
fitall <- glm(group ~ ., data = no.na.data, family=binomial(link='logit'))
fitstart <- glm(group ~ 1, data = no.na.data, family=binomial(link='logit'))
step(fitstart, direction = "forward", scope=formula(fitall))







