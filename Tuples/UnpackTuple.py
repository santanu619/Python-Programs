'''
@Author: Santanu Mohapatra
@Date: 11/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 12:00 PM
@Title:Program to unpack a tuple of different variables
'''
import logging
import loggerconfig

class Tuple:
    def createTuple():
        '''
        Description: Function is used to unpack a tuple of different variables.
        Parameters: Tuples.
        Return: None.
        ''' 
        try:
            details = (1,"Santanu","Mohapatra", "201700005")
            (student_id, student_firstName, student_lastName, student_registrationNumber) = details
            logging.info(student_id, student_firstName, student_lastName, student_registrationNumber)
        
        except Exception as e:
            logging.error(e)

class invalidTupleError(TypeError):
    logging.warning("Invalid pattern of tuple")
    pass

if __name__=="__main__":
    tuple = Tuple()
    tuple.createTuple()
    invalidTupleError(logging.ERROR)

