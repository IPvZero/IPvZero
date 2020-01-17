# Python Script to Generate a Genie Testbed file for IOS VIRL images
# Substitute your own username and password
# Modify IP addresses and loop range as required

print("---")
print("testbed:")
print("\n  credentials:")
print("    default:")
print("      username: \"john\"")
print("      password: \"cisco\"")

print("\ndevices:")

for i in range(1, 11):
  print("  R" + str(i) + ":")
  print("    alias: R" + str(i))
  print("    os: ios")
  print("    type: IOSv")
  print("    connections:")

  print("\n      defaults:")
  print("        class: unicon.Unicon")
  print("      console:")
  print("        protocol: ssh")
  print("        ip: 192.168.10." + str(i))
  print("\n    custom:")
  print("      abstraction:")
  print("         order: [os, type]\n")
