print("Python Program to Remove Punctuation from a String")

punctuations = ('''''!()-[]{};:'"\,<>./?@#$%^&*_~''')
message =input("Enter Message:")

storage = ""
for characters in message:
    if characters not in punctuations:
        storage = storage +characters
print(storage)




