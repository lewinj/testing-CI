
#from OMPython import OMCSessionZMQ
#omc = OMCSessionZMQ()
#omc.sendExpression("getVersion()")
#omc.sendExpression("cd()")
#omc.sendExpression("loadModel(Modelica)")
#omc.sendExpression("loadFile(getInstallationDirectoryPath() + \"/share/doc/omc/testmodels/BouncingBall.mo\")")
#omc.sendExpression("instantiateModel(BouncingBall)")
#omc.sendExpression("simulate(BouncingBall, outputFormat="csv", startTime=0, stopTime=4, numberOfIntervals=5)")
from OMPython import OMCSessionZMQ
omc = OMCSessionZMQ()
cmds = [
  'loadFile(getInstallationDirectoryPath() + "/share/doc/omc/testmodels/BouncingBall.mo")',
  "simulate(BouncingBall)",
  "plot(h)"
  ]
for cmd in cmds:
  answer = omc.sendExpression(cmd)
  print("\n{}:\n{}".format(cmd, answer))
