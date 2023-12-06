admin = "jackHasAcessToComputerAndKnowsAdmin-Or-RootPassword"
defusrperm = "jackHasAcessToComputerAndDoesNotKnowAdmin-Or-Root-Password"
nocomp = "jackDoesNotHaveAcessToAComputer"

while True:
    if admin == True {
        jack.hackComputer
        break
    }
    elif defusrperm == True {
        jack.getAdminPermsOnComputer
    }
    elif nocomp == True {
        jack.cry
    }
