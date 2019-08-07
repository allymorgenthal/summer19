library(qqman)
gwas1_results <- read.table(file = '/Users/allyson.morgenthal/Desktop/gwas_1.SAIGE_GLMM_ADD.UKB_Freeze_Five_EUR.chronic_pain.lmm.tsv', sep = '\t', header = TRUE)
str(gwas1_results)
head(gwas1_results)

gwas1_results <- read.table(file = '/Users/allyson.morgenthal/Desktop/gwas_1.SAIGE_GLMM_ADD.UKB_Freeze_Five_EUR.chronic_pain.lmm.tsv', sep = '\t', header = TRUE)
gwas2_results <- read.table(file = '/Users/allyson.morgenthal/Desktop/gwas_2.SAIGE_GLMM_ADD.UKB_Freeze_Five_EUR.chronic_pain.lmm.tsv', sep = '\t', header = TRUE)
gwas3_results <- read.table(file = '/Users/allyson.morgenthal/Desktop/gwas_3.SAIGE_GLMM_ADD.UKB_Freeze_Five_EUR.chronic_pain.lmm.tsv', sep = '\t', header = TRUE)
gwas4_results <- read.table(file = '/Users/allyson.morgenthal/Desktop/gwas_4.SAIGE_GLMM_ADD.UKB_Freeze_Five_EUR.chronic_pain.lmm.tsv', sep = '\t', header = TRUE)
gwas5_results <- read.table(file = '/Users/allyson.morgenthal/Desktop/gwas_5.SAIGE_GLMM_ADD.UKB_Freeze_Five_EUR.chronic_pain.lmm.tsv', sep = '\t', header = TRUE)

manhattan(gwas1_results, main = "Manhattan Plot for GWAS1", snp = "Name", chr = "Chr", p = "Pval", bp = "Pos")
manhattan(gwas2_results, main = "Manhattan Plot for GWAS2", snp = "Name", chr = "Chr", p = "Pval", bp = "Pos")
manhattan(gwas3_results, main = "Manhattan Plot for GWAS3", snp = "Name", chr = "Chr", p = "Pval", bp = "Pos")
manhattan(gwas4_results, main = "Manhattan Plot for GWAS4", snp = "Name", chr = "Chr", p = "Pval", bp = "Pos")
manhattan(gwas5_results, main = "Manhattan Plot for GWAS5", snp = "Name", chr = "Chr", p = "Pval", bp = "Pos")

qq(gwas1_results$Pval, main = "GWAS1 QQ Plot")
qq(gwas2_results$Pval, main = "GWAS2 QQ Plot")
qq(gwas3_results$Pval, main = "GWAS3 QQ Plot")
qq(gwas4_results$Pval, main = "GWAS4 QQ Plot")
qq(gwas5_results$Pval, main = "GWAS5 QQ Plot")

gwas4_results2 <- subset(gwas4_results, Pval >= 1e-200)
manhattan(gwas4_results2, main = "Manhattan Plot for GWAS4 Subset", snp = "Name", chr = "Chr", p = "Pval", bp = "Pos")

#args <- commandArgs(trailingOnly = TRUE)
data <- read.table("gwas1_results", header=TRUE)
medianP <- median(gwas1_results$Pval[gwas1_results$AAF>=0.01], na.rm = TRUE)
medianX2 <- qchisq(medianP, df=1, lower.tail=F)
val=(medianX2 / 0.455)
gwas1_lambda <- print(paste(val,"blah",sep=" "),quote=FALSE)

args <- commandArgs(trailingOnly = TRUE)
medianP <- median(gwas2_results$Pval, na.rm = TRUE)
medianX2 <- qchisq(medianP, df=1, lower.tail=F)
val=(medianX2 / 0.455)
gwas2_lambda <- print(paste(val,args[1],sep=" "),quote=FALSE)

args <- commandArgs(trailingOnly = TRUE)
medianP <- median(gwas3_results$Pval, na.rm = TRUE)
medianX2 <- qchisq(medianP, df=1, lower.tail=F)
val=(medianX2 / 0.455)
gwas3_lambda <- print(paste(val,args[1],sep=" "),quote=FALSE)

args <- commandArgs(trailingOnly = TRUE)
medianP <- median(gwas4_results$Pval, na.rm = TRUE)
medianX2 <- qchisq(medianP, df=1, lower.tail=F)
val=(medianX2 / 0.455)
gwas4_lambda <- print(paste(val,args[1],sep=" "),quote=FALSE)

args <- commandArgs(trailingOnly = TRUE)
medianP <- median(gwas4_results2$Pval, na.rm = TRUE)
medianX2 <- qchisq(medianP, df=1, lower.tail=F)
val=(medianX2 / 0.455)
gwas4_lambda2 <- print(paste(val,args[1],sep=" "),quote=FALSE)

args <- commandArgs(trailingOnly = TRUE)
medianP <- median(gwas5_results$Pval, na.rm = TRUE)
medianX2 <- qchisq(medianP, df=1, lower.tail=F)
val=(medianX2 / 0.455)
gwas5_lambda <- print(paste(val,args[1],sep=" "),quote=FALSE)

gwas1_results2 <- read.csv('/Users/allyson.morgenthal/Desktop/gwas1_imputed_collated.csv')
data <- read.table("gwas1_results2", header=TRUE)
medianP <- median(gwas1_results2$Pval[gwas1_results2$AAF>=0.01], na.rm = TRUE)
medianX2 <- qchisq(medianP, df=1, lower.tail=F)
val=(medianX2 / 0.455)
gwas1_lambda2 <- print(paste(val,"blah",sep=" "),quote=FALSE)
manhattan(gwas1_results2, main = "Manhattan Plot2 for GWAS1", snp = "Name", chr = "Chr", p = "Pval", bp = "Pos")

gwas2_results2 <- read.csv('/Users/allyson.morgenthal/Desktop/gwas2_imputed_collated.csv')
manhattan(gwas2_results2, main = "Manhattan Plot2 for GWAS2", snp = "Name", chr = "Chr", p = "Pval", bp = "Pos")

gwas5_results2 <- read.csv('/Users/allyson.morgenthal/Desktop/gwas5_imputed_collated.csv')
manhattan(gwas5_results2, main = "Manhattan Plot2 for GWAS5", snp = "Name", chr = "Chr", p = "Pval", bp = "Pos")

library(manhattanly)
gwas2_genes_try <- read.csv('/Users/allyson.morgenthal/Desktop/gwas2_genes_try.csv')
gwas2_genes <- read.csv('/Users/allyson.morgenthal/Desktop/gwas2_genes_wp.csv')
manhattanly(DT)
DT <- manhattanr(gwas2_genes, snp = "Name", gene = "Gene", chr = "Chr", bp = "Pos", p = "Pval")

gwas1_genes <- read.csv('/Users/allyson.morgenthal/Desktop/gwas1_genes_wp.csv')
manhattanly(DT2)
DT2 <- manhattanr(gwas1_genes, snp = "Name", gene = "Gene", chr = "Chr", bp = "Pos", p = "Pval")

gwas5_genes <- read.csv('/Users/allyson.morgenthal/Desktop/gwas5_genes_try2.csv')
DT5 <- manhattanr(gwas5_genes, snp = "Name", gene = "Gene", bp = "Pos", p = "Pval", chr = "Chr")
manhattanly(DT5)

gwas3_genes <- read.csv('/Users/allyson.morgenthal/Desktop/gwas5_genes_try.csv')
DT3 <- manhattanr(gwas5_genes, snp = "Name", gene = "Gene", bp = "Pos", p = "Pval", chr = "Chr")
manhattanly(DT3)

library(xlsx)
write.csv(gwas1_genes, file = "gwas1_genes_exact.csv")
write.csv(gwas2_genes, file = "gwas2_genes_exact.csv")
write.csv(gwas3_genes, file = "gwas3_genes_exact.csv")
write.csv(gwas5_genes, file = "gwas5_genes_exact.csv")

gwas1_genes_25K <- read.csv('/Users/allyson.morgenthal/Desktop/gwas1_genes_try.csv')
DT1_25K <- manhattanr(gwas1_genes_25K, snp = "Name", gene = "Gene", chr = "Chr", bp = "Pos", p = "Pval")
manhattanly(DT1_25K, title = "GWAS1 Manhattan")

gwas2_genes_25K <- read.csv('/Users/allyson.morgenthal/Desktop/gwas2_genes_try.csv')
DT2_25K <- manhattanr(gwas2_genes_25K, snp = "Name", gene = "Gene", chr = "Chr", bp = "Pos", p = "Pval")
manhattanly(DT2_25K)

gwas3_genes_25K <- read.csv('/Users/allyson.morgenthal/Desktop/gwas3_genes_try.csv')
DT3_25K <- manhattanr(gwas3_genes_25K, snp = "Name", gene = "Gene", chr = "Chr", bp = "Pos", p = "Pval")
manhattanly(DT3_25K)

gwas5_genes_25K <- read.csv('/Users/allyson.morgenthal/Desktop/gwas5_genes_try.csv')
DT5_25K <- manhattanr(gwas5_genes_25K, snp = "Name", gene = "Gene", chr = "Chr", bp = "Pos", p = "Pval")
manhattanly(DT5_25K, title = "GWAS5 Manhattan")

gwas4_genes <- read.csv('/Users/allyson.morgenthal/Desktop/gwas4_genes.csv')
DT4 <- manhattanr(gwas4_genes, snp = "Name", gene = "Gene", chr = "Chr", bp = "Pos", p = "Pval")
manhattanly(DT4, title = "GWAS4 Manhattan")

gwas4_genes_ex <- read.csv('/Users/allyson.morgenthal/Desktop/gwas4_genes_expand.csv')
DT4_25K <- manhattanr(gwas4_genes_ex, snp = "Name", gene = "Gene", chr = "Chr", bp = "Pos", p = "Pval")
manhattanly(DT4_25K, title = "GWAS4 Manhattan Expanded")
manhattan(gwas4_genes_ex, main = "Manhattan Plot for GWAS4 Expanded", snp = "Name", chr = "Chr", p = "Pval", bp = "Pos", annotatePval = 0.0001)

hist(, xlim=c(0, 3500), breaks=seq(0, 3500, 100), main=colnames[i], probability=TRUE, col="gray", border="white")
d <- density(crime[,i])
lines(d, col="red")







