# gpt-j-example
This repository has the code to show how to add examples to GPT-J-6B similar to GPT-3. 
This has been inspired from the code provided in the below link 
https://github.com/NielsRogge/Transformers-Tutorials/blob/master/GPT-J-6B/Inference_with_GPT_J_6B.ipynb 
and the "add example" approach in GPT-3.I have wrapped the code in two classes Eaxmple and GPTJ. 
The Example class has been developed to create the examples as an object and passed to the 
GPT model. The GPTJ class has the run_model module which executes the model by adding the 
examples to the given prompt. The output response is parsed and the best answer is returned by 
the model.

This is the first version of the code. I intend to make improvements incrementally to this 
version of the code. Any suggestions and improvement ideas are welcome. This code has been executed
in a Vertex AI Notebook instance which has a RAM size of 104GB(n1-highmem-16 (16 vCPUs, 104 GB RAM).
