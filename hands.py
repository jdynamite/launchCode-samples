# InsomniacScriptTestHands_JuanLugo
# juandiego.lugo@gmail.com

# Select the hand control
# ???
# PROFIT!

import maya.cmds as cmds

hand_ctrl = cmds.ls(sl=True)[0]
hand_joint = ''

# find hand joint
try:
    for node in cmds.listConnections(hand_ctrl):
        while (len(hand_joint) == 0):
            if (cmds.nodeType(node) == 'joint'):
                hand_joint = node
                print('A hand was found! It\'s called %s' % hand_joint)
                print('Let\'s proceed with finding us some fingers')
except TypeError:
    cmds.warning('Sorry, couldn\'t find anything connected to this object')

if (hand_joint):
    
    hand_roo = ''
    thumb = ''
    side = ''

    # y orient is up or down? negative or positive?
    hand_yUp = True if cmds.getAttr("%s.jointOrientY" % hand_joint) >= 0 else False 

    if (cmds.nodeType(hand_ctrl) == 'joint'): 
        hand_roo = cmds.joint(hand_ctrl, q=True, roo=True)
    else:
        hand_roo = cmds.joint(hand_joint, q=True, roo=True)
        
    # create a list with immediate children and all descendants
    im_children = cmds.listRelatives(hand_joint, c=True, type='joint')
    ad_children = cmds.listRelatives(hand_joint, ad=True, type='joint')
    
    # create a dictionary to make joint : length pairs and assume for now the first immediate child ihas the shortest chain
    length_dict = dict()
    shortest = im_children[0]
    
    # determine number of fingers
    num_of_fingers = len(im_children)
    
    # freeze transforms on all joints so we can orient them later
    for child in ad_children:
        cmds.makeIdentity(child, apply=True, t=1, r=1, s=1)
    
    # orient joint, calculate length of the chain, and compare to others
    # shortest chain should yield the thumb
    for child in im_children:
        cmds.joint(child, e=True, oj="xyz", sao="yup", roo=hand_roo, ch=True, zso=True)
        c_length = 0.0
        for chain_child in cmds.listRelatives(child, ad=True, type='joint'):
            c_length += cmds.getAttr( chain_child+'.tx' )
        length_dict[child] = c_length
        if (c_length < length_dict[shortest]): shortest = child

    # now we have the shortest chain (thumb), we can start finding other fingers
    # I will use two vectors, v1 will be the shortest chain (thumb), and v2 every other finger
    # then compare the angle between the two for each of them
    
    v1 = cmds.getAttr(shortest+'.translate')[0]
    angle_dict = dict()
    
    for child in im_children:
        if child != shortest:
            v2 = cmds.getAttr(child+'.translate')[0]
            ab = cmds.angleBetween(v1=v1,v2=v2)[-1]
            angle_dict[child] = ab
    
    # sort angles in a list
    
    angle_list = angle_dict.values()
    angle_list.sort()
    
    # match angles to names based on their distance from the thumb
    
    if (hand_ctrl.lower()).find('right') >= 0:
        side = 'right'
    else:
        side = 'left'

    for child, angle in angle_dict.iteritems():
        chain_children = cmds.listRelatives(child, ad=True, type='joint')
        if num_of_fingers == 4:
            if angle_dict[child] == angle_list[0]:
                # rename chain to index
                if (len(chain_children) > 3): 
                    cmds.rename(child, "%s_index_metatarsal" % side)
                else:
                    cmds.rename(child, "%s_index_0" % side)
                for i,chain_child in enumerate(reversed(chain_children)):
                    ind = i+1
                    cmds.rename(chain_child, "%s_index_%s" % (side, ind))
            elif angle_dict[child] == angle_list[1]:
                # rename chain to middle
                if (len(chain_children) > 3): 
                    cmds.rename(child, "%s_middle_metatarsal" % side)
                else:
                    cmds.rename(child, "%s_middle_0" % side)
                for i,chain_child in enumerate(reversed(chain_children)):
                    ind = i+1
                    cmds.rename(chain_child, "%s_middle_%s" % (side, ind))
            elif angle_dict[child] == angle_list[2]:
                # rename chain to pinky
                if (len(chain_children) > 3): 
                    cmds.rename(child, "%s_pinky_metatarsal" % side)
                else:
                    cmds.rename(child, "%s_pinky_0" % side)
                for i,chain_child in enumerate(reversed(chain_children)):
                    ind = i+1
                    cmds.rename(chain_child, "%s_pinky_%s" % (side, ind))
        if num_of_fingers == 5:
            if angle_dict[child] == angle_list[0]:
                # rename chain to index
                if (len(chain_children) > 3): 
                    cmds.rename(child, "%s_index_metatarsal" % side)
                else:
                    cmds.rename(child, "%s_index_0" % side)
                for i,chain_child in enumerate(reversed(chain_children)):
                    ind = i+1
                    cmds.rename(chain_child, "%s_index_%s" % (side, ind))
            elif angle_dict[child] == angle_list[1]:
                # rename chain to middle
                if (len(chain_children) > 3): 
                    cmds.rename(child, "%s_middle_metatarsal" % side)
                else:
                    cmds.rename(child, "%s_middle_0" % side)
                for i,chain_child in enumerate(reversed(chain_children)):
                    ind = i+1
                    cmds.rename(chain_child, "%s_middle_%s" % (side, ind))
            elif angle_dict[child] == angle_list[2]:
                # rename chain to ring
                if (len(chain_children) > 3): 
                    cmds.rename(child, "%s_ring_metatarsal" % side)
                else:
                    cmds.rename(child, "%s_ring_0" % side)
                for i,chain_child in enumerate(reversed(chain_children)):
                    ind = i+1
                    cmds.rename(chain_child, "%s_ring_%s" % (side, ind))
            elif angle_dict[child] == angle_list[3]:
                # rename chain to pinky
                if (len(chain_children) > 3): 
                    cmds.rename(child, "%s_pinky_metatarsal" % side)
                else:
                    cmds.rename(child, "%s_pinky_0" % side)
                for i,chain_child in enumerate(reversed(chain_children)):
                    ind = i+1
                    cmds.rename(chain_child, "%s_pinky_%s" % (side, ind))

    # rename thumb
    thumb_chain_children = cmds.listRelatives(shortest, ad=True, type='joint')
    if (len(thumb_chain_children) > 3):
        thumb = cmds.rename(shortest, "%s_thumb_metatarsal" % side)
    else:
        thumb = cmds.rename(shortest, "%s_thumb_0" % side)
    for i, chain_child in enumerate(reversed(thumb_chain_children)):
        ind = i+1
        cmds.rename(chain_child, "%s_thumb_%s" % (side, ind))

    # re-orient thumb to bend on the same axis as fingers
    thumb_yUp = "yup" if hand_yUp else "ydown"
    cmds.joint(thumb, e=True, oj="xzy", sao=thumb_yUp, ch=True, zso=True)
   
    # redefine immediate children since we renamed everything
    im_children = cmds.listRelatives(hand_joint, c=True, type='joint')

    # add attributes to the hand control and match them with fingers 
    # for every joint below wrist:

    for finger in im_children:

        finger_children = cmds.listRelatives(finger, ad=True, type='joint')

        # get prefix of finger
        prefix = finger.split('_')[1]

        # add main displayable attr in hand control
        cmds.addAttr(hand_ctrl, ln=prefix, at="enum", en="attributes:")
        cmds.setAttr(hand_ctrl + '.' + prefix, e=True, channelBox=True)

        # if there are metatarsals, add a cup attribute and connect it
        attr_stretch = ''
        attr_stretch = "%sStretch" % prefix
        cmds.addAttr(hand_ctrl, ln=attr_stretch, at='double', k=True, min=1)

        if (len(finger_children) > 3): 
            attr = "%sCup" % prefix
            cmds.addAttr(hand_ctrl, ln=attr, at='double', k=True)
            cmds.connectAttr("%s.%s" % (hand_ctrl, attr), "%s.rx" % finger, f=True)

        else:
            attr = "%sBase" % prefix
            cmds.addAttr(hand_ctrl, ln=attr, at='double', k=True)
            cmds.connectAttr("%s.%s" % (hand_ctrl, attr), "%s.rz" % finger, f=True)
            attr_spread = "%sSpread" % prefix
            cmds.addAttr(hand_ctrl, ln=attr_spread, at='double', k=True)
            cmds.connectAttr("%s.%s" % (hand_ctrl, attr_spread), "%s.ry" % finger, f=True)
            attr_twist = "%sTwist" % prefix
            cmds.addAttr(hand_ctrl, ln=attr_twist, at='double', k=True)
            cmds.connectAttr("%s.%s" % (hand_ctrl, attr_twist), "%s.rx" % finger, f=True)
            cmds.connectAttr("%s.%s" % (hand_ctrl, attr_stretch), "%s.sx" % finger, f=True)

        for i,fingers in enumerate(reversed(finger_children)):
            if (len(finger_children) > 3):
                if i == 0:
                    attr = "%sBase" % prefix
                    cmds.addAttr(hand_ctrl, ln=attr, at='double', k=True)
                    cmds.connectAttr("%s.%s" % (hand_ctrl, attr), "%s.rz" % fingers, f=True)
                    attr_spread = "%sSpread" % prefix
                    cmds.addAttr(hand_ctrl, ln=attr_spread, at='double', k=True)
                    cmds.connectAttr("%s.%s" % (hand_ctrl, attr_spread), "%s.ry" % fingers, f=True)
                    attr_twist = "%sTwist" % prefix
                    cmds.addAttr(hand_ctrl, ln=attr_twist, at='double', k=True)
                    cmds.connectAttr("%s.%s" % (hand_ctrl, attr_twist), "%s.rx" % fingers, f=True)
                    cmds.connectAttr("%s.%s" % (hand_ctrl, attr_stretch), "%s.sx" % fingers, f=True)

                elif i == 1:
                    attr = "%sMid" % prefix
                    cmds.addAttr(hand_ctrl, ln=attr, at='double', k=True)
                    cmds.connectAttr("%s.%s" % (hand_ctrl, attr), "%s.rz" % fingers, f=True) 
                    cmds.connectAttr("%s.%s" % (hand_ctrl, attr_stretch), "%s.sx" % fingers, f=True)

                elif i == 2:
                    attr = "%sTip" % prefix
                    cmds.addAttr(hand_ctrl, ln=attr, at='double', k=True)
                    cmds.connectAttr("%s.%s" % (hand_ctrl, attr), "%s.rz" % fingers, f=True)
                    cmds.connectAttr("%s.%s" % (hand_ctrl, attr_stretch), "%s.sx" % fingers, f=True)

            else:
                if i == 0:
                    attr = "%sMid" % prefix
                    cmds.addAttr(hand_ctrl, ln=attr, at='double', k=True)
                    cmds.connectAttr("%s.%s" % (hand_ctrl, attr), "%s.rz" % fingers, f=True) 
                    cmds.connectAttr("%s.%s" % (hand_ctrl, attr_stretch), "%s.sx" % fingers, f=True)
                elif i == 1:
                    attr = "%sTip" % prefix
                    cmds.addAttr(hand_ctrl, ln=attr, at='double', k=True)
                    cmds.connectAttr("%s.%s" % (hand_ctrl, attr), "%s.rz" % fingers, f=True)
                    cmds.connectAttr("%s.%s" % (hand_ctrl, attr_stretch), "%s.sx" % fingers, f=True)

else:
    cmds.warning('Sorry, coudln\'t find a hand joint from the selected object')