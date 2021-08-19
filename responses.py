from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi', 'sup'):
        return 'Hey! How is it going?'

    if user_message in ('who are you', 'who are you?'):
        return 'I am Bot, Buddy Bot!'

    if user_message in ('where are you', 'where are you?'):
        return 'Nowhere and everywhere at the same time!'

    if user_message in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime('%m/%d/%y, %H:%M:%S')
        return str(date_time)

    return 'I do not understand you.'