import torch
from transformers import GPTJForCausalLM, AutoTokenizer


class GPTJ:
    def __init__(self, model="EleutherAI/gpt-j-6B",
                 temperature=1,
                 max_length=100):
        self.examples = []
        self.model = model
        self.temperature = temperature
        self.max_length = max_length

    def add_example(self, ex):
        self.examples.append(ex.format_example())

    def add_all_examples(self):
        return '\n'.join(self.examples) + '\n'

    def add_example_to_prompt(self, prompt):
        return self.add_all_examples() + "input: " + prompt + "\noutput:"

    def run_model(self, prompt):

        model = GPTJForCausalLM.from_pretrained(self.model)
        tokenizer = AutoTokenizer.from_pretrained(self.model)
        mod_prompt = self.add_example_to_prompt(prompt)
        input_ids = tokenizer.encode(str(mod_prompt), return_tensors="pt")

        # The below try block is required to ensure that the max lenght
        # is more than the lenght of the input tokens lenght
        try:
            len_input_ids = len(input_ids[0])
            if len_input_ids > self.max_length:
                print("Token length of input : {len_input_ids}".format(len_input_ids=len_input_ids))
                print("Max length provided : {max_length}".format(max_length=self.max_length))
                raise Exception("Max length must be more than input token length")
        except Exception as e:
            print("An exception has occurred :{message}".format(message=e))
            raise

        generated_ids = model.generate(input_ids, do_sample=True,
                                       temperature=self.temperature,
                                       max_length=self.max_length)
        generated_text = tokenizer.decode(generated_ids[0])

        return generated_text

    def get_the_best_response(self, prompt):
        response = self.run_model(prompt)
        response_list = response.split("####")
        response_position = len(self.examples)
        return response_list[response_position]
