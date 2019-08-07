head(combined)
combined[3:56] <- list(NULL)

model <- lm(group~., data=combined, na.action = na.omit)
summary(model)

p <- ttest_wpain_fdr$pvalue
BH_adjust <- p.adjust(p, method = "BH", n = length(p))
View(BH_adjust)

hochberg_adjust <- p.adjust(p, method = "hochberg", n = length(p))
View(hochberg_adjust)

bonferroni_adjust <- p.adjust(p, method = "bonferroni", n = length(p))
View(bonferroni_adjust)

fdr_adjust <- p.adjust(p, method = "fdr", n = length(p))
View(fdr_adjust)

fitall <- glm(group ~ delta1 + delta1.deconf + rfmri.100.edge.251 + rfmri.25.edge.130 + rfmri.100.edge.920, data = combined, na.action = na.omit,family=binomial(link='logit'))
fitall <- lm(group ~ delta1 + delta1.deconf + rfmri.100.edge.251 + rfmri.25.edge.130 + rfmri.100.edge.920, data = combined, na.action = na.omit)
fitall2 <- lm(group ~ ., data = combined, na.action = na.omit)



fitall <- glm(group ~ ., data = combined, na.action = na.omit,family=binomial(link='logit'))
fitstart <- glm(group ~ 1, data = combined, na.action = na.omit, family=binomial(link='logit'))
step(fitstart, direction = "forward", scope=formula(fitall))

by_group <- combined %>% group_by(group)
boxplot(OA_10col_wIDPs$rfmri.25.amp.3, control_10col_wIDPs$rfmri.25.amp.3)

fitall <- glm(group2 ~ ., data = sig_vars_loose, na.action = na.omit,family=binomial(link='logit'))
fitstart <- glm(group2 ~ 1, data = sig_vars_loose, na.action = na.omit, family=binomial(link='logit'))
step(fitstart, direction = "forward", scope=formula(fitall))

sig_vars_loose1 <- na.omit(sig_vars_loose)
fitall <- glm(group ~ ., data = sig_vars_loose, na.action = na.omit, family=binomial(link='logit'))
fitstart <- glm(group ~ 1, data = sig_vars_loose, na.action = na.omit, family=binomial(link='logit'))
step(fitstart, direction = "forward", scope=formula(fitall))