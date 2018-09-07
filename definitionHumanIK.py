import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm

j_list = mc.ls(type='joint')

# set default angle
for i in range(len(j_list)):
    mc.setAttr('%s.rotateX' % (j_list[i]), 0)
    mc.setAttr('%s.rotateY' % (j_list[i]), 0)
    mc.setAttr('%s.rotateZ' % (j_list[i]), 0)

mc.setAttr('Hips.rotateX', -90)

# definition HumanIK
mel.eval('hikCreateDefinition;hikOnSwitchContextualTabs;')

for i in range(len(j_list)):
    nodeId = pm.other.hikGetNodeIdFromName(j_list[i])
    if nodeId > -1:
        pm.mel.setCharacterObject(j_list[i], 'Character1', nodeId, 0)

# character rename
mel.eval('hikRenameDefinition;')