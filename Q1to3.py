#1.	A property is an attribute of an object or an aspect of its behaviour. For example, properties 
    #of a code include, syntax, variables etc. To change the characteristics of an object, you change 
    #the values of its properties. 

    #A method is an action that an object can perform. For example, run a program, you can debug a 
    #program etc. Methods often have arguments that qualify how the action is performed. 

    #So, methods are actions and properties are qualities. Using a method causes something to 
    #happen to an object, while using a property returns information about the object or it causes a 
    #quality about the object to change.


#2.	a. arcpy.env.overwriteOutput = True 
    #This is a property. Since, ‘True’ is the quality of the over written output of the arcpy environment, 
    #it can be said that it is a property.
    #b. arcpy.SearchCursor(“roads”, “TYPE” <> 4’) 
    #This is a method. This is because search cursor causes the roads of TYPE, 4, to be accessed(read-only), 
    #which means, it is an action/method on the field. 
    #c. row.setValue(‘distance’,100)
    #This is a method. This is because, this line sets a value of 100, to the distance variable. This means, 
    #the line is performing an action on the variable. 
    #d. ArcGISProject.dateSaved
    #This is a property. This is because, dateSaved is the quality of the ArcGISProject. 
    #e. Table.isBroken
    #This is property. This is because, being broken is the quality of the table.


#3.	def letterFunc (wordParam1, wordParam2): 
    #if (wordParam1[0].lower() == wordParam2[0].lower()): 
    #return True 
    #else: 
    #return False

    #The function is not being called here, and hence, the function itself would not give any 
    #output. The parameters are being passed, the data type of each parameter can be a string, 
    #this is because, if the method lower performed on the parameters, the output is obtained 
    #irrespective of the case, that is the input would not be case sensitive. The output would 
    #be either True, or False, if the function is called or invoked.

