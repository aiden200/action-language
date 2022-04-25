
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CLASS_TOKEN DEPARTMENT_TOKEN END INSTRUCTER_TOKEN NAME_TOKEN NEWLINE NUMBER NUMBER_TOKEN PERSON_TOKEN ROLE_TOKEN ROSTER_TOKEN SECTION_TOKEN STRING YEAR_TOKENclass : CLASS_TOKEN NEWLINE name NEWLINE number NEWLINE section NEWLINE INSTRUCTER_TOKEN NEWLINE person NEWLINE END NEWLINE ROSTER_TOKEN NEWLINE roster NEWLINE END NEWLINE ENDnumber : NUMBER_TOKEN NUMBERsection : SECTION_TOKEN NUMBERroster : personroster : roster NEWLINE personperson : PERSON_TOKEN NEWLINE name NEWLINE role NEWLINE year NEWLINE ENDperson : PERSON_TOKEN NEWLINE name NEWLINE year NEWLINE role NEWLINE ENDperson : PERSON_TOKEN NEWLINE role NEWLINE name NEWLINE year NEWLINE ENDperson : PERSON_TOKEN NEWLINE role NEWLINE year NEWLINE name NEWLINE ENDperson : PERSON_TOKEN NEWLINE year NEWLINE role NEWLINE name NEWLINE ENDperson : PERSON_TOKEN NEWLINE year NEWLINE name NEWLINE role NEWLINE ENDrole : ROLE_TOKEN STRINGname : NAME_TOKEN STRINGyear : YEAR_TOKEN NUMBER'
    
_lr_action_items = {'CLASS_TOKEN':([0,],[2,]),'$end':([1,72,],[0,-1,]),'NEWLINE':([2,4,7,8,11,12,15,16,18,19,22,23,24,25,32,33,34,35,36,37,38,39,40,48,49,50,51,52,53,54,55,63,64,65,66,67,68,69,70,],[3,6,-13,10,-2,14,-3,17,20,21,28,29,30,31,-12,-14,41,42,43,44,45,46,47,-4,56,57,58,59,60,61,62,-5,71,-6,-7,-8,-9,-10,-11,]),'NAME_TOKEN':([3,21,30,31,45,46,],[5,5,5,5,5,5,]),'STRING':([5,26,],[7,32,]),'NUMBER_TOKEN':([6,],[9,]),'NUMBER':([9,13,27,],[11,15,33,]),'SECTION_TOKEN':([10,],[13,]),'INSTRUCTER_TOKEN':([14,],[16,]),'PERSON_TOKEN':([17,41,56,],[19,19,19,]),'END':([20,56,57,58,59,60,61,62,71,],[22,64,65,66,67,68,69,70,72,]),'ROLE_TOKEN':([21,29,31,43,47,],[26,26,26,26,26,]),'YEAR_TOKEN':([21,29,30,42,44,],[27,27,27,27,27,]),'ROSTER_TOKEN':([28,],[34,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'class':([0,],[1,]),'name':([3,21,30,31,45,46,],[4,23,37,40,53,54,]),'number':([6,],[8,]),'section':([10,],[12,]),'person':([17,41,56,],[18,48,63,]),'role':([21,29,31,43,47,],[24,35,39,51,55,]),'year':([21,29,30,42,44,],[25,36,38,50,52,]),'roster':([41,],[49,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> class","S'",1,None,None,None),
  ('class -> CLASS_TOKEN NEWLINE name NEWLINE number NEWLINE section NEWLINE INSTRUCTER_TOKEN NEWLINE person NEWLINE END NEWLINE ROSTER_TOKEN NEWLINE roster NEWLINE END NEWLINE END','class',21,'p_class','parser.py',79),
  ('number -> NUMBER_TOKEN NUMBER','number',2,'p_number','parser.py',87),
  ('section -> SECTION_TOKEN NUMBER','section',2,'p_section','parser.py',91),
  ('roster -> person','roster',1,'p_roster_one','parser.py',95),
  ('roster -> roster NEWLINE person','roster',3,'p_roster_two','parser.py',99),
  ('person -> PERSON_TOKEN NEWLINE name NEWLINE role NEWLINE year NEWLINE END','person',9,'p_person','parser.py',111),
  ('person -> PERSON_TOKEN NEWLINE name NEWLINE year NEWLINE role NEWLINE END','person',9,'p_person_one','parser.py',116),
  ('person -> PERSON_TOKEN NEWLINE role NEWLINE name NEWLINE year NEWLINE END','person',9,'p_person_two','parser.py',121),
  ('person -> PERSON_TOKEN NEWLINE role NEWLINE year NEWLINE name NEWLINE END','person',9,'p_person_three','parser.py',126),
  ('person -> PERSON_TOKEN NEWLINE year NEWLINE role NEWLINE name NEWLINE END','person',9,'p_person_four','parser.py',131),
  ('person -> PERSON_TOKEN NEWLINE year NEWLINE name NEWLINE role NEWLINE END','person',9,'p_person_five','parser.py',136),
  ('role -> ROLE_TOKEN STRING','role',2,'p_role','parser.py',142),
  ('name -> NAME_TOKEN STRING','name',2,'p_name','parser.py',146),
  ('year -> YEAR_TOKEN NUMBER','year',2,'p_year','parser.py',150),
]
