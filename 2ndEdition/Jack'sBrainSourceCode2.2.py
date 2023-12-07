##############################################################################################################################################
#---------------Setup--------------------------------
import socket

# Get the local IP address
ip = socket.gethostbyname(socket.gethostname())

# Create a list of all the computers on the network
computers = [ip for ip in range(192, 192 + 256) if ip in socket.gethostbyname_ex(ip)[2]]

computers = 0
#############################################################################################################################################
#Definitions for core algorithim
#-------Define-LocateNearestComputer--------------------
# Ping each computer
def LocateNearestComputer():
    for computer in computers:
      try:
          socket.create_connection((computer, 80))
          computers = computers + 1
      except socket.error:
          computers = computers

#--------Define-Cry------------------------------------
def cry():
    print(":'(")

#------Define nocomp-----------------------------------
if (LocateNearestComputer()) >> 0:
    #Jack does have acess to a computer
    computer = LocateNearestComputer()
    nocomp = False

elif ((LocateNearestComputer()) << 1):
    #Jack does not have acess to a computer
    nocomp = True

else:
    #Brain error
    nocomp = "undefined"

#------------------------------------------------------
def WORK_IN_PROGRESS():
    #-------Define-admin-and-defursperm--------------------
    #if (nocomp == False): 
        #if (attemptToLoginToAdmin(computer)) == "success":
            #Jack has access to computer and has admin password
            #admin = True
            #defusrperm = True

    
        #elif (attemptToLoginToAdmin(computer)) == "failButLowUserPerms": 
            #Jack has access to computer and does not know admin password
            #defusrperm = True
            #admin = False
    

    #--------------------------------------------------------

    #############################################################################################################################################
    #Core algorithm
    #while True: 
        #if (admin == True):
            #hackComputer()
            #break
    
        #elif (defusrperm == True):
            #getAdminPermsOnComputer()
    
        #elif (nocomp == True):
            #cry()
        
    

    #############################################################################################################################################