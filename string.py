"""String"""

VAR1 = 'some string'

VAR2 = '''
  this is a big case
'''

print('----len(VAR2)----', len(VAR2))
print('\n')
print('----VAR1[1]----', VAR1[1])
print('----VAR1[-1]----', VAR1[-1])
print('----VAR1[1:5]----', VAR1[1:5])
print('----VAR1[:5]----', VAR1[:5])
print('----VAR1[4:]----', VAR1[4:])
print('----VAR1[:]----', VAR1[:])

print('\n')

VAR3 = 'Python \" is awesome'

print('----VAR3----', VAR3)

VAR3 = 'Python \' is awesome'
print('----VAR3----', VAR3)

VAR3 = 'Python \\ is awesome'
print('----VAR3----', VAR3)

VAR3 = 'Python \\ is awesome'
print('----VAR3----', VAR3)

VAR3 = 'Python \n is awesome'
print('----VAR3----', VAR3)

print('\n')

FIRST_NAME = 'Hamidreza'
LAST_NAME = 'Nasrollahi'


# ----------------------------- formatted string ----------------------------- #
FULL_NAME = f"{FIRST_NAME} === {LAST_NAME}"

print('----FULL_NAME----', FULL_NAME)

# ------------------------------ string methods ------------------------------ #
VAR4 = '    python programming   '

print('----FULL_NAME.upper()----', VAR4.upper())
print('----VAR4.lower()----', VAR4.lower())
print('----VAR4.title()----', VAR4.title())
print('----VAR4.rstrip()----', VAR4.rstrip())
print('----VAR4.find("pro")----', VAR4.find("pro"))
print('----VAR4.replace("p","j")----', VAR4.replace("p", "j"))
print('----"pro" in VAR4----', "pro" in VAR4)
print('----"swift" not in VAR4----', "swift" not in VAR4)
