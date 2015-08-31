
"
A function that takes the order of matrix (n) & bias (p)
as parameters, and gives the probability of
its invertibility
Sample binary numbers to get a n by n matrix
and generate a 1000 samples of 1000 such matrixe per sample
"
prob_binary_matrix  <-  function(p  =  .5,  n  =  6) {
  start.time  <-  Sys.time()
  all.probs  <-  NULL
"for generating 1000 probabilities from 1000 
sampling exerisizes"
  for (i in 1:1000) {
"For each sample we generate 1000 binary matrixes 
  and estimate the probability of their invertibility"  
    inv.length  <-  NULL
    for (j  in  1:1000) {
#Sampling with bias 'p'      
      binary  <-  sample(c(0,  1),  n  *  n,  replace  =  TRUE
                         ,  prob  =  c(p,  1  -  p))
      mat  <-  matrix(binary,  n,  n)
      inv.length[j]  <-  ifelse(det(mat)  ==  0,  0,  1)
    }
    a  <-  length(inv.length[inv.length  ==  1])
    probability  <- a/1000
    all.probs[i]  <-  probability
  }
"
Generating confidence intervals for the probability 
of the samples, we generate LI & HI and use a t-distribution
at 95% confidence for 999 degrees of freedom
"  
  mean.probability  <-  mean(all.probs)
  sd.probability  <-  sd(all.probs)
  se.probability  <-  sd.probability/sqrt(1000)
  LI  <-  mean.probability  - qt(.975,999)  *  se.probability
  HI  <-  mean.probability  + qt(.975,999)  *  se.probability
  cat("probability of invertibility for ",  n  ," order matrix is ")
  cat(LI," and ",HI)
  end.time  <-  Sys.time()
  time.taken  <-  end.time - start.time
  cat("time taken is ",  time.taken)
}

