# -----TODO add hashtag string here to catch for comments 

from parsimonious.grammar import Grammar
grammar = Grammar(
 '''
  action = ("special action" spaces name ":" newline manditory_body) / ("action" spaces name ":" newline manditory_body) 
  manditory_body = gloss newline roles newline body? newline? salience newline body? newline?
  body = (preconditions newline body) / (effects newline body) 

  test= newline expressions
 
  gloss = "gloss:" spaces string spaces newline
  effects = newline spaces "effects:" newline expressions
  roles = newline spaces "roles:" spaces newline spaces single_role+
  salience = ("salience:" newline expressions) / ("saliences:" newline expressions)
  preconditions = "preconditions:" newline expressions
  single_role = spaces role spaces newline
  role = number_range? spaces input? spaces role_name? spaces chance?


  expressions = (spaces expression spaces newline)+
  expression = code / string / "conditional" / "queue" / "field_value" / number
  
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

  name = ~'[<a-z><A-Z><0-9>*&()^%@!#@,./;?><:}{- ]'+
  spaces = " "*
  newline = "\\n"*
  optional_newline= "\\n"*
  number = ~"[0-9]+"
  role_name = ~"[initiator / recipient / symbol / location / subject / bystander / absent]+"
  number_range = ~"[<0-9>]+" "-" ~"[<0-9>]+"
  input = "$" ~"[<a-z><A-Z>]+"
  chance = "[0." ~"[<0-9>]+" "]"
  code = "{" ~"[<a-z><A-Z><0-9>*&()^%@!#@,./;'?><:\[\]]+" "}"
  string = (~'"[<a-z><A-Z><0-9>*&()^%@!#@,./;?><:{} ]+"') / (~"'[<a-z><A-Z><0-9>*&()^%@!#@,./;?><:{} ]+'")
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
'''

print((grammar.parse(input)))