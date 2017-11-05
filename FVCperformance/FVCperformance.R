#set up data
epochs       =  seq(0, 15, 1)

conv_acc     = c(0, 0.3118, 0.4468, 0.5221, 0.5727, 0.6219, 
                0.6774, 0.7312, 0.7819, 0.8216, 0.8560, 0.8819,
                0.8978, 0.9132, 0.9196, 0.9302)

conv_val_acc = c(0, 0.4221, 0.5021, 0.5383, 0.5587, 0.5748, 0.5645,
                 0.5795, 0.5957, 0.5977, 0.5857, 0.5818, 0.5918,
                 0.5949, 0.5932, 0.5960)


## Plot first set of data and draw its axis
par(bg ='transparent')
plot(epochs, conv_acc, pch = 16, axes = FALSE, ylim = c(0, 1), xlab = '', ylab = '', 
     type = 'b',col = 'black', main = 'Basic ConvNet')
lines(epochs, conv_val_acc, pch = 15,  xlab = '', type = 'b', col = 'red')
abline(h = 0.6, lty = 2)
axis(2, ylim = c(0,1), col = 'black', las = 1)  ## las=1 makes horizontal labels
axis(1, ylim = epochs)
mtext('prediction accuracy', side = 2, line = 2.5)
mtext('iteration', side = 1, line = 2.5)
box()
## Add Legend
legend('topleft', 
       legend = c('training set acc.', 'test set acc.'),
       text.col = c('black','red'),
       pch = c(16,15),
       col = c('black','red'), 
       cex = 0.9)