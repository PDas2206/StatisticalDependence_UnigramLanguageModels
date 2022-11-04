# Statistical Dependence
In statistical NLP we frequently make independence assumptions about relevant events which are not actually correct in reality. We are asking you to test the independence assumptions of unigram language models.
Pointwise mutual information, \
$pmi(w_{1}, w_{2})=log \frac{P(X_{t}=w_{1}, X_{t+1}=w_{2})} {P(X_{t}=w_{1})P(X_{t+1}=w_{2})} $ 
$\approx log \frac{C(w_{1}w_{2})N}{C(w_{1})C(w_{2})}$ \
is a measure of statistical dependence of the events $X_{t}=w_{1}$ and $X_{t+1}=w_{2}$; $C(w)$ is the absolute frequency and *N* is the size of the corpus. If the probability of the next word in the corpus being $w_{2}$ is unaffected by the probability of the previous word being $w_{1}$, then $pmi(w_{1}, w_{2}) = 0$; otherwise the pmi is positive or negative.
We calculate the pmi for all successive pairs $(w_{1}, w_{2})$ of words in a corpus of our choice (*text2* from *nltk.book* has been used here). Words (not word pairs!) that occur in the corpus less than 10 times have been ignored. The 20 word pairs with the highest pmi value and the 20 word pairs with the lowest pmi value have been listed.
