"""with statement"""


#  *************************************
#  *  WHEN WE HAVE A MODULE WHICH HAS  *
#  * .__EXIT__ AND __ENTER__ WE DON'T  *
#  * NEED TO CLOSE THEM AND CLEAR THEM *
#  *************************************

with open('./basic.py') as file:
    print('file opened')
