from parsimonious.grammar import Grammar
grammar = Grammar(
 """
    roles = newline spaces "roles:" spaces newline spaces list_of_roles
    list_of_roles = role*
    role = number_range? spaces input? spaces ":" spaces role_name? spaces chance?
    spaces = " "*
    newline = "\\n"+
    role_name = "initiator | recipient | symbol | location | subject | bystander | absent"+
""")

# | <INPUT>: <ROLE_NAME> <CHANCE> | <NUMBER_RANGE> <INPUT>: <ROLE_NAME> 

input = '''
roles: 
   test   '''.replace('\t', '')


print(grammar.parse(input))