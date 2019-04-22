## Simple Bar Plot 

## Create the data
freq <- c(23,14,13,8,5,4,4,4,4,21)
names <- c("Prostate", "Lung", "Colorectal", "Leukemia", "Bladder", "Melanoma", "Head and Neck", "Bovel", "Pancreas", "Other")

## Assign names
names(freq) <- names

## Specify margins
par(mar = c(10,6,4,2) + 0.1)

## Plot
barplot(freq, main="Most frequent tumors in men (2012)", xlab="", ylab="Frequency (%)", names.arg=names, las=2, col=terrain.colors(10))
