from tools import calculator, word_counter, text_uppercase 

def run_agent(command): 
     command = command.lower() 

     if command == "uppercase": 
          text = input("Enter the text:") 
          return text_uppercase(text)

     elif command == "count":
          text = input("Enter text:") 
          return word_counter(text) 

     elif command == "calculator":
          a = float(input("Enter the first number:")) 
          b = float(input("Enter the second number:")) 
          operation = input(
                              "Enter operation (add/substract/multiply/devide):"
                            ) 
          return calculator(a,b,operation) 
     else: 
          return "I don't know which tools to use" 
