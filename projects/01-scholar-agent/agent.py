from tools import calculator, word_counter, text_uppercase 
def run_agent(command):
     command = command.strip().lower() 

     if  "uppercase" in command: 
          text = input("Enter the text:") 
          return text_uppercase(text)

     elif "count" in command:
          text = input("Enter text:") 
          return word_counter(text) 

     elif  "calculator" in command or "calculate" in command:
          a = float(input("Enter the first number:")) 
          b = float(input("Enter the second number:")) 
          operation = input(
                              "Enter operation (add/substract/multiply/devide): "
                            ).strip().lower() 
          return calculator(a,b,operation) 
     else: 
          return "I don't know which tools to use" 
