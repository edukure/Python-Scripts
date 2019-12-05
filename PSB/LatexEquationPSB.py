import re as Regex

pattern1 = Regex.compile(r'(W\d{2}x)')
pattern2 = Regex.compile(r'(W\d{2}\(x)')
pattern3 = Regex.compile(r'(W\d{3})')
pattern4 = Regex.compile(r'(W\d{3}[A-Z])')
pattern5 = Regex.compile(r'(W\d{2}[A-Z])')

inputFile = open("PSB//EquationsPSB", "r")
lines = inputFile.readlines()
inputFile.close()

outputFile = open("PSB//RMarkdownEquations", "w")

for line in lines:
    outputLine = line

    #W20x
    matchArray = pattern1.findall(line)
    for match in matchArray:
        newValue = match[:1] + '_' + match[1] + '^' + match[2:]
        outputLine = outputLine.replace(match, newValue)

    #W20(x
    matchArray = pattern2.findall(line)
    for match in matchArray:
        newValue = match[:1] + '_' + match[1] + '^' + match[2:]
        outputLine = outputLine.replace(match, newValue)

    #W167
    matchArray = pattern3.findall(line)
    for match in matchArray:
        newValue = match[:1] + '_{' + match[1:3] + '}^' + match[3:]
        outputLine = outputLine.replace(match, newValue)
    
    #W160A
    matchArray = pattern4.findall(line)
    for match in matchArray:
        newValue = match[:1] + '_{' + match[1:3] + '}^' + match[3:]
        outputLine = outputLine.replace(match, newValue)

    #W80A
    matchArray = pattern5.findall(line)
    for match in matchArray:
        newValue = match[:1] + '_' + match[1] + '^' + match[2:]
        outputLine = outputLine.replace(match, newValue)

    outputLine = '$$ ' + outputLine[:len(outputLine)-1] + " $$" + '\n'
    print(outputLine)
    outputFile.write(outputLine)

outputFile.close()




