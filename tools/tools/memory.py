memory = {}

def store(user, data):
    memory[user] = data

def get(user):
    return memory.get(user, {})
