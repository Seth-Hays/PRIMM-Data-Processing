# PRIMM: Processing Data
In this PRIMM activity, you will learn how to process data contained in a Comma-Separated Values (CSV) file in order to extract descriptive information from it.

## Predict
First look at the `resources/stolen_bikes.csv` file to understand the data within. Then review the `process_data.py` file to get a sense of the code. **Do not RUN the code yet.**

Answer the following prediction questions:
1. Look at `resources/stolen_bikes.csv`.

    - How many fields are present? 
        > 15 Fields

    - How many records are present?
        > 8,986 Records

    - What types of data are the fields (strings, ints, etc.)?
        > Strings, Ints, Floast, Boolean


2. Look at the `get_records()` function. 

    - How many and what type of arguments does it take?
        > 1 and String

    - What does the function return?
        > A list

3. What would the program print out when run?
    > The first record

## Run
Run the program. 
1. Does the program's output match what you expected? If not, what were the differences?
    > Kinda, differences:  The amount of records read in and the district where it occured

## Investigate
View the instructor's [presentation](https://docs.google.com/presentation/d/186dvW8FcyGPVWGNRolW7RLBhoDX1yBZCGrQT-tGRUuM/edit#slide=id.g32e76c66631_0_7) about CSV files and lists and dictionaries.

## Modify
Write a function called `convert_record_data(record: dict[str, Union[str, int]]) -> None:` that takes a record (dictionary) and converts the fields to the correct data type. It will change the record *in place* meaning, the dictionary that is passed in will be modified.

## Make
Write a function that will help you answer the question: *In which district were the most bikes stolen?*

### Recommendation
Write a function `get_count_by_district(records: list[dict[str, Union[str,int]]]) -> dict[str, int])`. This function takes a record list, will return a dictionary where the keys are the districts and the values are the counts.