library(MASS)
# Fit the full model 
full.model <- lm(Fertility ~., data = swiss)
# Stepwise regression model
step.model <- stepAIC(full.model, direction = "both", 
                      trace = FALSE)
summary(step.model)

full.model <- lm(group2 ~ age + gender + rfm + delta1 + rfmri.100.edge.251 + Mean_OD_in_superior_corona_radiata_on_FA_skeleton_.left. 
                 + rfmri.100.edge.851 + rfmri.100.edge.782 + rfmri.25.edge.184 + delta1.deconf + Volume_of_grey_matter_in_Occipital_Pole_.right. 
                 + rfmri.25.edge.101 + rfmri.100.edge.164 + rfmri.100.edge.262 + rfmri.25.edge.180 + rfmri.100.edge.1220 
                 + Mean_FA_in_cingulum_hippocampus_on_FA_skeleton_.right. + rfmri.100.edge.698 + Mean_OD_in_cingulum_hippocampus_on_FA_skeleton_.left. 
                 + Mean_FA_in_superior_corona_radiata_on_FA_skeleton_.left. + rfmri.100.edge.1067 + rfmri.100.edge.33 + 
                   Mean_MO_in_cingulum_hippocampus_on_FA_skeleton_.left. + Mean_OD_in_cingulum_hippocampus_on_FA_skeleton_.right., data = sig_vars_loose)
step.model <- stepAIC(full.model, direction = "both", trace = TRUE)
summary(step.model)


fitall <- glm(group ~ age + gender + rfm + delta1 + rfmri.100.edge.251 + Mean_OD_in_superior_corona_radiata_on_FA_skeleton_.left. 
             + rfmri.100.edge.851 + rfmri.100.edge.782 + rfmri.25.edge.184 + delta1.deconf + Volume_of_grey_matter_in_Occipital_Pole_.right. 
             + rfmri.25.edge.101 + rfmri.100.edge.164 + rfmri.100.edge.262 + rfmri.25.edge.180 + rfmri.100.edge.1220 
             + Mean_FA_in_cingulum_hippocampus_on_FA_skeleton_.right. + rfmri.100.edge.698 + Mean_OD_in_cingulum_hippocampus_on_FA_skeleton_.left. 
             + Mean_FA_in_superior_corona_radiata_on_FA_skeleton_.left. + rfmri.100.edge.1067 + rfmri.100.edge.33 + 
               Mean_MO_in_cingulum_hippocampus_on_FA_skeleton_.left. + Mean_OD_in_cingulum_hippocampus_on_FA_skeleton_.right., data = sig_vars_loose, family=binomial(link='logit'))
fitstart <- glm(group ~ 1, data = sig_vars_loose, family=binomial(link='logit'))
step(fitstart, direction = "forward", scope=formula(fitall))

fitall <- glm(group ~ ., data = sig_vars_loose, family=binomial(link='logit'))
fitstart <- glm(group ~ 1, data = sig_vars_loose, family=binomial(link='logit'))
step(fitstart, direction = "forward", scope=formula(fitall))

fitall <- glm(group ~ age + rfm + delta1 + delta1.deconf + Volume_of_grey_matter_in_Occipital_Pole_.right.
              + Weighted.mean_L1_in_tract_middle_cerebellar_peduncle + rfmri.100.edge.251 + rfmri.25.edge.130 
              + Weighted.mean_OD_in_tract_middle_cerebellar_peduncle, data = sig_vars_periph2, family=binomial(link='logit'))
fitstart <- glm(group ~ 1, data = sig_vars_periph2, family=binomial(link='logit'))
step(fitstart, direction = "forward", scope=formula(fitall))




full.model <- lm(group2 ~ age + rfm + delta1 + delta1.deconf + Volume_of_grey_matter_in_Occipital_Pole_.right.
                 + Weighted.mean_L1_in_tract_middle_cerebellar_peduncle + rfmri.100.edge.251 + rfmri.25.edge.130 
                 + Weighted.mean_OD_in_tract_middle_cerebellar_peduncle, data = sig_vars_periph2)
step.model <- stepAIC(full.model, direction = "both", trace = TRUE)
summary(step.model)

z <- lm(group2 ~ age + rfm + delta1 + delta1.deconf + Volume_of_grey_matter_in_Occipital_Pole_.right.
        + Weighted.mean_L1_in_tract_middle_cerebellar_peduncle + rfmri.100.edge.251 + rfmri.25.edge.130 
        + Weighted.mean_OD_in_tract_middle_cerebellar_peduncle, data = sig_vars_periph2, na.action = na.exclude)
plot(z)
coef(z)
confint(z)
summary(z)

library(visreg)
visreg(z, points.par = list(pch = 16, cex = 1.2, col = "red"))


z2 <- lm(group2 ~ age + rfm + delta1 + rfmri.100.edge.251 + Mean_OD_in_superior_corona_radiata_on_FA_skeleton_.left. 
              + rfmri.100.edge.851 + rfmri.100.edge.782 + rfmri.25.edge.184 + delta1.deconf + Volume_of_grey_matter_in_Occipital_Pole_.right. 
              + rfmri.25.edge.101 + rfmri.100.edge.164 + rfmri.100.edge.262 + rfmri.25.edge.180 + rfmri.100.edge.1220 
              + Mean_FA_in_cingulum_hippocampus_on_FA_skeleton_.right. + rfmri.100.edge.698 + Mean_OD_in_cingulum_hippocampus_on_FA_skeleton_.left. 
              + Mean_FA_in_superior_corona_radiata_on_FA_skeleton_.left. + rfmri.100.edge.1067 + rfmri.100.edge.33 + 
                Mean_MO_in_cingulum_hippocampus_on_FA_skeleton_.left. + Mean_OD_in_cingulum_hippocampus_on_FA_skeleton_.right., data = sig_vars_loose, na.action = na.exclude)
visreg(z2, points.par = list(pch = 16, cex = 1.2, col = "red"))
plot(z2)
coef(z2)
confint(z2)
summary(z2)

class(sig_vars_periph2$group)
levels(sig_vars_periph2$group)

library(randomForest)
model <- randomForest(y=as.factor(v.a),x=cbind(v.b,as.factor(v.c)),ntree=10)


glm.fit <- glm(group ~ age + rfm + delta1 + delta1.deconf + Volume_of_grey_matter_in_Occipital_Pole_.right.
        + Weighted.mean_L1_in_tract_middle_cerebellar_peduncle + rfmri.100.edge.251 + rfmri.25.edge.130 
        + Weighted.mean_OD_in_tract_middle_cerebellar_peduncle, data = sig_vars_periph2, na.action = na.exclude, family = binomial)
summary(glm.fit)
plot(mylogit)
visreg(mylogit, points.par = list(pch = 16, cex = 1.2, col = "red"))
vif(mylogit)
summary(sig_vars_periph2)



library(caret)
x <- sig_vars_periph2[,4:12]
y <- sig_vars_periph2[,2]
scales <- list(x=list(relation="free"), y=list(relation="free"))
featurePlot(x=x, y=y, plot="density", scales=scales)

glm.probs <- predict(glm.fit,type = "response")
glm.probs[1:5]
glm.pred <- ifelse(glm.probs > 0.5, "PG", "CG")





