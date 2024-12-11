# Outage Severity and People Affected

By Quy-Dzu Do

# Introduction

For this project, I will be working with the dataset titled "Data on major power outage events in the continental U.S." provides comprehensive information on significant power outages across the United States from 2000 to 2016. It encompasses various aspects, including general outage details, regional climate data, specifics of each outage event, electricity consumption patterns, economic characteristics, and land-use information.

**Key Components of the Dataset:**

- **General Information:** Details about each outage event, such as location, date, and duration.

- **Regional Climate Information:** Climate data pertinent to the regions affected by outages.

- **Outage Events Information:** Specifics on the causes and impacts of each outage.

- **Regional Electricity Consumption Information:** Data on electricity usage in the affected areas.

- **Regional Economic Characteristics:** Economic data related to the regions experiencing outages.

- **Regional Land-Use Characteristics:** Information on land use in the areas affected by outages.

This dataset serves as a valuable resource for analyzing the patterns and causes of major power outages in the U.S., aiding in the development of strategies to mitigate future occurrences.

The raw Data is hosted by Purdue University here: [https://engineering.purdue.edu/LASCI/research-data/outages](https://engineering.purdue.edu/LASCI/research-data/outages).
The full report with desciptions of the data can be found here: [https://www.sciencedirect.com/science/article/pii/S2352340918307182](https://www.sciencedirect.com/science/article/pii/S2352340918307182)

Here is a brief description of the relevant columns to my project:

|Column                |Description|
|---                |---        |
|`'YEAR'`                |Indicates the year when the outage event occurred|
|`'MONTH'`                |Indicates the month when the outage event occurred|
|`'U.S._STATE'`                |Represents all the states in the continental U.S.|
|`'NERC.REGION'`                |North American Electric Reliability Corporation (NERC) regions involved in the outage event|
|`'CLIMATE.REGION'`                |U.S. Climate regions as specified by National Centers for Environmental Information (9 Regions)|
|`'ANOMALY.LEVEL'`                |Oceanic El Niño/La Niña (ONI) index referring to the cold and warm episodes by season|
|`'CLIMATE.CATEGORY'`           |This represents the climate episodes corresponding to the years|
|`'OUTAGE.START.DATE'`                |Day of the year when the outage event started|
|`'OUTAGE.START.TIME'`                |Time of the day when the outage event started|
|`'OUTAGE.RESTORATION.DATE'`                |Day of the year when power was restored to all the customers|
|`'OUTAGE.RESTORATION.TIME'`                |Time of the day when power was restored to all the customers|
|`'CAUSE.CATEGORY'`                |Categories of all the events causing the major power outages|
|`'OUTAGE.DURATION'`                |Duration of outage events (in minutes)|
|`'DEMAND.LOSS.MW'`                |Amount of peak demand lost during an outage event (in Megawatt) [but in many cases, total demand is reported]|
|`'CUSTOMERS.AFFECTED'`                |Number of customers affected by the power outage event|
|`'TOTAL.PRICE'`                |Average monthly electricity price in the U.S. state (cents/kilowatt-hour)|
|`'TOTAL.SALES'`                |Total electricity consumption in the U.S. state (megawatt-hour)|
|`'TOTAL.CUSTOMERS'`                |Annual number of total customers served in the U.S. state|
| `'RES.PERCEN'`                |Percentage of residential electricity consumption compared to the total electricity consumption in the state (in %)|
|`'COM.PERCEN'`	                    |Percentage of commercial electricity consumption compared to the total electricity consumption in the state (in %)|
|`'IND.PERCEN'`	                    |Percentage of industrial electricity consumption compared to the total electricity consumption in the state (in %)|
|`'POPULATION'`                     |Population in the U.S. state in a year|
|`'RES.CUSTOMERS'`       |Annual number of customers served in the residential electricity sector of the U.S. state|
|`'COM.CUSTOMERS'`       |Annual number of customers served in the commercial electricity sector of the U.S. state|
|`'IND.CUSTOMERS'`       |Annual number of customers served in the industrial electricity sector of the U.S. state|

# Data Cleaning and Exploratory Data Analysis

To work with the data, we will clean the data changing certain variables to easier data types to do statistical analysis on.

## Cleaning

We shall begin by pulling the data into a Pandas Dataframe skipping the first 5 rows and the seventh row as they do not contain data and we set the ```"OBV"``` Column to the index as it IDs the rows of data. We will also convert the ```"OUTAGE.START.TIME"``` and ```"OUTAGE.RESTORATION.TIME"``` to timedelta objects, and ```"OUTAGE.START.DATE"``` and ```"OUTAGE.RESTORATION.DATE"``` to timestamp objects so they can be combined into a single date-time value stores as a Pandas Timestamp in a new dataframe with ```"OUTAGE.START.DATE"``` and ```"OUTAGE.RESTORATION.DATE"``` containing the new objects and the Time columns dropped.

The first few rows of this cleaned DataFrame are shown below, with a portion of columns selected.

|   YEAR |   MONTH | U.S._STATE   |NERC.REGION   | CLIMATE.REGION     |   ANOMALY.LEVEL | CLIMATE.CATEGORY   | OUTAGE.START.DATE   | OUTAGE.RESTORATION.DATE   | CAUSE.CATEGORY     |   OUTAGE.DURATION |   CUSTOMERS.AFFECTED | TOTAL.SALES |   RES.PERCEN |   COM.PERCEN |   IND.PERCEN |   RES.CUSTOMERS |   COM.CUSTOMERS |   IND.CUSTOMERS |   TOTAL.CUSTOMERS | POPULATION |
|-------:|--------:|:-------------|--------------|:-------------------|----------------:|:-------------------|:--------------------|:--------------------------|:------------------:|------------------:|---------------------:|------------:|-------------:|-------------:|-------------:|----------------:|----------------:|----------------:|------------------:|-----------:|
|   2011 |       7 | Minnesota    |MRO           | East North Central |            -0.3 | normal             | 2011-07-01 17:00:00 | 2011-07-03 20:00:00       | severe weather     |              3060 |                70000 | 6.56252e+06 |      35.5491 |      32.225  |      32.2024 |         2308736 |          276286 |           10673 |           2595696 |    5348119 |
|   2014 |       5 | Minnesota    |MRO           | East North Central |            -0.1 | normal             | 2014-05-11 18:38:00 | 2014-05-11 18:39:00       | intentional attack |                 1 |                  nan | 5.28423e+06 |      30.0325 |      34.2104 |      35.7276 |         2345860 |          284978 |            9898 |           2640737 |    5457125 |
|   2010 |      10 | Minnesota    |MRO           | East North Central |            -1.5 | cold               | 2010-10-26 20:00:00 | 2010-10-28 22:00:00       | severe weather     |              3000 |                70000 | 5.22212e+06 |      28.0977 |      34.501  |      37.366  |         2300291 |          276463 |           10150 |           2586905 |    5310903 |
|   2012 |       6 | Minnesota    |MRO           | East North Central |            -0.1 | normal             | 2012-06-19 04:30:00 | 2012-06-20 23:00:00       | severe weather     |              2550 |                68200 | 5.78706e+06 |      31.9941 |      33.5433 |      34.4393 |         2317336 |          278466 |           11010 |           2606813 |    5380443 |
|   2015 |       7 | Minnesota    |MRO           | East North Central |             1.2 | warm               | 2015-07-18 02:00:00 | 2015-07-19 07:00:00       | severe weather     |              1740 |               250000 | 5.97034e+06 |      33.9826 |      36.2059 |      29.7795 |         2374674 |          289044 |            9812 |           2673531 |    5489594 |

This changed helped to agregate some of the data so allow for analysis of the date and time and looking at times, I was able to easily see which outages lasted for several days and thus see if that had any impact in the rest of the data such as if rural areas had more Duration compared to other areas. Statistically, it was easier to look at the Outage Duration category by in terms of human reading, the start and end dates haveing both date and time together was easier to look at as a human.

## Exploratory Data Analysis

### Univariate Analysis

In my initial look at the data, I decided to look at the distributions of the Outage Duration of the entire data set and the Outage Duration of California State to see if there seemed to  be a significant difference
<iframe
  src="Website_Resources/uni_1_1.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>
Now I plotted the distribution of California data points.
<iframe
  src="Website_Resources/uni_1_2.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>
After, I wanted to look at the trends of Outage Duration means over the Years and see if there was a posistive or negative trend in the data.
<iframe
  src="Website_Resources/uni_2_1.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

### Bivariate Analysis

To analyze the relation ship between variables in the data set, I did some Bivariate Analysis looking at the effects some variables had on the `'Customers Affected'` Variables.  The First scatter plot I made was of `'Customers Affected'` as a result of `'Outage Duration'`.

<iframe
  src="Website_Resources/bi_1.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

I did a similar plot between `'Customer Affected'` vs `'Number of Customers'`.

<iframe
  src="Website_Resources/bi_2.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

Surprisingly enough, there seems to be very little correlation between the variables given the intuition that the number of customers would correlate in a similar rise in customers affected in a given power outage and also as time increases, the number of people likely to be affected increases as they either need to use teh electricity at a certain time or have a higher chance to use an electronic device.

### Grouping and Aggregates

For this pivot table, I was interested in looking at the output variables, the variables relating to the severity of the outages, and their changes across the States. For this, I used a simple average of all the values in a given state's variables and stored it as a value in a cell on the pivot table. Here we can see that the average customers affected and Demand Lost increases in Urban States while Outage Duration is higher in those Rural States.

| U.S._STATE           |   CUSTOMERS.AFFECTED |   DEMAND.LOSS.MW |   OUTAGE.DURATION |
|:---------------------|---------------------:|-----------------:|------------------:|
| Alabama              |             94328.8  |        291.5     |         1152.8    |
| Alaska               |             14273    |         35       |          nan      |
| Arizona              |             64402.7  |       1245.7     |         4552.92   |
| Arkansas             |             47673.8  |        149.9     |         1514.36   |
| California           |            201366    |        667.595   |         1666.34   |
| Colorado             |             41060.6  |        154.636   |          901.071  |
| Connecticut          |             60339.2  |         36.4286  |         1278.83   |
| Delaware             |              3475    |          4.13043 |          144.925  |
| District of Columbia |            194709    |       1280       |         4303.6    |
| Florida              |            289369    |        804.575   |         4094.67   |
| Georgia              |            120680    |        494.75    |         1345.41   |
| Hawaii               |            147237    |        536       |          845.4    |
| Idaho                |              5833.33 |        116.5     |          414.625  |
| Illinois             |            207027    |        214.222   |         1602.45   |
| Indiana              |             69551.4  |        301.524   |         3521.64   |
| Iowa                 |             94000    |        337.5     |         4793.75   |
| Kansas               |            108000    |        250       |         4376.29   |
| Kentucky             |            130531    |        207       |         5093.92   |
| Louisiana            |            151003    |        224.471   |         4084.55   |
| Maine                |             54839.4  |         38.125   |         1097.06   |
| Maryland             |            120535    |        357.5     |         2313.09   |
| Massachusetts        |             77983.4  |       2392.2     |          944.167  |
| Michigan             |            152878    |        696.549   |         5302.98   |
| Minnesota            |            124007    |         69       |         2727.93   |
| Mississippi          |              5000    |         15       |           84      |
| Missouri             |             50611.1  |        156.455   |         3374.07   |
| Montana              |               nan    |        nan       |           54      |
| Nebraska             |             87070.7  |        385.75    |         2455.75   |
| Nevada               |             22220    |         14       |          553.286  |
| New Hampshire        |             13869.8  |          0       |          279.643  |
| New Jersey           |            160217    |        140.056   |         4450.91   |
| New Mexico           |            166667    |        346.667   |          140.375  |
| New York             |            190676    |       1283.15    |         6034.96   |
| North Carolina       |             99624.8  |        914.37    |         1457.28   |
| North Dakota         |             34500    |        902.5     |          720      |
| Ohio                 |            136783    |       1057.32    |         2867.86   |
| Oklahoma             |            160683    |        178.5     |         3019.09   |
| Oregon               |             43958.6  |         67.1111  |          766.68   |
| Pennsylvania         |            168537    |        225.263   |         3811.7    |
| South Carolina       |            251913    |       1699.71    |         3135      |
| South Dakota         |               nan    |        228.5     |          120      |
| Tennessee            |             59317.4  |        356.154   |         1041.97   |
| Texas                |            223232    |        552.083   |         2704.82   |
| Utah                 |             10227.7  |        186.048   |          250.22   |
| Vermont              |                 0    |          0       |           35.4444 |
| Virginia             |            149429    |        521.3     |         1051.19   |
| Washington           |            101944    |        214.195   |         1508.15   |
| West Virginia        |            179794    |        362       |         6979      |
| Wisconsin            |             45876    |        161       |         7904.11   |
| Wyoming              |             11833.3  |         26.75    |           33.3333 |

# Assessment of Missingness

## NMAR Analysis

A column I would suspect is NMAR could be the `DEMAND.LOSS.MV` Column. I would say this because the Demand would most likely only be calcuated if there was historical data from a given area affected that would allow the utilities to estimate Demand lost. Furthermore, the data also noted that total demand would be submitted most of the time so the missingness is based on whether the companies would give the correct data which is not shown in the data set. Thus, we could not tell if the data is completely missing at random or if it is dependent on somehting else as the report clearly states that the missingness is based on the correct data being recieved or not.

Furthermore, We do not not if there were other reasons why the data may not be there. We could look into finding whether the company reporting the data has data about the peak usages of tehor comunities and use that information to determine causes of teh missing data thus making it MAR.

## Missingness Dependency
To test missingness dependency, I will focus on the Missingness of `OUTAGE.DURATION`. I will test this against the columns `NERC.REGION` and `MONTH`.

### Nerc Region

We will begin by seeing the Missingness of `OUTAGE.DURATION` in relation to `NERC.REGION`.

**Null Hypothesis:** The distribution of `NERC.REGION` is the same whether `OUTAGE.DURATION` is missing or not missing.

**Alternate Hypothesis:** The distribution of `NERC.REGION` is different whether `OUTAGE.DURATION` is missing or not missing.

For this test, I got a TVD of 0.315 which resulted in a p-value of 0. From this test, We were able to say that the Missingness of the `OUTAGE.DURATION` column is dependent on the `NERC.REGION` column. This shows that there is evidence that certain region are likely to be missing data on their outage duration more than others and that a given missing value may be more likely to be from one or many regions but not others.

<iframe
  src="Website_Resources/missing_MAR.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

### Month

For this test, I will see if the missingness of `OUTAGE.DURATION` is dependent on the `MONTH` Column

**Null Hypothesis:** The distribution of `MONTH` is the same whether `OUTAGE.DURATION` is missing or not missing.

**Alternate Hypothesis:** The distribution of `MONTH` is different whether `OUTAGE.DURATION` is missing or not missing.

For this test, I got a TVD of 0.315 which resulted in a p-value of 0. From this test, We were able to say that the Missingness of the `OUTAGE.DURATION` column is dependent on the `NERC.REGION` column. This test provides that there is no evidence that the `OUTAGE.DURATION` missingness is dependent on the `MONTHS` column which means that we fail to reject the null hypothesis so we conclude that the The distribution of `MONTH` is the same whether `OUTAGE.DURATION` is missing or not missing.

<iframe
  src="Website_Resources/missing_MCAR.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

# Hypothesis Testing
I will be testing whether the outage duration is greater on average for severe weather outages over intentional attack outages. The relevant columns for this test are `OUTAGE.DURATION` and `CAUSE.CATEGORY`. I will only be using the outages where `CAUSE.CATEGORY` is equal to 'severe weather' or 'intentional attack'.

**Null Hypothesis:** On average, the duration of severe weather outages is the same as the duration of intentional attack outages.

**Alternate Hypothesis:** On average, the duration of severe weather outages is greater than the duration of intentional attack outages.

**Test Statistic:** Difference in means. Specifically, mean outage duration of severe weather - mean outage duration of intentional attacks.

I performed a permutation test with 10,000 simulations in order to generate an empirical distribution of the test statisic under the null hypothesis.

The p-value I got was 0.0, so with a standard significance level of 0.05, we reject the null hypothesis because the results are statistically significant. We conclude that on average, the duration of severe weather outages is greater than intentional attack outages.

The plot below shows the observed difference against the empirical distribution of differences from the permutation tests.
<iframe
  src="assets/h_test.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

# Framing a Prediction Problem

While Outage Duration is a good classifier for how extreme an outage is, most companies would be more interested in the effects it has on customers and how whether they are more likely to complain. Thus, we will be using the given data and predicting how many customers are affected. This will help the companies to identify events that are more likely to affect more people. From there, the companies may seek to create new methods to counter act on these specific predictive variables.

Looking at inital models, I saw that much of the data seems very much skewed by extremely low values that happen very often and a few outlier high values. This has resulted in very high RMSE values and overall a bad predictor for what is creates a high amount of affected customers. To remedy this, I will do a classification model and define a new variable "High_Risk_Customers" as a Binary classification of whether a certain event will have more than a certain number of affected customers thus the model will focus on identifying these communities and risk factors rather than trying to accurately predicting the values.

# Baseline Model
My model is a binary classifier using the features NERC Region, Anomaly level, Year, and Urban factor to predict whether a major outage is caused by severe weather or an intentional attack. This information would provide companies with how to approach energy infrastructure problems and decide whether to devote resources to better security against attacks or better protection from severe weather.

The features are: `NERC.REGION` (nominal), `ANOMALY.LEVEL` (quantitative), `YEAR` (ordinal), and `URBAN` (quantitative).
I chose these because `NERC.REGION` indicates the energy infrastructure and regulation of a region, `ANOMALY.LEVEL` provides climate conditions that might create more severe weather, `YEAR` to account for changes over time, and `URBAN` since areas with a higher urban factor have more densely populated areas which could have more strains on enery and are impacted more by major power outages.

The predicted columns was converted to 1 for severe weather and 0 for intentional attack.

The performance of this model was pretty good, with an r-squared of 0.764 on the test set.
The F1 score was 0.831.


# Final Model
My final model incorporated these features: `NERC.REGION`, `CLIMATE.REGION`, `ANOMALY.LEVEL`, `YEAR`, `MONTH`, `TOTAL.PRICE`, `TOTAL.SALES`, `TOTAL.CUSTOMERS`, `URBAN`. I used a DecisionTreeClassifier and was able to achieve an R-squared of 0.88 when testing on the test set.

I added `CLIMATE.REGION` (nominal) becaause certain climate regions are more prone to be hit by severe weather. `MONTH` (ordinal) incorporates changing weather with the seasons, `TOTAL.PRICE` (quantitative) and `TOTAL.SALES` (quantitative) incorporate economic factors that are driving energy consumption. `TOTAL.CUSTOMERS` (quantitative) adjusts for the fact that some areas are servicing more customers, so the higher usage could lead to more drastic outages.

I used GridSearchCV to find the best hyperparameters for the DecisionTreeClassifier. These were:
- criterion: 'entropy'
- max_depth: 10
- min_samples_split: 5

I used a F1 score to measure the performance of my model. I got an F1 score of 0.902, and since the F1 score increased from the baseline to the final, this indicates better performance of the final model.

# Fairness Analysis
My groups for the fairness analysis are longer vs shorter outages. This is defined as outages that are greater than 3000 minutes, vs outages that are less than 3000 minutes.

I decided on these groups because the cause category (which is predicted by my model) can greatly determine the outage duration. We want to make sure that the model can predict the classification well because this can inform energy companies on what to focus on to prevent longer outages.

My evaluation metric will be F1 score since the classes (longer vs shorter) are imbalanced, and this metric accounts for that imbalance, while also incorporating the precision and recall. I will use permutation tests to calculate the F1 score for longer vs shorter outages (that are randomly shuffled) and then compare this absolute difference to my initial observed absolute difference.

**Null Hypothesis:** The model is fair. Its F1 scores for longer and shorter outages are roughly the same, and any differences are due to random chance.

**Alternative Hypothesis:** The model is unfair. Its F1 score for longer outages is significantly different from the F1 score for shorter outages.

I performed a permutation test with 10000 trials. My significance level is the standard 0.05, and I got a p_value of 0.0 so because this is below the significance level, I reject the null hypothesis. The model is significantly different in terms of F1 score for longer vs shorter outages.

The figure below shows the distribution of the statistic.
<iframe
  src="Website_Resources/fairness_analysis.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>