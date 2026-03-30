data = [ ]
variable = [ ]
output = []
def print_statement(line):
    temp = ""
    if line[0] == '<' and line[len(line) - 1] == '>' and line[1] == '"' and line[len(line) - 2] == '"':
        temp = line[1:len(line) - 1]
        output.append(temp)                                                        #sample statement:
    elif line[1:len(line) - 1] in variable:                                        # <"Hello World"> or <name>
        output.append(data[variable.index(line[1:len(line) - 1])])
    else:
        output.append("SYNTAX ERROR")
    
def input_statement(line):
    if line[0:3] == "vin":
        prompt = str(line[4:len(line) - 1]) 
        var = input(prompt + ": ")
        if line[3] == '<' and line[len(line) - 1] == '>':
            data.append(var)
            variable.append(prompt)                              #sample statement:
        else:                                                    #vin (variable input)
            output.append("SYNTAX ERROR")                        
    else:                                                        #vin<name> 
        output.append("SYNTAX ERROR")

enter = input("")
commands = []
while enter != "run":
    commands.append(enter)
    enter = input("")
for i in range(len(commands)):
    temp = commands[i]
    if temp[0] == "v":
        input_statement(temp)
    else:
        print_statement(temp)
        pass


print ("__________________ OUTPUT __________________")
for j in output:
    print (j)
print("Over")