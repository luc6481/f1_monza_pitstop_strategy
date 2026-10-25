F1 Monza Pitstop Strategy:

This project is to teach a Random Forest model to understand Formula One Pit Stop Strategies. I have one folder on the gathering data aspect and one on the machine learning aspect

Data Acquisition:
In most files, there are lines that have "CHANGE_ME". Replace this text with the path to your dataset in quotations.

The data acquisition is to be run in this order:
1. project_data_update1
2. project_data_update2
3. combining_datasets
4. adding_extra_data
5. finalizing_data

If you want more data, you can run the scraper and the following code in this order after you run the ones above:
1. bs4_starter_scraper
2. adding_positions_csv_scraped
3. combining_scraped_data
4. combining_scraped_and_nonscraped

There are still some lines with missing data, you can delete these to make the dataset run in a machine learning model. Updates may come where I fix this.

ML:
The most recent version of the model is the file called adding_extension within the directory called random_forest_classifier. The other ML files are for experimentation or my MVP and are not the final product.