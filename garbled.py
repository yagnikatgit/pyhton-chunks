''' 

Finds secret message from garbled string. 

'''

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

# Step size -2 reveals real message.
message = garbled[::-2]

print(message)
