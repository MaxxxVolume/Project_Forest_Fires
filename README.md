# Project: Forest Fire Data Analysis (1881-2025)

This is a complete end-to-end Exploratory Data Analysis (EDA) and Machine Learning experiment on a (synthetic) global forest fire dataset. The goal was to identify patterns in fire occurrences and attempt to predict the `Burned_Area_Ha` based on climatic, temporal, and geographic features.
The used [Dataset](https://www.kaggle.com/datasets/berkekarakanl/global-wildfires-and-climate-dataset-18812025) is by Berke Karakanli.

## 1. Exploratory Data Analysis (EDA) - Key Findings

The analysis uncovered several key, and often contradictory, insights into the dataset.

### Insight 1: Frequency vs. Severity (The Country Analysis)

Analyzing the fires by country revealed that the sheer *count* of fires does not tell the full story.

* **Frequency (`Fires_Count`):** Turkey and the USA lead the list with the highest *number* of fire incidents.
* **Severity (`Burned_Area_Ha`):** The USA and Turkey also lead in *total cumulative damage*.
* **The Anomaly (Spain vs. France):** While France ranked 3rd for *number* of fires, it was near the bottom for *total area burned*. Spain showed the exact opposite pattern: few fires, but catastrophic damage.

This led to analyzing the "Destructiveness" (`Area_per_Fire`), which revealed that **Italy and Spain** have the most devastating fires on average, while the numerous fires in the USA and Turkey are, on average, much smaller.

### Insight 2: The "Why" Question (The Climate Dashboard)

Analyzing the three climate drivers (Temperature, Humidity, Wind) revealed a complex picture:

* **Spain** represents a "perfect storm": It exhibits the highest median temperature, the lowest median humidity, and high wind speeds, clearly explaining its destructive fire profile.
* **USA & Turkey** are the opposite: They show cool median temperatures and high median humidity, which explains why their fires, despite their high frequency, are less severe on average.
* **The Enigma (Italy & Australia):** Despite being top-tier for `Area_per_Fire`, both countries were found to be in the "mid-field" for *all three* climate indicators.

**Conclusion:** The severity of a fire is not driven by a single climate factor but by a complex interaction that is not visible in simple 1-to-1 plots.

### Insight 3: The "When" Question (Seasonality & Trend)

* **Seasonality:** The data shows a clear "fire season" concentrated in the Northern Hemisphere's summer months (May-Oct). This is a fascinating **bias** in the dataset, as major Southern Hemisphere countries (Australia, Brazil) are included, but their real-world fire seasons are ignored.
* **Long-Term Trend:** The interactive time-series plot shows **no clear upward or downward trend** over the 140-year period. Instead, it demonstrates high volatility and appears to be stationary "random noise." This is another strong indicator of the data's synthetic nature.

**[Link to the interactive time-series plot (1881-2025)](yearly_trend_plot.html)**

### Insight 4: The "Cause" Question (The Human Factor)

Analyzing the `Cause` of fires revealed:

* 'Human', 'Unknown', and 'Lightning' are the most common individual categories.
* However, by re-classifying 'Climate Change' and 'Deforestation' as "human-made" (which they are), a new conclusion emerges: **At least 3 out of 4 fires of known origin in this dataset are attributable to human activity.**

---

## 2. Machine Learning Analysis: A Successful Failure

The goal was to train a `RandomForestRegressor` model to predict the `Burned_Area_Ha` (`y`) using all other features (`X`).

### The Result: Total Model Failure

* **Mean Absolute Error (MAE):** 26,725 Ha. The model's average error was over 50% of the dataset's mean fire size.
* **R-Squared (R²) Score:** **-0.041 (or -4.1%)**

A negative R² score signifies that the complex model performed **worse** than a naive baseline model that simply guesses the average. The model was unable to find any valid, learnable patterns.

### The Autopsy: Feature Importance

The final `feature_importance_` plot confirmed *why* the model failed:

* The model deemed the other "random" numerical columns (`Fires_Count`, `Year`, `Temp`, `Wind`, `Humidity`) as the most important predictors.
* The features that *should* have told the story (e.g., `Country_Italy` or `Cause_Human`) had importance scores near zero.

---

## 3. Overall Project Conclusion

The Exploratory Data Analysis (EDA) successfully proved that this dataset is **synthetic** and **internally inconsistent**.

* It lacks a logical long-term trend, despite climate data.
* Its seasonality ignores the geography of its own subjects (Southern Hemisphere).
* Its climate features (`Temp`, `Wind`, etc.) have **no meaningful linear correlation** to the fire severity (`Burned_Area_Ha`).
* The Machine Learning model **mathematically confirmed** this by failing catastrophically (R² = -4.1%), proving that there were no real, complex patterns to be found.

This project was a complete success in demonstrating the full data science workflow (EDA, ML, Evaluation) to rigorously analyze a dataset and prove its (synthetic) limitations.
