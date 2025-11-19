import ollama as o

print('Hi, I am an AI program using the phi3:mini model. How can I help you today?')

while True:

    user_input = input('>>> ')
    if user_input == 'exit':
        print('Have a nice day!')
        break
    else:
        for chunk in o.generate(model='phi3:mini', prompt=user_input, stream=True):
            print(chunk['response'], end='', flush=True)
        print()
