[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **FVCEurostoxxPLS** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: FVCEurostoxxPLS

Published in: Face Value of Companies

Description: 'Estimates a partial least squares (PLS) model. Independent variables are averaged emotion scores (anger, disgust, fear, contempt, happiness, neutrality, sadness, surprise) for all webcasts of press conferences held by the European central bank between Jan. 2011 and Sep. 2017. The dependent variable is daily return data of Eurostoxx50.'

Keywords: financial, projection, principal-components, R-squared, correlation, multi-dimensional, returns

Author: Sophie Burgard

Submitted:  05.11.2017

Datafile: 'ECB_avg_emo.csv'


```

### R Code
```r

#install required packages if necessary
pkg = c('plsdepot')
lapply(pkg, require, character.only = TRUE)
lapply(pkg, library, character.only = TRUE)

#path where dataset is 
dir_data = '...'

#load data
avg_emo = read.csv2(dir_data) 

#sort data, that y-variable is in last position 
emodata = avg_emo[,c(2:9,11)]

#estimate model
pls_fit = plsreg1(emodata[,1:8], emodata[,9], comps = 4, crosval = TRUE)

#loads for each variable in components
pls_fit$x.loads

#R2-fit of model
pls_fit$R2




```

automatically created on 2018-05-28