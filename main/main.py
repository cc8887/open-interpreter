import interpreter

interpreter.reset()
interpreter.model = "gpt-3.5-turbo"
interpreter.debug_mode = True
messages = interpreter.chat("""Please perform the calculation 27073*7397 then reply with just the integer answer with 
no commas or anything, nothing else.""", return_messages=True)
print(messages)
