from ollama import chat
print("__AI CHAT STARTRED__")
messages=[]
while True:
    print("You:",end="")
    user_input=input("")
    if user_input=="exit":
        print("Thanks come again")
        break
    messages.append({"role":"user","content":user_input})
    response=chat(
        model="qwen2.5:3b",
        messages=messages
    )
    print("Boot:",end="")
    boot_response=response.message.content
    print(boot_response)
    messages.append({"role":"assistant","content":boot_response})
print(messages)