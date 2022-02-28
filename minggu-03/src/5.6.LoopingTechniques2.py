questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# What is your name?  It is lancelot. (Output)
# What is your quest?  It is the holy grail. (Output)
# What is your favorite color?  It is b (Output)