install.packages("glmnet")

library(tidyverse)
library(caret)
library(glmnet)

sig_vars_periph <- na.omit(sig_vars_periph)

sample_n(sig_vars_periph, 3)

set.seed(123)
training.sample <- sig_vars_periph$group %>%
  createDataPartition(p=0.8, list=FALSE)
train.data <-sig_vars_periph[training.sample, ]
test.data <- sig_vars_periph[-training.sample, ]

x <- model.matrix(train.data$group~., train.data)[,-1]
y <- ifelse(train.data$group == "PG", 1, 0)

glmnet(x, y, family = "binomial", alpha = 1, lambda = NULL)


library(glmnet)
set.seed(123)
cv.lasso <- cv.glmnet(x, y, alpha = 1, family = "binomial")
model <- glmnet(x, y, alpha = 1, family = "binomial", lambda = cv.lasso$lasso.min)
coef(model)

x.test <- model.matrix(group ~., test.data)[,-1]
probabilities <- model %>% predict(newx = x.test)
predicted.classes <- ifelse(probabilities > 0.5, "pos", "neg")

observed.classes <-test.data$group
mean(predicted.classes == observed.classes)





