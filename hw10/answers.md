# When dealing with human coded data, it can be tempting to throw out data items that did not have perfect or majority agreement. Why is this a bad practice?
This can be problemmatic since throwing out these outlying data points may lead to a loss of important information about the variability/complexity of human opinions and behaviours. The disagreements can reveal ambiguities in the typology or reflect differences in human interpretation (valuable for understanding limitations of the data and analysis). It may also introduce bias - since the kept data would represent the more straightforward cases only.

# Consider the following analysis tasks. Rank them by the degree to which they are fishing expeditions. Explain your ranking.
- Measure the correlation between outside temperature and the amount of foot traffic on St. Laurent on a Saturday night.
Least since it specifies 2 concrete variables: temperature and foot traffic. it has a concrete outcome in mind - the correlation between the temperature and foot traffic.
- Identify the kinds of locations where people go on St. Laurent.
A bit more precise than the next option, since there is a relative focus on the kinds of locations people go for. it is still fishing for a target though.
- Identify the dietary preferences of people who shop on St. Laurent.
Dietary preferences is a braod and variable topic that lacks guidance in data collection, making it very open ended.

# For the most extreme fishing expedition identified in #1, explain how more work in the data annotation phase would avoid/limit the open-ness of the question.
well defined categories in the typology (that specifies the dietary options), data collection focus (ensure that the annotators know what to loook for)

# Diagram and explain how the desire to use automated data annotation can lead to a secondary data science project.
initial project goal: annotate data automatically -> automated annotation setup -> data issues identified -> secondary project: improve annotaiton algorithm (tasks: data clenaing, developing machine learning models, optimizinf performance)
- might realise the model struggels with accuracy due to noisy/ambiguous data. we might need a secondary project to improve the annotation algorithm - developing better models, refininf data cleaning process and handling edge cases.

# For each question below, identify the type of answer required (definition, process, or motivation) and give a precise answer for a young child audience (say somewhere around 5-6 years old).
- What is an airplane?
definition: a big machine with wings that flies high up in the sky and carries people or things from one place to another
- Why do we have stoplights?
explanation of motivation: to keep everyone safe on the roads. they help people and cars know when to stop and go so that noone gets hurt.
- When is it appropriate to yell “Fire” in a crowded room?
explanation of process: only if there is a fire in the room.
- How do you eat an apple?  
explanation of process: wash the apple so that it is clean, then hold it in your hand and take a bite with your teeth. chew it before swallowing and repeatedely take bites until only the apple core is left.