# Statistical Dependence
In statistical NLP we frequently make independence assumptions about relevant events which are not actually correct in reality. We are asking you to test the independence assumptions of unigram language models.
Pointwise mutual information, \
$pmi(w_{1}, w_{2})=log \frac{P(X_{t}=w_{1}, X_{t+1}=w_{2})} {P(X_{t}=w_{1})P(X_{t+1}=w_{2})} \approx log \frac{C(w_{1}w_{2}).N}{C(w_{1}). C(w_{2})} $ \
is a measure of statistical dependence of the events $X_{t}=w_{1}$ and $X_{t+1}=w_{2}$
