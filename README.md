# Data Science Diabetes Project

Diabetes mellitus is a chronic metabolic disorder characterized by elevated blood glucose levels resulting from defects in insulin production, insulin action, or both. The disease manifests primarily in two forms: Type 1 diabetes, an autoimmune condition where the pancreas fails to produce insulin, and Type 2 diabetes, characterized by insulin resistance and relative insulin deficiency.

Key risk factors include obesity, genetic predisposition, sedentary lifestyle, hypertension, and dyslipidemia. Long-term complications affect multiple organ systems, including cardiovascular disease, neuropathy, nephropathy, and retinopathy. Management focuses on glycemic control through medication, dietary modifications, physical activity, and regular monitoring.

This project analyzes demographic, clinical, and lifestyle factors associated with diabetes prevalence, exploring correlations between socioeconomic status, health behaviors, and disease outcomes.

## Project Organization

```
├── .gitignore         <- Files and directories to be ignored by Git.
├── environment.yml    <- The requirements file to reproduce the analysis environment.
├── LICENSE            <- Open source license (MIT).
├── README.md          <- Main README for developers using this project.
|
├── dados              <- Data files for the project.
|
├── notebooks          <- Jupyter Notebooks.
│
|   └──src             <- Source code for use in this project.
|      │
|      ├── __init__.py  <- Makes it a Python module.
|      ├── config.py    <- Basic project settings.
|      └── helpers.py   <- Functions created specifically for this project.
|
├── referencias        <- Data dictionaries.
```

## Environment Setup

1. Clone the repository that will be created from this template.

    ```bash
    git clone git@github.com:galhanogabriel/Diabetes-Analysis.git
    ```

2. Create a virtual environment for your project using conda.

    ```bash
    conda env create -f ambiente.yml --name diabetes_analysis
    ```

## More About the Dataset

[Click here](references/data_dictionaries.md) to view the data dictionary

## Summary of Key Results

The analysis confirms hypertension and poor general health status as the strongest predictors of diabetes prevalence, with worsening health levels showing increased disease probability.

The inverse relationship between physical activity and diabetes risk explains the observed associations with mobility limitations and advanced age, as both conditions typically reduce exercise capacity. Socioeconomic factors demonstrate the strongest negative correlations, suggesting better healthcare access, nutritional literacy, and fitness resources mediate diabetes risk.

Data quality limitations were noted, with numerous zero values in certain columns potentially obscuring finer relationships, though the overall patterns remain statistically significant.
