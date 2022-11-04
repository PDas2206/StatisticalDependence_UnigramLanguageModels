# Statistical Dependence
In statistical NLP we frequently make independence assumptions about relevant events which are not actually correct in reality. We are asking you to test the independence assumptions of unigram language models.
Pointwise mutual information,
$pmi(w1, w2)=log \frac{P(X_{t}=w1, X_{t+1}=w2)} {P(X_{t}=w1)P(X_{t+1}=w2)}$
