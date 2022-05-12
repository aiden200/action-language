from parsimonious.grammar import Grammar
grammar = Grammar(
 """
   roles = newline spaces "roles:" spaces newline spaces single_role+
   single_role = spaces role spaces newline
   role = number_range? spaces input? spaces role_name? spaces chance?
   spaces = " "*
   newline = "\\n"+
   role_name = ~"[initiator | recipient | symbol | location | subject | bystander | absent]+"
   number_range = ~"[<0-9>]+" "-" ~"[<0-9>]+"
   input = "$" ~"[<a-z><A-Z>]+"
   chance = "[0." ~"[<0-9>]+" "]"

""")

# | <INPUT>: <ROLE_NAME> <CHANCE> | <NUMBER_RANGE> <INPUT>: <ROLE_NAME> 


input = '''
    roles:
        $insulter initiator 
        $insultee recipient
        0-9999 $observer bystander [0.5]
'''.replace('\t', '')

print(grammar.parse(input))