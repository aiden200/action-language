# -----TODO add hashtag string here to catch for comments 

from parsimonious.grammar import Grammar
grammar = Grammar(
 '''
  action = (spaces newline "special action" spaces name ":" newline manditory_body) / (spaces newline"action" spaces name ":" newline manditory_body) 
  manditory_body = gloss newline roles newline body? newline? salience newline body? newline?
  body = (preconditions newline body) / (effects newline body) 

  test= newline expressions
 
  gloss = spaces newline? "gloss:" spaces string spaces newline
  effects = newline spaces "effects:" newline expressions
  roles = newline spaces "roles:" spaces newline spaces single_role+
  salience = (spaces? newline? "salience:" newline expressions) / (spaces? newline? "saliences:" newline expressions)
  preconditions = "preconditions:" newline expressions
  single_role = spaces role spaces newline
  role = number_range? spaces input? spaces role_name? spaces chance?

  expression = (field_value / code  / string  / conditional / queue / number)
  expressions = (spaces expression newline?)+
  field_value = spaces string spaces? ":" spaces (code / input) spaces newline?
  conditional = (if (else / multilineelse)?) / (multilineif (else / multilineelse)?) / (loop / multilineloop)
  loop = spaces "loop" spaces code spaces "as" spaces input spaces ":" spaces newline? spaces expression spaces newline?
  multilineloop = spaces "loop" spaces code spaces "as" spaces input spaces ":" spaces newline spaces "begin" spaces newline spaces expressions spaces newline? spaces "end" spaces newline? spaces
  multilineif = spaces "if" spaces code spaces ":" spaces newline spaces "begin" spaces  newline spaces expressions spaces newline? spaces "end" spaces newline?
  multilineelse = spaces "else" spaces ":" spaces newline spaces "begin" spaces newline spaces expressions spaces newline? spaces "end" spaces newline?
  else = spaces "else" spaces ":" spaces newline spaces expression spaces newline?
  if = spaces "if" spaces code spaces ":" spaces newline spaces expression spaces newline?
  
  queue = ("urgent queue" spaces more_actions ":" newline queue_body) / ("queue" spaces more_actions ":" newline queue_body) 
  queue_body = bindings? newline priority? newline expiration_code? newline kill_code? newline location? newline time_of_day? newline abandon? newline
  more_actions = string
  bindings = "bindings:" newline bindings_body
  bindings_body = string ":" spaces input newline bindings_body?
  priority = "priority:" spaces number
  expiration_code = "expiration_code:" spaces code
  kill_code = "kill_code:" spaces code
  location = "location:" spaces code
  time_of_day = "time_of_day:" spaces code
  abandon = "abandon:" spaces code

  name = ~'[<a-z><A-Z><0-9>*&()^%@!#@,./;?><-]+'
  spaces = " "*
  newline = "\\n"*
  optional_newline= "\\n"*
  number = ~"[0-9]+"
  role_name = ~"[initiator / recipient / symbol / location / subject / bystander / absent]+"
  number_range = ~"[<0-9>]+" "-" ~"[<0-9>]+"
  input = "$" ~"[<a-z><A-Z>]+"
  chance = "[0." ~"[<0-9>]+" "]"
  code = "{" ~"[<a-z><A-Z><0-9>*&()^%@!#@,./;'?><:\[\]]+" "}"
  string = (~'"[<a-z><A-Z><0-9>*&()^%@!$#@,./;?><{} ]+"') / (~"'[<a-z><A-Z><0-9>*&()^%@$!#@,./;?><{} ]+'")
'''
)
#    
# string = ~'"[<a-z><A-Z><0-9> _}{,.?]+"' / ~"'[<a-z><A-Z><0-9> _}{,.?]+'"
# | <INPUT>: <ROLE_NAME> <CHANCE> | <NUMBER_RANGE> <INPUT>: <ROLE_NAME> 


input = '''
    roles:
        $insulter initiator 
        $insultee recipient
        0-9999 $observer bystander [0.5]
'''.replace('\t', '')

input = """
'test'
"test"
{tes't's}
"""

input = '''
gloss: '{traveler.name} decides to go to {destination.name}'
'''

input = '''
special action contemplate-serial-mistreatment:
    gloss: "{$mistreated.name} contemplate serial mistreatment by {$mistreater.name}"
    roles:
        $mistreated initiator
        $mistreater absent
    salience:
        $mistreated: 100
'''.replace('\t', '')



print((grammar.parse(input)))