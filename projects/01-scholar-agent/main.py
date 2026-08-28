from agent import run_agent

print("welcome to scholarAgent") 
print("Available commands: calculator, count , uppercase")

command = input("what do you want to do ? ") 

result= run_agent(command)

print("Result:",result) 

