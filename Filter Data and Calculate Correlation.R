library(psych)

################### Body Data ####################
Adult <- subset(MergedData,AGE >=18 )
# filter kids
BodyData.Raw <- Adult[,c(1:6)]
BodyData.Raw <- BodyData.Raw[complete.cases(BodyData.Raw),]
# filter complete data
BodyData.Filtered <- BodyData.Raw
# filter BMI
BodyData.SPD <- BodyData.Filtered[,c(1,3)]
BodyData.Result <- BodyData.Filtered[,c(1,5:6)]
# get intake and measurement data
BodyData.Corr = corr.test(BodyData.Result,BodyData.SPD,
                            use = "complete", method = "pearson", adjust = "none")
BodyData.P = BodyData.Corr$p
BodyData.R = BodyData.Corr$r 

################ Plasma Data ################

PlasmaData.Raw <- Adult[,c(1:4,7,8,10,11)]
PlasmaData.Raw <- PlasmaData.Raw[complete.cases(PlasmaData.Raw),]

# >>> filter HbA1c <<<

#HbA1cFiltered <- subset(MergedData,HbA1c <= 7 )
HbA1cFiltered <- subset(PlasmaData.Raw,HbA1c <= 7 )

# >>> filter Insulin <<<
InsulinFiltered <- subset(HbA1cFiltered,IN <= 17 )
PlasmaData.filtered <-InsulinFiltered

# >> get filtered data
PlasmaData.SPD <- PlasmaData.filtered[,c(1,3)]
PlasmaData.Result <- PlasmaData.filtered[,c(1,5:8)]
PlasmaData.Corr = corr.test(PlasmaData.Result,PlasmaData.SPD,
                            use = "complete", method = "pearson", adjust = "none")
PlasmaData.P = PlasmaData.Corr$p
PlasmaData.R = PlasmaData.Corr$r  

BodyData.Out <- BodyData.Filtered[,c(1,3,5,6)]
write.csv(BodyData.Out,"NHANES2010_BodyData.csv")
PlasmaData.Out <- PlasmaData.filtered[,c(1,3,5:8)]
write.csv(PlasmaData.Out,"NHANES2010_PlasmaData.csv")

# clean
rm(InsulinFiltered)
rm(HbA1cFiltered)
rm(PlasmaData.Corr)
rm(PlasmaData.Result)
rm(PlasmaData.SPD)
rm(PlasmaData.Raw)
rm(BodyData.Raw)
rm(BodyData.Corr)
rm(BodyData.SPD)
rm(BodyData.Result)
rm(PlasmaData.filtered)
rm(BodyData.Filtered)
