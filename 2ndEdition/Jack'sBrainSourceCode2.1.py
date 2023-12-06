#############################################################################################################################################
#Definitions for core algorithim

#------Define nocomp-----------------------------------
if (jack.LocateNearestComputer(x64)) == "Located" {
    #Jack does have acess to a computer
    computer = jack.LocateNearestComputer(x64)
    nocomp = False
}
elif ((jack.LocateNearestComputer(x64)) == "notFound"):{
    #Jack does not have acess to a computer
    nocomp = True
}
else:{
    #Brain error
    nocomp = "undefined"
}
#------------------------------------------------------

#-------Define admin and defursperm--------------------
if (nocomp == False): {
    if (jack.attemptToLoginToAdmin(computer)) == "success":{
        #Jack has access to computer and has admin password
        admin = True
        defusrperm = True

    }
    elif (jack.attemptToLoginToAdmin(computer)) == "failButLowUserPerms": {
        #Jack has access to computer and does not know admin password
        defusrperm = True
        admin = False
    }
}
else: {
    break
}
#--------------------------------------------------------

#############################################################################################################################################
#Core algorithm
while True: {
    if (admin == True):{
        jack.hackComputer
        break
    }
    elif (defusrperm == True):{
        jack.getAdminPermsOnComputer
    }
    elif (nocomp == True):{
        jack.cry
        
    }
}
#############################################################################################################################################