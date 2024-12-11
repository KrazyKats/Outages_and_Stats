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



## Exploratory Data Analysis

### Univariate Analysis
In my exploratory data analysis, I first perform univariate analysis to examine the distribution of single variables.

First, I wanted to see how the number of outages has changed over time.
<iframe
  src="assets/outage_over_time.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>
I also wanted to see the distribution of major causes of power outages.
<iframe
  src="assets/major_causes.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>
Then, I wanted to see the distribution of the number of outages by each U.S. state.
<iframe
  src="assets/map1.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

### Bivariate Analysis
I conducted many bivariate analyses, and the most significant results are shown below.

I examined the relationship between Outage Duration and Customers Affected, two metrics of the severity of a power outage. I expected there to be a positive correlation, since major outages likely affect a lot of customers and have a long duration, but there was variability within this. There are many outages that affected a lot of customers but were not as long, indicating that Customers Affected might be a better metric for measuring outage severity.
<iframe
  src="assets/duration_cust.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

The plot below shows the relation between outage duration and cause category. It shows that some of the outages with the longest duration were due to a fuel supply emergency.
<iframe
  src="assets/duration_cause.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

### Grouping and Aggregates
I grouped by NERC Region and then performed an aggregate function mean() to get the average severity metrics for each region. The severity metrics are Outage Duration, Customers Affected, and Demand Loss. The first few rows of this DataFrame are shown below:

| NERC.REGION   |   OUTAGE.DURATION |   CUSTOMERS.AFFECTED |   DEMAND.LOSS.MW |
|:--------------|------------------:|---------------------:|-----------------:|
| ASCC          |           nan     |                14273 |           35     |
| ECAR          |          5603.31  |               256354 |         1314.48  |
| FRCC          |          4271.12  |               375007 |         1072.6   |
| FRCC, SERC    |           372     |                  nan |          nan     |
| HECO          |           895.333 |               126729 |          466.667 |

I also performed grouping with a pivot table, on Climate Region and Cause Category to see which regions experienced severe weather outages the most. The first few rows of this data frame are shown below:

| CLIMATE.REGION     |   equipment failure |   fuel supply emergency |   intentional attack |   islanding |   public appeal |   severe weather |   system operability disruption |
|:-------------------|--------------------:|------------------------:|---------------------:|------------:|----------------:|-----------------:|--------------------------------:|
| Central            |                   7 |                       4 |                   38 |           3 |               2 |              135 |                              11 |
| East North Central |                   3 |                       5 |                   20 |           1 |               2 |              104 |                               3 |
| Northeast          |                   5 |                      14 |                  135 |           1 |               4 |              176 |                              15 |
| Northwest          |                   2 |                       1 |                   89 |           5 |               2 |               29 |                               4 |
| South              |                  10 |                       7 |                   28 |           2 |              42 |              113 |                              27 |

# Assessment of Missingness

## NMAR Analysis
Several columns contain missing data in the data set, but one of these columns that is likely NMAR is `CUSTOMERS.AFFECTED`. This is because the missingness is likely due to the data collection method, which aggregates data from a variety of sources. If certain companies did not report the number of customers that were affected, then there would be missing values.

Additional data I could collect to determine if `CUSTOMERS.AFFECTED` is MAR is to collect the individual reporting companies for each outage, and then conduct analysis to see whether the missingness of the customers is dependent on the company.

## Missingness Dependency
To test missingness dependency, I will focus on the distribution of `OUTAGE.DURATION`. I will test this against the columns `CAUSE.CATEGORY` and `MONTH`.

### Cause Category
First, I examine the distribution of Cause Category when Duration is missing vs not missing.

**Null Hypothesis:** The distribution of Cause Category is the same when Duration is missing vs not missing.

**Alternate Hypothesis:** The distribution of Cause Category is different when Duration is missing vs not missing.


 I found an observed TVD of 0.444 which has a p value of 0.0. The empirical distribution of the TVDs is shown below. At this value, I reject the null hypothesis in favor of the alternate hypothesis, which is that the distribution of Cause Category is significantly different when Duration is missing vs not, indicating that the missingness of Duration is dependent on Cause Category.
<iframe
  src="Website_Resources/missing_MAR.html"
  width="800"
  height="600"
  frameborder="0"
></iframe>

### Month
Next, I examined the dependency of Duration missing on another column, `MONTH`.
**Null Hypothesis:** The distribution of Month is the same when Duration is missing vs not missing.

**Alternate Hypothesis:** The distribution of Month is different when Duration is missing vs not missing.

Here is the distribution of Month when Duration is missing vs not missing.

I found an observed TVD of 0.143. This had a p value of 0.1756. The empirical distribution of the TVDs is shown below. At this value, I fail to reject the null hypothesis in favor of the alternate hypothesis. The distribution of Month is not significantly different when Duration is missing vs not, indicating that the missingness of Duration is not dependent on Month.
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
My model will try to predict the cause of a power outage. This will be a binary classification because we are only focusing on outages cause by severe weather or intentional attacks.

The metric I am using the evaluate my model is the F1 score, because there is an imbalance within the classes so this will most effectively balance that out and incorporate both the precision and recall.

At the time of prediction, we would know the state, NERC region, climate region, anomaly level, year, month, total sales, total price, total customers, and the urban factor. This information will allow us to predict what the cause of a major power outage is.

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