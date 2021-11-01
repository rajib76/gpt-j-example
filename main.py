from gpt_classes.Example import Example
from gpt_classes.GPTJ import GPTJ

model = GPTJ(model="EleutherAI/gpt-j-6B",
                temperature=1,
                max_length=40)

ex1 = Example('Show 5 rows from a dataframe','df.head(5)')
model.add_example(ex1)
prompt= "Show 6 rows from a dataframe"
best_response = model.get_the_best_response(prompt)
print(best_response)