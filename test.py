# -----TODO add hashtag string here to catch for comments 

from parsimonious.grammar import Grammar
grammar = Grammar(
 '''
  test= newline expressions
  roles = newline spaces "roles:" spaces newline spaces single_role+
  single_role = spaces role spaces newline
  role = number_range? spaces input? spaces role_name? spaces chance?

  expressions = (spaces expression spaces newline)+
  expression = code / string / "conditional" / "queue" / "field_value" / number

  spaces = " "*
  newline = "\\n"+
  number = ~"[0-9]+"
  role_name = ~"[initiator | recipient | symbol | location | subject | bystander | absent]+"
  number_range = ~"[<0-9>]+" "-" ~"[<0-9>]+"
  input = "$" ~"[<a-z><A-Z>]+"
  chance = "[0." ~"[<0-9>]+" "]"
  code = "{" ~"[<a-z><A-Z><0-9>*&()^%@!#@,./;'?><:\[\]]+" "}"
  string = ~'"[<a-z><A-Z><0-9>*&()^%@!#@,./;?><:{} ]+"' / ~"'[<a-z><A-Z><0-9>*&()^%@!#@,./;?><:{} ]+'"
'''
)
#    



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


print((grammar.parse(input)))