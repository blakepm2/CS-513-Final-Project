A description of the actual data cleaning workflow W that was performed, and a comparison with the original Phase-I plan: e.g., were you able to execute the steps as planned, and if not, what did you have to change and why?

1) Convert To Titlecase. Many of the fields below were all capital, which didn't make sense of what they were representing
- Name, Sponser, Event, Venue, Place, Physical Description, Easter, etc

2) Convert notes to lowercase. There are long description of notes in menu.csv. It would make sense to have those notes lowercase. 

3) Cluster Events, since many different variations for the same word, such as Dinner having 10 different variations. Combining them gives much more clarity. 

4) Converted Date String to Date Type so that analysis software can correctly recognize that the columns are indeed dates. 

5) Most values in Dish.csv were numbers. Convert appropriate columns to number type.

6) Repeated same step as 5 for other sheets

7) Removed Menu Items whose price is greater than $100,000, as a menu item greater than 100,000 is not resonable

8) Used Text Faucet and clustering in Venue. Similar reason to #3, where we don't want variations of text that is representing the same word. 

9) Used Date Faucet in First_Appeared_Year and Last_Appeared in Dish.CV to remove years greater than 2025, since it is not possible for menu items to appear in years greater than 2025 (as of the current date)

