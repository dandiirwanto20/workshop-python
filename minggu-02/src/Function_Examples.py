# efinisi fungsi contoh berikut dengan memperhatikan marker / dan *:
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# contoh standard_arg
standard_arg(2)
# 2 (Output)

standard_arg(arg=2)
# 2 (Output)

# contoh pos_only_arg
pos_only_arg(1)
# 1 (Output)

pos_only_arg(arg=1)
# Traceback (most recent call last): (Output Error)
# File "<stdin>", line 1, in <module> (Output Error)
# TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg' (Output Error)

# contoh kwd_only_args
kwd_only_arg(3)
# Traceback (most recent call last): (Output Error)
#  File "<stdin>", line 1, in <module> (Output Error)
# TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given (Output Error)

kwd_only_arg(arg=3)
# 3 (Output)

# pemanggilan dalam definisi fungsi yang sama:
combined_example(1, 2, 3)
# Traceback (most recent call last): (Output Error)
#  File "<stdin>", line 1, in <module> (Output Error)
# TypeError: combined_example() takes 2 positional arguments but 3 were given (Output Error)

combined_example(1, 2, kwd_only=3)
# 1 2 3 (Output)

combined_example(1, standard=2, kwd_only=3)
# 1 2 3 (Output)

combined_example(pos_only=1, standard=2, kwd_only=3)
# Traceback (most recent call last): (Output Error)
#  File "<stdin>", line 1, in <module> (Output Error)
# TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only' (Output Error)