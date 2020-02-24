# further exercise using dictionaries
swahili = dict()
swahili['hello'] = 'Jambo'
swahili['blue'] = 'samawati'

print(swahili['hello'])

print("The swahili word for hello is {}".format(swahili['hello']))

print("{hello}, shati langu ni {blue}".format(**swahili))
