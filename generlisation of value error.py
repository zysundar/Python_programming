def readval(valtype,requestmsg,errormsg):
    while True:
        val=raw_input(requestmsg+' ')
        try:
            val=valtype(val)
        except ValueError:
            print val,errormsg
            break
            
