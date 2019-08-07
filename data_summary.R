summary(OA_RA_wIDPs$X31.0.0)
summary(control_wIDPs$X31.0.0)
summary(OA_RA_wIDPs$X34.0.0)
summary(control_wIDPs$X34.0.0)

summary(OA_RA_wIDPs$Volume_of_amygdala_.right.)
summary(control_wIDPs$Volume_of_amygdala_.right.)

t.test(OA_RA_wIDPs$Volume_of_amygdala_.right., control_wIDPs$Volume_of_amygdala_.right.)
lm(OA_RA_wIDPs$Volume_of_amygdala_.right.~control_wIDPs$Volume_of_amygdala_.right.*X31.0.0)

OARA_amyg_right <- OA_RA_wIDPs$Volume_of_amygdala_.right.
control_amyg_right <- control_wIDPs$Volume_of_amygdala_.right.

boxplot(OARA_amyg_right, control_amyg_right, main = "amyg volume in groups")

sum(IDPs$Volume_of_grey_matter_.normalised_for_head_size., na.rm = TRUE)
sum(IDPs$Volume_of_putamen_.right., na.rm = TRUE)
summary(IDPs$Volume_of_grey_matter_.normalised_for_head_size.)

t.test(OA_RA_wIDPs$Volume_of_grey_matter_.normalised_for_head_size., control_wIDPs$Volume_of_grey_matter_.normalised_for_head_size.)
boxplot(OA_RA_wIDPs$Volume_of_grey_matter_.normalised_for_head_size., control_wIDPs$Volume_of_grey_matter_.normalised_for_head_size.)


t.test(OA_10col_wIDPs$Volume_of_grey_matter_.normalised_for_head_size., control_10col_wIDPs$Volume_of_grey_matter_.normalised_for_head_size.)
boxplot(OA_10col_wIDPs$Volume_of_grey_matter_.normalised_for_head_size., control_10col_wIDPs$Volume_of_grey_matter_.normalised_for_head_size.)
summary(OA_10col_wIDPs$X31.0.0)
summary(control_10col_wIDPs$X31.0.0)
summary(OA_10col_wIDPs$X34.0.0)
summary(control_10col_wIDPs$X34.0.0)

t.test(OA_10col_wIDPs$Volume_of_putamen_.right., control_10col_wIDPs$Volume_of_putamen_.right.)
boxplot(OA_10col_wIDPs$Volume_of_putamen_.right., control_10col_wIDPs$Volume_of_putamen_.right.)

t.test(OA_10col_wIDPs$Volume_of_amygdala_.right., control_10col_wIDPs$Volume_of_amygdala_.right.)
boxplot(OA_10col_wIDPs$Volume_of_amygdala_.right., control_10col_wIDPs$Volume_of_amygdala_.right.)

t.test(OA_10col_wIDPs$Volume_of_peripheral_cortical_grey_matter_.normalised_for_head_size., control_10col_wIDPs$Volume_of_peripheral_cortical_grey_matter_.normalised_for_head_size.)
boxplot(OA_10col_wIDPs$Volume_of_peripheral_cortical_grey_matter_.normalised_for_head_size., control_10col_wIDPs$Volume_of_peripheral_cortical_grey_matter_.normalised_for_head_size.)

t.test(OA_10col_wIDPs$Volume_of_grey_matter_in_Amygdala_.right., control_10col_wIDPs$Volume_of_grey_matter_in_Amygdala_.right.)
boxplot(OA_10col_wIDPs$Volume_of_grey_matter_in_Amygdala_.right., control_10col_wIDPs$Volume_of_grey_matter_in_Amygdala_.right.)

t.test(OA_10col_wIDPs$Volume_of_grey_matter_in_Putamen_.right., control_10col_wIDPs$Volume_of_grey_matter_in_Putamen_.right.)
boxplot(OA_10col_wIDPs$Volume_of_grey_matter_in_Putamen_.right., control_10col_wIDPs$Volume_of_grey_matter_in_Putamen_.right.)

t.test(OA_10col_wIDPs$Volume_of_putamen_.left., control_10col_wIDPs$Volume_of_putamen_.left.)
boxplot(OA_10col_wIDPs$Volume_of_putamen_.left., control_10col_wIDPs$Volume_of_putamen_.left.)

t.test(OA_10col_wIDPs$Volume_of_thalamus_.right., control_10col_wIDPs$Volume_of_thalamus_.right.)
boxplot(OA_10col_wIDPs$Volume_of_thalamus_.right., control_10col_wIDPs$Volume_of_thalamus_.right.)



t.test(OA_10col_wIDPs$rfmri.25.amp.1, control_10col_wIDPs$rfmri.25.amp.1)
boxplot(OA_10col_wIDPs$rfmri.25.amp.1, control_10col_wIDPs$rfmri.25.amp.1)

t.test(OA_10col_wIDPs$rfmri.25.amp.2, control_10col_wIDPs$rfmri.25.amp.2)
boxplot(OA_10col_wIDPs$rfmri.25.amp.2, control_10col_wIDPs$rfmri.25.amp.2)

t.test(OA_10col_wIDPs$rfmri.25.amp.3, control_10col_wIDPs$rfmri.25.amp.3)
boxplot(OA_10col_wIDPs$rfmri.25.amp.3, control_10col_wIDPs$rfmri.25.amp.3)

t.test(OA_10col_wIDPs$rfmri.25.amp.4, control_10col_wIDPs$rfmri.25.amp.4)
boxplot(OA_10col_wIDPs$rfmri.25.amp.4, control_10col_wIDPs$rfmri.25.amp.4)

t.test(OA_10col_wIDPs$rfmri.25.amp.5, control_10col_wIDPs$rfmri.25.amp.5)
boxplot(OA_10col_wIDPs$rfmri.25.amp.5, control_10col_wIDPs$rfmri.25.amp.5)

t.test(OA_10col_wIDPs$rfmri.25.amp.6, control_10col_wIDPs$rfmri.25.amp.6)
boxplot(OA_10col_wIDPs$rfmri.25.amp.6, control_10col_wIDPs$rfmri.25.amp.6)

t.test(OA_10col_wIDPs$rfmri.25.amp.7, control_10col_wIDPs$rfmri.25.amp.7)

t.test(OA_10col_wIDPs$rfmri.25.amp.8, control_10col_wIDPs$rfmri.25.amp.8)

t.test(OA_10col_wIDPs$rfmri.25.amp.9, control_10col_wIDPs$rfmri.25.amp.9)

t.test(OA_10col_wIDPs$rfmri.25.amp.10, control_10col_wIDPs$rfmri.25.amp.10)

t.test(OA_10col_wIDPs$rfmri.25.amp.11, control_10col_wIDPs$rfmri.25.amp.11)

t.test(OA_10col_wIDPs$rfmri.25.amp.12, control_10col_wIDPs$rfmri.25.amp.12)

t.test(OA_10col_wIDPs$rfmri.25.amp.13, control_10col_wIDPs$rfmri.25.amp.13)

t.test(OA_10col_wIDPs$rfmri.25.amp.14, control_10col_wIDPs$rfmri.25.amp.14)

t.test(OA_10col_wIDPs$rfmri.25.amp.15, control_10col_wIDPs$rfmri.25.amp.15)

t.test(OA_10col_wIDPs$rfmri.25.amp.16, control_10col_wIDPs$rfmri.25.amp.16)

t.test(OA_10col_wIDPs$rfmri.25.amp.17, control_10col_wIDPs$rfmri.25.amp.17)

t.test(OA_10col_wIDPs$rfmri.25.amp.18, control_10col_wIDPs$rfmri.25.amp.18)

t.test(OA_10col_wIDPs$rfmri.25.amp.19, control_10col_wIDPs$rfmri.25.amp.19)

t.test(OA_10col_wIDPs$rfmri.25.amp.20, control_10col_wIDPs$rfmri.25.amp.20)

t.test(OA_10col_wIDPs$rfmri.25.amp.21, control_10col_wIDPs$rfmri.25.amp.21)

t.test(OA_10col_wIDPs$Volume_of_grey_matter_.normalised_for_head_size., control_10col_wIDPs$Volume_of_grey_matter_.normalised_for_head_size.)



summary(OA_3mon$X31.0.0)
summary(control_no_pain$X31.0.0)

summary(OA_3mon$X34.0.0)
summary(control_no_pain$X34.0.0)

summary(OA_3mon$X48.0.0)
summary(control_no_pain$X48.0.0)

summary(OA_3mon$X50.0.0)
summary(control_no_pain$X50.0.0)

summary(OA_3mon$X1707.0.0)
summary(control_no_pain$X1707.0.0)

t.test(OA_3mon$delta1, control_no_pain$delta1)
boxplot(OA_3mon$delta1, control_no_pain$delta1, names = c('OA', 'CG'))
title("delta1")

t.test(OA_3mon$Volume_of_grey_matter_in_Occipital_Pole_.right., control_no_pain$Volume_of_grey_matter_in_Occipital_Pole_.right.)
boxplot(OA_3mon$Volume_of_grey_matter_in_Occipital_Pole_.right., control_no_pain$Volume_of_grey_matter_in_Occipital_Pole_.right., names = c('OA', 'CG'))
title("Volume of grey matter in Occipital Pole (right)")

t.test(OA_3mon$delta1.deconf, control_no_pain$delta1.deconf)
boxplot(OA_3mon$delta1.deconf, control_no_pain$delta1.deconf, names = c('OA', 'CG'))
title("delta1.deconf")

t.test(OA_3mon$rfmri.100.edge.251, control_no_pain$rfmri.100.edge.251)
boxplot(OA_3mon$rfmri.100.edge.251, control_no_pain$rfmri.100.edge.251, names = c('OA', 'CG'))
title("rfmri.100.edge.251")

t.test(OA_3mon$rfmri.25.edge.130, control_no_pain$rfmri.25.edge.130)
boxplot(OA_3mon$rfmri.25.edge.130, control_no_pain$rfmri.25.edge.130, names = c('OA', 'CG'))
title("rfmri.25.edge.130")

t.test(OA_3mon$rfmri.100.edge.920, control_no_pain$rfmri.100.edge.920)
boxplot(OA_3mon$rfmri.100.edge.920, control_no_pain$rfmri.100.edge.920, names = c('OA', 'CG'))
title("rfmri.100.edge.920")

mean(OA_3mon$X34.0.0)
sd(OA_3mon$X34.0.0)

mean(control_no_pain$X34.0.0)
sd(control_no_pain$X34.0.0)

mean(OA_w_age_rfm$age)
sd (OA_w_age_rfm$age)

mean(control_w_age_rfm$age)
sd (control_w_age_rfm$age)

mean(OA_w_age_rfm$rfm, na.rm = TRUE)
mean(control_w_age_rfm$rfm, na.rm = TRUE)

mean(final_periph_pain$age)
sd(final_periph_pain$age)

mean(final_periph_pain$gender)
mean(final_periph_pain$rfm, na.rm=TRUE)
sd(final_periph_pain$rfm, na.rm = TRUE)


t.test(final_periph_pain$delta1, final_control$delta1)
boxplot(final_periph_pain$delta1, final_control$delta1, names = c('PP', 'CG'))
title("delta1")

t.test(final_periph_pain$age, final_control$age)
boxplot(final_periph_pain$age, final_control$age, names = c('PP', 'CG'))
title("Age")

t.test(final_periph_pain$rfm, final_control$rfm)
boxplot(final_periph_pain$rfm, final_control$rfm, names = c('PP', 'CG'))
title("RFM")

t.test(final_periph_pain$delta1.deconf, final_control$delta1.deconf)
boxplot(final_periph_pain$delta1.deconf, final_control$delta1.deconf, names = c('PP', 'CG'))
title("delta1.deconf")

t.test(final_periph_pain$Volume_of_grey_matter_in_Occipital_Pole_.right., final_control$Volume_of_grey_matter_in_Occipital_Pole_.right.)
boxplot(final_periph_pain$Volume_of_grey_matter_in_Occipital_Pole_.right., final_control$Volume_of_grey_matter_in_Occipital_Pole_.right., names = c('PP', 'CG'))
title("Volume_of_grey_matter_in_Occipital_Pole_.right.")


t.test(final_periph_pain$Weighted.mean_OD_in_tract_middle_cerebellar_peduncle, final_control$Weighted.mean_OD_in_tract_middle_cerebellar_peduncle)
boxplot(final_periph_pain$Weighted.mean_OD_in_tract_middle_cerebellar_peduncle, final_control$Weighted.mean_OD_in_tract_middle_cerebellar_peduncle, names = c('PP', 'CG'))
title("Weighted.mean_OD_in_tract_middle_cerebellar_peduncle")

t.test(final_periph_pain$rfmri.100.edge.251, final_control$rfmri.100.edge.251)
boxplot(final_periph_pain$rfmri.100.edge.251, final_control$rfmri.100.edge.251, names = c('PP', 'CG'))
title("rfmri.100.edge.251")

t.test(final_periph_pain$rfmri.25.edge.130, final_control$rfmri.25.edge.130)
boxplot(final_periph_pain$rfmri.25.edge.130, final_control$rfmri.25.edge.130, names = c('PP', 'CG'))
title("rfmri.25.edge.130")

periph_pain_group <- read.csv('/Users/allyson.morgenthal/Desktop/Data/final groups:stats/all_periph_pain_final.csv')
loose_control_group <- read.csv('/Users/allyson.morgenthal/Desktop/Data/loose controls 2/loose_rfm_age.csv')

t.test(periph_pain_group$rfm, loose_control_group$rfm)
boxplot(periph_pain_group$rfm, loose_control_group$rfm, names = c('PG', 'LCG'))
title("RFM")

t.test(periph_pain_group$age, loose_control_group$age)
boxplot(periph_pain_group$age, loose_control_group$age, names = c('PG', 'LCG'))
title("Age")

t.test(periph_pain_group$rfm, loose_control_group$rfm)
boxplot(periph_pain_group$rfm, loose_control_group$rfm, names = c('PG', 'LCG'))
title("RFM")

t.test(periph_pain_group$delta1, loose_control_group$delta1)
boxplot(periph_pain_group$delta1, loose_control_group$delta1, names = c('Pain', 'Control'))
title("Delta1")

t.test(periph_pain_group$delta1.deconf, loose_control_group$delta1.deconf)
boxplot(periph_pain_group$delta1.deconf, loose_control_group$delta1.deconf, names = c('PG', 'LCG'))
title("delta1.deconf")

boxplot(periph_pain_group$Mean_OD_in_superior_corona_radiata_on_FA_skeleton_.left., loose_control_group$Mean_OD_in_superior_corona_radiata_on_FA_skeleton_.left., names = c('PG', 'LCG'))
title("Mean_OD_in_superior_corona_radiata_on_FA_skeleton_.left.")

t.test(periph_pain_group$Mean_FA_in_superior_corona_radiata_on_FA_skeleton_.left., loose_control_group$Mean_FA_in_superior_corona_radiata_on_FA_skeleton_.left.)
boxplot(periph_pain_group$Mean_FA_in_superior_corona_radiata_on_FA_skeleton_.left., loose_control_group$Mean_FA_in_superior_corona_radiata_on_FA_skeleton_.left., names = c('Pain', 'Control'))
title("Mean FA in superior corona radiata on FA skeleton left.")

t.test(periph_pain_group$Volume_of_grey_matter_in_Occipital_Pole_.right., loose_control_group$Volume_of_grey_matter_in_Occipital_Pole_.right.)
boxplot(periph_pain_group$Volume_of_grey_matter_in_Occipital_Pole_.right., loose_control_group$Volume_of_grey_matter_in_Occipital_Pole_.right., names = c('PG', 'LCG'))
title("Volume_of_grey_matter_in_Occipital_Pole_.right.")

t.test(periph_pain_group$Mean_FA_in_cingulum_hippocampus_on_FA_skeleton_.right., loose_control_group$Mean_FA_in_cingulum_hippocampus_on_FA_skeleton_.right.)
boxplot(periph_pain_group$Mean_FA_in_cingulum_hippocampus_on_FA_skeleton_.right., loose_control_group$Mean_FA_in_cingulum_hippocampus_on_FA_skeleton_.right., names = c('Pain', 'Control'))
title("Mean FA in cingulum hippocampus on FA skeleton right.")

t.test(periph_pain_group$Mean_OD_in_cingulum_hippocampus_on_FA_skeleton_.right., loose_control_group$Mean_OD_in_cingulum_hippocampus_on_FA_skeleton_.right.)
boxplot(periph_pain_group$Mean_OD_in_cingulum_hippocampus_on_FA_skeleton_.right., loose_control_group$Mean_OD_in_cingulum_hippocampus_on_FA_skeleton_.right., names = c('PG', 'LCG'))
title("Mean_OD_in_cingulum_hippocampus_on_FA_skeleton_.right.")

t.test(periph_pain_group$Mean_MO_in_cingulum_hippocampus_on_FA_skeleton_.left., loose_control_group$Mean_MO_in_cingulum_hippocampus_on_FA_skeleton_.left.)
boxplot(periph_pain_group$Mean_MO_in_cingulum_hippocampus_on_FA_skeleton_.left., loose_control_group$Mean_MO_in_cingulum_hippocampus_on_FA_skeleton_.left., names = c('PG', 'LCG'))
title("Mean_MO_in_cingulum_hippocampus_on_FA_skeleton_.left.")

t.test(periph_pain_group$rfmri.100.edge.251, loose_control_group$rfmri.100.edge.251)
boxplot(periph_pain_group$rfmri.100.edge.251, loose_control_group$rfmri.100.edge.251, names = c('PG', 'LCG'))
title("rfmri.100.edge.251")

t.test(periph_pain_group$rfmri.100.edge.851, loose_control_group$rfmri.100.edge.851)
boxplot(periph_pain_group$rfmri.100.edge.851, loose_control_group$rfmri.100.edge.851, names = c('PG', 'LCG'))
title("rfmri.100.edge.851")

t.test(periph_pain_group$rfmri.100.edge.782, loose_control_group$rfmri.100.edge.782)
boxplot(periph_pain_group$rfmri.100.edge.782, loose_control_group$rfmri.100.edge.782, names = c('PG', 'LCG'))
title("rfmri.100.edge.782")

t.test(periph_pain_group$rfmri.25.edge.184, loose_control_group$rfmri.25.edge.184)
boxplot(periph_pain_group$rfmri.25.edge.184, loose_control_group$rfmri.25.edge.184, names = c('PG', 'LCG'))
title("rfmri.25.edge.184")

t.test(periph_pain_group$rfmri.25.edge.101, loose_control_group$rfmri.25.edge.101)
boxplot(periph_pain_group$rfmri.25.edge.101, loose_control_group$rfmri.25.edge.101, names = c('PG', 'LCG'))
title("rfmri.25.edge.101")

t.test(periph_pain_group$rfmri.100.edge.164, loose_control_group$rfmri.100.edge.164)
boxplot(periph_pain_group$rfmri.100.edge.164, loose_control_group$rfmri.100.edge.164, names = c('PG', 'LCG'))
title("rfmri.100.edge.164")

t.test(periph_pain_group$rfmri.100.edge.262, loose_control_group$rfmri.100.edge.262)
boxplot(periph_pain_group$rfmri.100.edge.262, loose_control_group$rfmri.100.edge.262, names = c('PG', 'LCG'))
title("rfmri.100.edge.262")

t.test(periph_pain_group$rfmri.25.edge.180, loose_control_group$rfmri.25.edge.180)
boxplot(periph_pain_group$rfmri.25.edge.180, loose_control_group$rfmri.25.edge.180, names = c('PG', 'LCG'))
title("rfmri.25.edge.180")

t.test(periph_pain_group$rfmri.100.edge.1220, loose_control_group$rfmri.100.edge.1220)
boxplot(periph_pain_group$rfmri.100.edge.1220, loose_control_group$rfmri.100.edge.1220, names = c('PG', 'LCG'))
title("rfmri.100.edge.1220")

t.test(periph_pain_group$rfmri.100.edge.698, loose_control_group$rfmri.100.edge.698)
boxplot(periph_pain_group$rfmri.100.edge.698, loose_control_group$rfmri.100.edge.698, names = c('PG', 'LCG'))
title("rfmri.100.edge.698")

t.test(periph_pain_group$rfmri.100.edge.1067, loose_control_group$rfmri.100.edge.1067)
boxplot(periph_pain_group$rfmri.100.edge.1067, loose_control_group$rfmri.100.edge.1067, names = c('PG', 'LCG'))
title("rfmri.100.edge.1067")

t.test(periph_pain_group$rfmri.100.edge.33, loose_control_group$rfmri.100.edge.33)
boxplot(periph_pain_group$rfmri.100.edge.33, loose_control_group$rfmri.100.edge.33, names = c('PG', 'LCG'))
title("rfmri.100.edge.33")


mean(loose_control_group$age)
sd(loose_control_group$age)

mean(loose_control_group$rfm, na.rm = TRUE)
sd(loose_control_group$rfm, na.rm = TRUE)

meanFAhip_pain <- na.omit(periph_pain_group$Mean_FA_in_cingulum_hippocampus_on_FA_skeleton_.right.)
hist(meanFAhip_pain, main="Pain Group - Mean FA in the Cingulum Hippocampus (right)", probability=TRUE, col="gray", border="white", xlim = c(-4, 4))
d <- density(meanFAhip_pain)
lines(d, col="red")

meanFAhip_control <- na.omit(loose_control_group$Mean_FA_in_cingulum_hippocampus_on_FA_skeleton_.right.)
hist(meanFAhip_control, main="Mean FA in the Cingulum Hippocampus (right)", probability=TRUE, col="gray", border="white", xlim = c(-4,4))
d <- density(meanFAhip_control)
lines(d, col="red")

meanFAcor_pain <- na.omit(periph_pain_group$Mean_FA_in_superior_corona_radiata_on_FA_skeleton_.left.)
hist(meanFAcor_pain, main="Pain Group - Mean FA in the Corona Radiata (left)", probability=TRUE, col="gray", border="white", xlim = c(-4,4))
d <- density(meanFAcor_pain)
lines(d, col="red")

meanFAcor_control <- na.omit(loose_control_group$Mean_FA_in_superior_corona_radiata_on_FA_skeleton_.left.)
hist(meanFAcor_control, main="Mean FA in the Corona Radiata (left)", probability=TRUE, col="gray", border="white", xlim = c(-4,4))
d <- density(meanFAcor_control)
lines(d, col="red")

delta1_pain <- na.omit(periph_pain_group$delta1)
hist(delta1_pain, main="Delta1", probability=TRUE, col="gray", border="white", xlim = c(-20, 20))
d <- density(delta1_pain)
lines(d, col="red")

delta1_control <- na.omit(loose_control_group$delta1)
hist(delta1_control, main="Delta1", probability=TRUE, col="gray", border="white", xlim = c(-20, 20), ylim = c(0, 0.08), breaks = 15)
d <- density(delta1_control)
lines(d, col="red")
