import ply.lex as lex
import ply.yacc as yacc




tokens = (
    'STRING', 'PERSON_TOKEN', 'NAME_TOKEN', "ROLE_TOKEN", "YEAR_TOKEN", "NEWLINE", "END", "NUMBER", "SECTION_TOKEN", 
    "NUMBER_TOKEN", "INSTRUCTER_TOKEN", "ROSTER_TOKEN", "CLASS_TOKEN, "DEPARTMENT_TOKEN"
)

t_STRING    = r'\"[a-zA-Z0-9_]*\"'
t_PERSON_TOKEN = r'person:|Person:'
t_NAME_TOKEN = r'name:|Name:'
t_ROLE_TOKEN = r'role:|Role:'
t_YEAR_TOKEN = r'year:|Year:'
t_DEPARTMENT_TOKEN = r'Department:|department'
t_NUMBER_TOKEN = r'number:|Number:'
t_SECTION_TOKEN = r'section:|Section:'
t_INSTRUCTER_TOKEN = r'Instructor:|Instructor:'
t_ROSTER_TOKEN = r'roster:|Roster:'
t_CLASS_TOKEN = r'class:|Class:'
t_NEWLINE = r'\n'
t_END = r'END'
t_NUMBER = r'[0-9]+'


# Ignored characters
t_ignore = " \t"
    
class_list = []
people_list = []

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

class person_class:
    def __init__(self, name, role, year):
        self.name = name
        self.role = role
        self.year = year

    def print_myself(self, depth):
        print('\t'*depth + "Person: name - " + self.name + ", role - " + self.role + ", year - " + self.year)

class class_class:
    def __init__(self, name, number, section, instructer, roster):
        self.name = name
        self.number = number
        self.section = section 
        self.instructer = instructer
        self.roster = roster


    def print_myself(self, depth):
        
        print('\t'*depth + "Class: name - " + self.name + ", number - " + self.number + ", section - " + self.section, end = "\n" + '\t'*(depth) + "instructer: \n")
        self.instructer.print_myself(depth + 1)
        print('\t'*depth + "roster: ")
        for student in self.roster:
            print('\t'*(depth), end= "")
            student.print_myself(depth)

class department_class:
    def init(self, name, chair, classes):
        self.name = name
        self.chair = chair
        self.classes = classes
    
    def print_myself(self, depth):
        print('\t'*depth + "Department:\nname - " + self.name + ",")

def p_statement_assign(t):
    'statement : class'

def p_class(t):
    'class : CLASS_TOKEN NEWLINE name NEWLINE number NEWLINE section NEWLINE INSTRUCTER_TOKEN NEWLINE person NEWLINE END NEWLINE ROSTER_TOKEN NEWLINE roster NEWLINE END NEWLINE END'

    # t[0] = class_class(t[3], t[5], t[7], t[11], t[17])
    class_list.append(class_class(t[3], t[5], t[7], t[11], t[17]))

    # t[0].print_myself()

def p_number(t):
    'number : NUMBER_TOKEN NUMBER'
    t[0] = t[2]

def p_section(t):
    'section : SECTION_TOKEN NUMBER'
    t[0] = t[2]

def p_roster_one(t):
    'roster : person'
    t[0] = [t[1]]

def p_roster_two(t):
    'roster : roster NEWLINE person'
    t[0] = t[1] + [t[3]]

# def p_department(t):
#     'department : name NEWLINE chair: '






def p_person(t):
    'person : PERSON_TOKEN NEWLINE name NEWLINE role NEWLINE year NEWLINE END'
    t[0] = person_class(t[3], t[5], t[7])
    # t[0].print_myself()

def p_person_one(t):
    'person : PERSON_TOKEN NEWLINE name NEWLINE year NEWLINE role NEWLINE END'
    t[0] = person_class(t[3], t[7], t[5])
    # t[0].print_myself()

def p_person_two(t):
    'person : PERSON_TOKEN NEWLINE role NEWLINE name NEWLINE year NEWLINE END'
    t[0] = person_class(t[5], t[3], t[7])
    # t[0].print_myself()

def p_person_three(t):
    'person : PERSON_TOKEN NEWLINE role NEWLINE year NEWLINE name NEWLINE END'
    t[0] = person_class(t[5], t[7], t[3])
    # t[0].print_myself()

def p_person_four(t):
    'person : PERSON_TOKEN NEWLINE year NEWLINE role NEWLINE name NEWLINE END'
    t[0] = person_class(t[5], t[7], t[3])
    # t[0].print_myself()

def p_person_five(t):
    'person : PERSON_TOKEN NEWLINE year NEWLINE name NEWLINE role NEWLINE END'
    t[0] = person_class(t[5], t[7], t[3])
    # t[0].print_myself()
    # TODO add two more so year can be first but i'm too lazy to do that now

def p_role(t):
    'role : ROLE_TOKEN STRING'
    t[0] = t[2]

def p_name(t):
    'name : NAME_TOKEN STRING'
    t[0] = t[2]

def p_year(t):
    'year : YEAR_TOKEN NUMBER'
    t[0] = t[2]


def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()


s = """Class:
        Name: "software_design"
        Number: 257
        Section: 01
        Instructor:
            Person:
                Name: "James_Ryan"
                Role: "Professor"
                Year: 0000
            END
        END
        Roster:
            Person: 
                Name: "Aiden_Chang"
                Role: "Student"
                Year: 2023
            END
            Person:
                Name: "Owen_Barnett"
                Role: "Student"
                Year: 2022
            END
            Person:
                Name: "Bob"
                Role: "Nothing"
                Year: 298348
            END
        END
    END"""

parser.parse(s)

while(True):
    print("Please type a command, type h for more commands and x to exit: \n")
    x = input()
    if x != 'x' and x != 'h' and x != 'all':
        print("incorrect command")
    else:
        if x == 'x':
            break
        elif x == 'h':
            print('To exit: x\nFor more commands: h\nTo print out the entire parsed list in a string: all\n')
        elif x == 'all':
            print("Classes:")
            for classes in class_list:
                # print('\t', end =" ")
                classes.print_myself(1)
            for people in people_list:
                # print('\t', end =" ")
                people.print_myself(0)
                
     


