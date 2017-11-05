#install required packages if necessary
pkg = c('corrplot')
lapply(pkg, require, character.only = TRUE)
lapply(pkg, library, character.only = TRUE)

#path where dataset is 
dir_data = '...'

#load data
avg_emo = read.csv2(dir_data) 

#rename return variable in dataset
names(avg_emo)[11] = "return"

#generate and round correlation matrix, choose relevant columns
cormat = round(cor(avg_emo[,c(2:9,11)]), digits = 2)

#generate plot with fct. from 'corrplot'-package
corrplot(cormat, method = "circle", type = 'upper', tl.col = "black", order = "hclust")


