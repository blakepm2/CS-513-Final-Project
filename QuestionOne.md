A description of the actual data cleaning workflow W that was performed, and a comparison with the original Phase-I plan: e.g., were you able to execute the steps as planned, and if not, what did you have to change and why?

1) Convert To Titlecase. Many of the fields below were all capital, which didn't make sense of what they were representing. For example, name of "ANSHUL GOSWAMI" should be titlecase. 
2) - Name, Sponser, Event, Venue, Place, Physical Description, Easter, etc

3) Convert notes to lowercase. There are long description of notes in menu.csv. It would make sense to have those notes lowercase since they are representing full paragraphs of notes. Titlecase would not make sense in this case. 

4) Cluster Events, since many different variations for the same word, such as Dinner having 10 different variations. Combining them gives much more clarity. For example, Dinnr, D!nner, diner, were all combined into "Dinner". We don't want mispelling of words because the user will not be able to clearly filter by one keyword such as "Dinner" 

5) Converted Date String to Date Type so that analysis software can correctly recognize that the columns are indeed dates. OpenRefine wasn't able to automatically convert to date format so used string transformatio to convert dates prevent into a format that Open Refine was able to recognize. This is a neccessary step so that analysis software can filter by date if neccessary. 

6) Most values in Dish.csv were numbers. Convert appropriate columns to number type so that software can be treated as numbers. Import as fields need to be numeric data in order to be used for quantative analysis. 

7) Repeated same step as 5 for other sheets

8) Removed Menu Items whose price is greater than $100,000, as a menu item greater than 100,000 is not resonable. This was a neccessary step as these outliers should not skew any quantative analysis of data. 

9) Used Text Faucet and clustering in Venue. Similar reason to #3, where we don't want variations of text that is representing the same word. 

10) Used Date Faucet in First_Appeared_Year and Last_Appeared in Dish.CV to remove years greater than 2025, since it is not possible for menu items to appear in years greater than 2025 (as of the current date). This is neccessary as it is impossible to have current data representing years greater than 2025. 

