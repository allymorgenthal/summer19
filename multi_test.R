for (i in names(OA_10col_wIDPs)) {
  t.test(OA_10col_wIDPs$i, control_10col_wIDPs$i)
}

lapply(names(df1)[-1],function(x)
  t.test(as.formula(paste(x,colnames(df1),sep="~")),
         data=df1))

install.packages("dplyr")
library(plyr)
cols_to_test <- colnames(df1)
results <- ldply(
  cols_to_test,
  function(colname) {
    t_val = t.test(testData[[colname]] ~ testData$Label)$statistic
    return(data.frame(colname=colname, t_value=t_val))
  })

col_names <- list()
for (i in names(OA_10col_wIDPs)) {
  col_names <- c(col_names, i)
}
install.packages("rlist")

for (name in col_names) {
  t.test(OA_10col_wIDPs$name, control_10col_wIDPs$name)
}

lapply(OA_10col_wIDPs[-1], function(x) t.test(x ~ OA_10col_wIDPs$Label))
