from OMPython import OMCSessionZMQ
omc = OMCSessionZMQ()
omc.sendExpression("getVersion()")
omc.sendExpression("cd()")
omc.sendExpression("loadModel(Modelica)")
omc.sendExpression("loadFile(getInstallationDirectoryPath() + \"/share/doc/omc/testmodels/BouncingBall.mo\")")
omc.sendExpression("instantiateModel(BouncingBall)")