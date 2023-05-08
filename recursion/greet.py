def greet2(name):
    print("hello,",name,"?")

def world():
    print("world!")

def greet(name):
    print("how are you?",name,"!")
    greet2(name)
    print("getting ready to say bye...")
    world()

greet("python")
