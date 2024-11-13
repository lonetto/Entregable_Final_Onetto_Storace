_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASTERISK COMMA DOT EQ GT LPAREN LT NUMBER RPAREN SEMICOLON STRING WORDstatement : statement token\n                 | token\n                 | statement SEMICOLON\n                 | token SEMICOLONtoken : WORD\n             | NUMBER\n             | GT\n             | LT\n             | EQ\n             | STRING\n             | LPAREN\n             | RPAREN\n             | COMMA\n             | ASTERISK\n             | DOT'
    
_lr_action_items = {'WORD':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[3,3,-2,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[4,4,-2,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),'GT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[5,5,-2,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),'LT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[6,6,-2,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),'EQ':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[7,7,-2,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),'STRING':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[8,8,-2,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),'LPAREN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[9,9,-2,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),'RPAREN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[10,10,-2,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),'COMMA':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[11,11,-2,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),'ASTERISK':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[12,12,-2,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),'DOT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[13,13,-2,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[0,-2,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),'SEMICOLON':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[15,16,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-1,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'token':([0,1,],[2,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> statement token','statement',2,'p_statement','usql_parser.py',6),
  ('statement -> token','statement',1,'p_statement','usql_parser.py',7),
  ('statement -> statement SEMICOLON','statement',2,'p_statement','usql_parser.py',8),
  ('statement -> token SEMICOLON','statement',2,'p_statement','usql_parser.py',9),
  ('token -> WORD','token',1,'p_token','usql_parser.py',17),
  ('token -> NUMBER','token',1,'p_token','usql_parser.py',18),
  ('token -> GT','token',1,'p_token','usql_parser.py',19),
  ('token -> LT','token',1,'p_token','usql_parser.py',20),
  ('token -> EQ','token',1,'p_token','usql_parser.py',21),
  ('token -> STRING','token',1,'p_token','usql_parser.py',22),
  ('token -> LPAREN','token',1,'p_token','usql_parser.py',23),
  ('token -> RPAREN','token',1,'p_token','usql_parser.py',24),
  ('token -> COMMA','token',1,'p_token','usql_parser.py',25),
  ('token -> ASTERISK','token',1,'p_token','usql_parser.py',26),
  ('token -> DOT','token',1,'p_token','usql_parser.py',27),
]
