# sqlalchemy-challenge
Climate analysis leveraging sqlalchemy skills

This challenge has multiple parts:

### Precipitation Analysis

### Station Analysis

### Build an API climate APP with multiple routes

### Bonus Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

*I used pandas to evaluate the data, compute an average per station for June and December, and then compared these data sets in a paired t test.

The paired t test across 9 stations in June vs Dec shows that the p-value is < .05 so we reject the null hypothesis.

The null hypothesis was that the mean of the temps in June is equal to the mean of the temps in December.  Since we have a pvalue less than what we tested for (.05), we reject the null hypothesis 
and state that the mean temp in June IS significantly different than the mean temperature in December.

###Bonus Temperature Analysis II
