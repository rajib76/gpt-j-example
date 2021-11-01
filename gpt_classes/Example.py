class Example():
    """
    This class is used to create the examples as an object and then add to the
    model before running the model.
    """
    def __init__(self, ex_input, ex_output):
        self.ex_input = ex_input
        self.ex_output = ex_output

    def set_input(self, input):
        self.ex_input = input

    def get_input(self):
        return self.ex_input

    def set_output(self, output):
        self.ex_output = output

    def get_output(self):
        return self.ex_output

    def format_example(self):
        return f"input: {self.ex_input}\noutput: {self.ex_output}\n####"
