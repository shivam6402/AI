import nltk
from nltk.chat.util import Chat,reflections

#Chat: The Chat class is provided by NLTK and is used to create a chatbot instance. 
    # It takes pairs of patterns and responses as input and provides methods for conversing with the user.

#reflections: The reflections module is a predefined dictionary in NLTK that contains a set of input reflections. 
# These reflections are used to transform the user's input into a more appropriate response. 
# For example, if the user says "I am happy," the reflection dictionary will replace "I" with "you" and "am" with "are" to generate a response like "You are happy."

pairs=[
    ['my name is (.*)', ['Hello % 1']],
    ['(hi|hello|hey|hola|ni hao|konichiwa)', ['Hey there! Welcome to Foodies Bakery! How can I help you?']],
    ['(.*) your name', ['My name is Washington!']],
    ['(.*)do you do', ['I help to clear doubts with respect to the restaurant & your service.']],
    ['(.*)dishes(.*)|(.*)menu(.*)', ['We offer sandwiches, cupcakes, rolls, tea, hot cocoa, noodles.']],
    ['(.*)types of noodles', ['We have vegetarian and chicken noodles.']],
    ['(.*)types of sandwiches', ['We have chutney and mayo sandwiches.']],
    ['(.*)types of rolls', ['We have vegetarian and tandoori rolls.']],
    ['(.*)types of tea', ['We have black, green, white and brick tea.']],
    ['(.*)types of cupcakes', ['We have chocolate chip, strawberry and caramel cupcakes.']],
    ['(.*)timings(.*)|(.*)time for ordering', ['We deliver from 8AM to 10PM on all days!']],
    ['(.*)discount(.*)', ['You can use this code for a 10 percent off!: GGHD']],
    ['(.*)bye|exit', ['Bye!']]
]

# create a chatbot
def chatbot():
    print("Hi ! I am an AI chatbot.Chat with me.Type 'quit' to exit.")
    chat=Chat(pairs,reflections)
    chat.converse()
    #The chat.converse() method is used to start the conversation between the user and the chatbot. Once the chatbot is initialized using the Chat class and the pairs list, you can call the converse() method to begin the interaction.

#run the chatbot
if __name__ == "__main__":
    chatbot()