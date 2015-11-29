def create_answer(label, type, value):
    # Question(label=label, type=type, value=value)
    return {
        'question_label': label,
        'type': type,
        'value': value,
    }


class Question:
    def __init__(self, label=None, type=None, value=None):
        self.label = label
        self.type = type
        self.value = value


dir(__builtins__)

answers = [create_answer('dateOfShipped', 'text', '2015-11-16'), create_answer("dateOfReceipt", 'text', '2015-11-19')]

for answer in answers:
    if answer['question_label'] == 'dateOfReceipt':
        print(answer['value'])

print(filter(lambda answer: answer['question_label'] == 'dateOfReceipt', answers)[0]['value'])
