def escape_by(plan):
  if (plan == "jump over"):
    print ("we cannot escape by jumping over as the boulder is too big")
  elif (plan == "run around"):
    print ("we cannot escape by running around as the boulder is too fast")
  elif (plan == "go deeper"):
    print ("that may work let's go deeper")
  else:
    print("Wecannot escape that way as the boulder is in the way")

escape_by("jump over")
escape_by("run around")
escape_by("go deeper")

