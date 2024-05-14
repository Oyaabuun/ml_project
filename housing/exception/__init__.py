import os
import sys

class HousingException(Exception):
    
    def __init__(self, error_message:Exception,error_detail:sys): # we are capturing
        super().__init__(error_message) #we are passsing to the exception class, super means to parent class initializer we are passsing the information
        self.error_message=HousingException.get_detailed_error_message(error_message=error_message,
                                                                       error_detail=error_detail
                                                                        )


    @staticmethod #return line no fileno everything you dont need objectt to call the function from the class, you can directly use the class name when you call a static method
    def get_detailed_error_message(error_message:Exception,error_detail:sys)->str:
        """
        error_message: Exception object
        error_detail: object of sys module
        """
        _,_ ,exec_tb = error_detail.exc_info() #exe_info return three things :- type,vale,traceback , since we dont need the 1st and 2nd so we used _ as variable
        exception_block_line_number = exec_tb.tb_frame.f_lineno #from traceback we extracted linenumber and filename
        try_block_line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"""
        Error occured in script: 
        [ {file_name} ] at 
        try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] 
        error message: [{error_message}]
        """
        return error_message

    def __str__(self): #str shows what should be displayed in the print statement when we print the object of any class
        return self.error_message


    def __repr__(self) -> str: #repr is object representation, it shows the object in the form of string
        return HousingException.__name__.str()

