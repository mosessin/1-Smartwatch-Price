# Project Title

Smartwatch E-Commerce Price Prediction using Linear Regression, Ridge Regression, and LASSO

## Abstract

The development of *smartwatches* as of lately has experienced rapid growth along with the growth of the e-commerce market that offers a wide variety of products with a wide price range. *Smartwatch* pricing is an important issue because it is influenced by many factors, which makes accurate price prediction a challenge in e-commerce data analysis. This study aims to build and compare regression-based *smartwatch* price prediction models to understand the influence of product features and the effectiveness of each method. This study uses three regression models: Linear Regression as the baseline model, as well as Ridge Regression and LASSO as models with regularization. The results show that Linear Regression is able to achieve good performance with an RMSE value of 3780.710 and an R² score of 95.958%. Ridge Regression and LASSO show improved performance, with Ridge Regression achieved an RMSE of 3699.951 and R² score of 96.129%, as well as LASSO which achieved an RMSE of 3167.308 and an R² score of 97.163%. Variations in the regularization parameter value α were shown to affect the performance of both models, with the optimal parameter value α balancing model bias and variance. Overall, the results show that applying regression with regularization is effective in improving the accuracy of *smartwatch* price prediction on e-commerce platforms.

***Key words***: Price prediction, *smartwatch*, Linear Regression, Ridge Regression, LASSO


## Required Libraries

[Pandas](https://pandas.pydata.org/) (https://pandas.pydata.org/).

[Scikit-Learn](http://scikit-learn.org/) (http://scikit-learn.org/).

For plotting purposes, this project also uses [NumPy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/).


## Notes

1. The `main.py` file contains the main Python code for the project. 
2. In the `main.py` file, you can modify the model parameters in line 23 (for Ridge Regression) and line 24 (for LASSO).
3. In the `main.py` file, you can replicate and choose the model to run in line 25 (`LRg` for Linear Regression, `Rdg` for Ridge Regression, and `Las` for LASSO).
4. The `plotter_1.py` file contains the Python code for plotting training vs testing data, and `plotter_2.py` contains the Python code for plotting model parameters vs R² score.
5. Just like in the main code, you can change the model parameters and choose the model to run.


## Few words

This project is documented in [my personal website page](https://mosessinanta.github.io/projects/001.html). My work is free to use as a reference for any project, but please do cite them in your works.

Thank you for visiting my project. Good luck and have fun!


## License


[MIT License](https://choosealicense.com/licenses/mit/)
