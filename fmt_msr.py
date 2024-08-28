# Credits to Joschuka and M-1 for the Dread plugin, which was referred to for some parts
from inc_noesis import *

# =================================================================
# Plugin options
# =================================================================

# set the path dump, only necessary if you're using the texture scanning.
# For example: r"D:\Metroid Samus Returns\romfs\packs\_extracted"
dumpPath = r"E:\Game Files\MSR\romfs\packs\_extracted"
showHiddenMeshes = False
loadAnimations = True


def registerNoesisTypes():
    handle = noesis.register("Metroid Samus Returns", ".bcmdl")
    noesis.setHandlerTypeCheck(handle, CheckModelType)
    noesis.setHandlerLoadModel(handle, LoadModel)
    handle = noesis.register("Metroid Samus Returns", ".bctex")
    noesis.setHandlerTypeCheck(handle, CheckTextureType)
    noesis.setHandlerLoadRGBA(handle, LoadRGBA)
    return 1

crcTable = [0, 1996959894, 3993919788, 2567524794, 124634137, 1886057615, 3915621685, 2657392035, 249268274, 2044508324, 3772115230, 2547177864, 162941995, 2125561021, 3887607047, 2428444049, 498536548, 1789927666, 4089016648, 2227061214, 450548861, 1843258603, 4107580753, 2211677639, 325883990, 1684777152, 4251122042, 2321926636, 335633487, 1661365465, 4195302755, 2366115317, 997073096, 1281953886, 3579855332, 2724688242, 1006888145, 1258607687, 3524101629, 2768942443, 901097722, 1119000684, 3686517206, 2898065728, 853044451, 1172266101, 3705015759, 2882616665, 651767980, 1373503546, 3369554304, 3218104598, 565507253, 1454621731, 3485111705, 3099436303, 671266974, 1594198024, 3322730930, 2970347812, 795835527, 1483230225, 3244367275, 3060149565, 1994146192, 31158534, 2563907772, 4023717930, 1907459465, 112637215, 2680153253, 3904427059, 2013776290, 251722036, 2517215374, 3775830040, 2137656763, 141376813, 2439277719, 3865271297, 1802195444, 476864866, 2238001368, 4066508878, 1812370925, 453092731, 2181625025, 4111451223, 1706088902, 314042704, 2344532202, 4240017532, 1658658271, 366619977, 2362670323, 4224994405, 1303535960, 984961486, 2747007092, 3569037538, 1256170817, 1037604311, 2765210733, 3554079995, 1131014506, 879679996, 2909243462, 3663771856, 1141124467, 855842277, 2852801631, 3708648649, 1342533948, 654459306, 3188396048, 3373015174, 1466479909, 544179635, 3110523913, 3462522015, 1591671054, 702138776, 2966460450, 3352799412, 1504918807, 783551873, 3082640443, 3233442989, 3988292384, 2596254646, 62317068, 1957810842, 3939845945, 2647816111, 81470997, 1943803523, 3814918930, 2489596804, 225274430, 2053790376, 3826175755, 2466906013, 167816743, 2097651377, 4027552580, 2265490386, 503444072, 1762050814, 4150417245, 2154129355, 426522225, 1852507879, 4275313526, 2312317920, 282753626, 1742555852, 4189708143, 2394877945, 397917763, 1622183637, 3604390888, 2714866558, 953729732, 1340076626, 3518719985, 2797360999, 1068828381, 1219638859, 3624741850, 2936675148, 906185462, 1090812512, 3747672003, 2825379669, 829329135, 1181335161, 3412177804, 3160834842, 628085408, 1382605366, 3423369109, 3138078467, 570562233, 1426400815, 3317316542, 2998733608, 733239954, 1555261956, 3268935591, 3050360625, 752459403, 1541320221, 2607071920, 3965973030, 1969922972, 40735498, 2617837225, 3943577151, 1913087877, 83908371, 2512341634, 3803740692, 2075208622, 213261112, 2463272603, 3855990285, 2094854071, 198958881, 2262029012, 4057260610, 1759359992, 534414190, 2176718541, 4139329115, 1873836001, 414664567, 2282248934, 4279200368, 1711684554, 285281116, 2405801727, 4167216745, 1634467795, 376229701, 2685067896, 3608007406, 1308918612, 956543938, 2808555105, 3495958263, 1231636301, 1047427035, 2932959818, 3654703836, 1088359270, 936918000, 2847714899, 3736837829, 1202900863, 817233897, 3183342108, 3401237130, 1404277552, 615818150, 3134207493, 3453421203, 1423857449, 601450431, 3009837614, 3294710456, 1567103746, 711928724, 3020668471, 3272380065, 1510334235, 755167117]

def hashFunction(str):
    checksum = 0xffffffff
    for c in str:
        checksum = crcTable[(checksum & 0xff) ^ ord(c)] ^ (checksum >> 8)
    return checksum

def ValidateInputDirectory(inVal):
    if not os.path.isdir(inVal):
        return "'" + inVal + "' is not a valid directory."

def CheckModelType(data):
    bs = NoeBitStream(data)
    magic = bs.readBytes(4)
    major_version = bs.readUShort()
    minor_version = bs.readUShort()
    if magic == b"MMDL" and major_version == 1 and minor_version == 39:
        return 1
    return 0

def CheckTextureType(data):
    bs = NoeBitStream(data)
    magic = bs.readBytes(4)
    major_version = bs.readUShort()
    minor_version = bs.readUShort()
    if magic == b"MTXT" and major_version == 1 and minor_version == 4:
        return 1
    return 0

def LoadRGBA(data, texList):
    rapi.processCommands('-texnorepfn')    
    global textureList
    textureList = []
    processRGBA(data)
    for tex in textureList:
        texList.append(tex)
    return 1

def processRGBA(data, texName = None):
    tex = rapi.loadTexByHandler(data[0x80:], ".ctpk")
    if texName is not None:
        tex.name = texName
    else:    
        tex.name = tex.name[:-4] + ".dds"
    if tex.name == "cubemetroids.dds":
        for i in range(len(tex.pixelData)//4):
            tex.pixelData[3 + 4*i] = tex.pixelData[2 + 4*i]
    else:
        #textureData = noesis.deinterleaveBytes(tex.pixelData, 0, 3, 4)
        textureData = rapi.imageDecodeRaw(tex.pixelData, tex.width, tex.height, "r8g8b8a8")
        tex = NoeTexture(tex.name, tex.width, tex.height, textureData, noesis.NOESISTEX_RGBA32)
    textureList.append(tex)    
    return 1

def processSplitRGBA(data, texName = None):
    tex = rapi.loadTexByHandler(data[0x80:], ".ctpk")
    if texName is not None:
        tex.name = texName[:-4]
    else:
        tex.name = tex.name[:-4]

    convertedTextures = []
    textureData = rapi.imageDecodeRaw(tex.pixelData, tex.width, tex.height, "r8g8b8a8")
    for c in range(4):
        channelData = noesis.deinterleaveBytes(textureData, c, 1, 4)
        # Convert to rgb texture
        convertedData = bytearray(3 * len(channelData))
        for i in range(3):
            convertedData[i::3] = channelData[0::1]
        convertedTextureRaw = rapi.imageDecodeRaw(convertedData, tex.width, tex.height, "r8g8b8")
        convertedTexture = NoeTexture(tex.name + "_channel" + 'RGBA'[c] + ".dds", tex.width, tex.height,
                                      convertedTextureRaw, noesis.NOESISTEX_RGBA32)
        textureList.append(convertedTexture)
        convertedTextures.append(convertedTexture.name)

    return convertedTextures


def LoadKFValues(bs, offset, animName, frameCount):
    """Load animation"""
    bs.seek(offset)    
    kfCount = bs.readUShort()
    unk = bs.readUShort()
    assert(unk == 2)
    timings = []
    values = []
    
    if kfCount:    
        for _ in range(kfCount):
            timings.append(int(bs.readFloat()))
            values.append([bs.readFloat(), bs.readFloat(),bs.readFloat()])  
        allValues = []
        for i in range(len(timings)-1):
            t0 = timings[i]
            t1 = timings[i+1]
            v0 = values[i][0]
            v1 = values[i+1][0]
            for t in range(t1-t0):
                alpha = t/(t1-t0)
                allValues.append(v0 * (1 - alpha) + v1 * alpha)
        # for i in range(len(timings)-1):
            # t0 = timings[i]
            # t1 = timings[i+1]
            # v0 = values[i][0]
            # v1 = values[i+1][0]
            # s0 = values[i][2] # out slope for point 0
            # s1 = values[i+1][1] # in slope for point 1
            
            # for t in range(t1-t0):
                # alpha = t/(t1-t0)
                # cubicCoeffs = NoeVec4([v0,v1, s0, s1]) * NoeMat44([[2, -3, 0, 1], [-2, 3, 0, 0], [1, -2, 1, 0], [1, -1, 0, 0]])            
                # allValues.append(NoeVec4([alpha**3, alpha**2, alpha,1]).dot(cubicCoeffs))        
        return [True,allValues]
        
    else:
        assert(not bs.readUInt())        
        return [False,bs.readFloat()]

def LoadTracks(bs, frameCount, framerate, animName):
   
    semanticValues = []    
    checkpoint = bs.tell()
    
    for i in range(9):
        bs.seek(checkpoint + 4 * i)
        value = bs.readUInt()
        if value:
            output = LoadKFValues(bs, value, animName, frameCount)
            if output[0]:
                semanticValues.append(output[1])
            else:
                semanticValues.append([output[1] for _ in range(int(frameCount))])            
        else:
            if i < 6:
                semanticValues.append([value for _ in range(int(frameCount))])
            else:
                semanticValues.append([1.0 for _ in range(int(frameCount))])
    
    rotNoeKeyFramedValues = []
    posNoeKeyFramedValues = []
    scaleNoeKeyFramedValues = []
    
    #position
    for t,(x,y,z) in enumerate(zip(semanticValues[0],semanticValues[1],semanticValues[2])):
        posNoeKeyFramedValues.append(NoeKeyFramedValue(t / framerate, NoeVec3([x,y,z])))
    #rotation
    for t,(x,y,z) in enumerate(zip(semanticValues[3],semanticValues[4],semanticValues[5])):
        rotNoeKeyFramedValues.append(NoeKeyFramedValue(t / framerate, NoeAngles([x,y,z]).toDegrees().toMat43_XYZ().toQuat()))
    #scale
    for t,(x,y,z) in enumerate(zip(semanticValues[6],semanticValues[7],semanticValues[8])):
        scaleNoeKeyFramedValues.append(NoeKeyFramedValue(t / framerate, NoeVec3([x,y,z])))    
    
    return [posNoeKeyFramedValues, rotNoeKeyFramedValues, scaleNoeKeyFramedValues]

def LoadAnim(data, joints, jointHashToIDMap, animName):
    bs = NoeBitStream(data)
    
    framerate = 60
    bs.readUInt() #fourCC
    bs.readUInt() #version stuff
    bs.readUInt() #reserved
    frameCount = bs.readFloat()
    entryCount = bs.readUInt()
    keyframedJointList = []
    
    checkpoint = bs.tell()
    for i in range(entryCount):
        bs.seek(checkpoint + 0x28 * i)
        hash = bs.readUInt()
        # print(hex(hash))
        if hash not in jointHashToIDMap:
            continue
        jointID = jointHashToIDMap[hash]
        posNoeKeyFramedValues, rotNoeKeyFramedValues, scaleNoeKeyFramedValues = LoadTracks(bs, frameCount, framerate, animName)
        
        animatedJoint = NoeKeyFramedBone(jointID)
        animatedJoint.setRotation(rotNoeKeyFramedValues, noesis.NOEKF_ROTATION_QUATERNION_4,noesis.NOEKF_INTERPOLATE_LINEAR)
        animatedJoint.setTranslation(posNoeKeyFramedValues, noesis.NOEKF_TRANSLATION_VECTOR_3,noesis.NOEKF_INTERPOLATE_LINEAR)
        animatedJoint.setScale(scaleNoeKeyFramedValues, noesis.NOEKF_SCALE_VECTOR_3,noesis.NOEKF_INTERPOLATE_LINEAR)
        keyframedJointList.append(animatedJoint)
    # print(len(keyframedJointList))
    anim = None
    if keyframedJointList:
        anim = NoeKeyFramedAnim(animName, joints, keyframedJointList, framerate)
    return anim

def readOffsetString(bs, offset):
    bs.seek(offset)
    return bs.readString()

def loadTextureFromString(texName, alreadyLoaded, missingTexFiles, meshName, isSplit=False):
    parse_function = processSplitRGBA if isSplit else processRGBA
    if texName not in alreadyLoaded:
        alreadyLoaded[texName] = True
        fulltexPath = os.path.dirname(rapi.getInputName()) + os.sep + "textures" + os.sep + texName + ".bctex"
        fallbackPath = os.path.join(dumpPath, "maps", "textures", texName + ".bctex")
        if rapi.checkFileExists(fulltexPath):
            return parse_function(rapi.loadIntoByteArray(fulltexPath), texName + ".dds")
        elif rapi.checkFileExists(fallbackPath):
            return parse_function(rapi.loadIntoByteArray(fallbackPath), texName + ".dds")
        else:
            missingTexFiles.append([texName, meshName])
            return [] if isSplit else 0
    elif isSplit:
        return [texName + "_channel" + 'RGBA'[c] + ".dds" for c in range(4)]

def readMaterial(bs, offset, alreadyLoaded, missingTexFiles, meshName) -> NoeMaterial:
    bs.seek(offset)
    name_offset = bs.readUInt()
    shader_offset = bs.readUInt()
    _ = bs.readUInt()  # always 0, possibly sentinel
    unk_count = bs.readUInt()
    _ = bs.read('f' * 18)  # Skip past unknown float params
    emissiveColor = NoeVec4(bs.read('f' * 4))
    _ = bs.read('f' * 8)  # Skip past unknown float params
    _ = bs.read('i' * 3) # unk_count)  # Skip past unknown array of ints
    texOffsets = [bs.readUInt() for _ in range(6)]
    textures = [readOffsetString(bs, o) for o in texOffsets]

    # TODO: Hacky texture code, should try to figure out individual shaders
    material = NoeMaterial(readOffsetString(bs, name_offset), "")
    if len(textures) == 0 or len(textures[0]) == 0:
        return material
    texName = textures[0]

    material.setTexture(texName + ".dds")
    loadTextureFromString(texName, alreadyLoaded, missingTexFiles, meshName)

    if len(textures) > 2 and len(textures[2]) != 0 and textures[2].endswith('_a'):
        split = loadTextureFromString(textures[2], alreadyLoaded, missingTexFiles, meshName, True)
        if len(split) == 4:
            r, g, b, a = split
            material.setOcclTexture(r)
            emissivePass = NoeMaterial(material.name + "_emissive", g)
            emissivePass.setBlendMode("GL_ONE", "GL_ONE")
            emissivePass.setDiffuseColor(emissiveColor)
            emissivePass.flags |= noesis.NMATFLAG_BASICBLEND
            material.setNextPass(emissivePass)
    return material


def LoadModel(data, mdlList):
    
    ctx = rapi.rpgCreateContext()
    bs = NoeBitStream(data)
    global textureList
    textureList = []    
    
    bs.seek(8)  # We've already verified the magic and version numbers, so skip past them
    offsets = bs.read('10i') 
    
    bs.seek(offsets[7])
    bs.seek(bs.readUInt())
    boneOffsets = []
    while(True):
        boneOffsets.append(bs.readUInt())
        nextOffs = bs.readUInt()
        if not nextOffs:
            break
            
    boneList = []
    jointHashToIDMap = {}
    for i, boneOffset in enumerate(boneOffsets):
        bs.seek(boneOffset)
        boneTransformOffset, boneNameOffset, boneParentNameOffset = bs.read('3i')
        bs.seek(boneNameOffset)
        boneName = bs.readString()
        bs.seek(boneTransformOffset)
        translation = NoeVec3(bs.read('3f'))
        boneMatrix = NoeAngles(bs.read('3f')).toDegrees().toMat43_XYZ()
        boneMatrix[3] = translation
        
        if boneParentNameOffset:
            bs.seek(boneParentNameOffset)
            pName = bs.readString()
            boneList.append(NoeBone(i, boneName, boneMatrix, pName, -1))
        else:
            boneList.append(NoeBone(i, boneName, boneMatrix, None, -1))
        jointHashToIDMap[hashFunction(boneName)] = i
    boneList = rapi.multiplyBones(boneList)

    animList = []
    animPaths = []
    if loadAnimations:
        animDir = noesis.userPrompt(noesis.NOEUSERVAL_FOLDERPATH, "Open Folder", "Select the folder to get the animations from", noesis.getSelectedDirectory(), ValidateInputDirectory)
        if animDir is not None:
            for root, dirs, files in os.walk(animDir):
                for fileName in files:
                    lowerName = fileName.lower()
                    if lowerName.endswith(".bcskla"):
                        fullPath = os.path.join(root, fileName)
                        animPaths.append(fullPath)
            for animPath in animPaths:
                with open(animPath, "rb") as animStream:
                    animName = "".join(os.path.basename(animPath).split(".")[:-1]) # Filename without extension
                    anim = LoadAnim(animStream.read(), boneList, jointHashToIDMap, animName)
                    if anim is not None:
                        animList.append(anim)

    bs.seek(offsets[4])
    meshInfoOffsets = []
    while(True):
        meshInfoOffsets.append(bs.readUInt())
        nextOffs = bs.readUInt()
        if not nextOffs:
            break
            
    meshesInfo = []
    for meshInfoOffs in meshInfoOffsets:
        bs.seek(meshInfoOffs)
        meshesInfo.append(bs.read('3i'))
        # print(bs.tell())
        
    meshNames = []
    meshVis = []
    for info in meshesInfo:
        bs.seek(info[2])
        nameOffs = bs.readUInt()
        meshVis.append(True if bs.readUByte() else False)
        bs.seek(nameOffs)        
        meshNames.append(bs.readString())
        
    materials = []
    alreadyLoaded = {}
    missingTexFiles = []
    for meshIdx, info in enumerate(meshesInfo):
        # if not meshVis[meshIdx] and not showHiddenMeshes:
        #     continue
        material = readMaterial(bs, info[1], alreadyLoaded, missingTexFiles, meshNames[meshIdx])
        materials.append(material)
    
    if missingTexFiles:
        outFilePath = noesis.getPluginsPath() + "python" + os.sep + "SR" + os.sep + os.path.basename(rapi.getInputName()) + ".txt"
        if not os.path.exists(noesis.getPluginsPath() + "python" + os.sep + "SR"):
            os.makedirs(noesis.getPluginsPath() + "python" + os.sep + "SR")
        with open(outFilePath, "w") as f:
            for mt in missingTexFiles:
                f.write(mt[1] + " is missing the " + mt[0] + " texture\n")
    
    nonRigidMeshesInfo = []
    bAtLeastOneRigid = False
    for meshIdx, info in enumerate(meshesInfo):
        if not meshVis[meshIdx] and not showHiddenMeshes:
            continue
        
        bs.seek(info[0] + 0x4c)
        vBufferInfoOffset, submeshCount, submeshInfoOffsetPtr = bs.readUInt(), bs.readUInt(), bs.readUInt()
        transform = NoeVec3.fromBytes(bs.readBytes(12))
        
        bs.seek(submeshInfoOffsetPtr)
        submeshInfoOffsets = []
        for _ in range(submeshCount):
            submeshInfoOffsets.append(bs.readUInt())
            bs.readUInt()        

        bs.seek(vBufferInfoOffset + 8)
        vBufferSize = bs.readUInt()
        vCount = bs.readUInt()
        vBufferOffset = bs.readUInt()        
        attributeCount = bs.readUInt()  
        attributes = []
        
        for _ in range(attributeCount):
            attributes.append(bs.read('2i2H1i'))
        
        bs.seek(vBufferOffset)
        vBuffer = None
        vBuffer = bs.readBytes(vBufferSize)
        posOffset, normalOffset, jIdxValues, jIdxCount = None, None, None, None
        hasNormals = False
        rapi.rpgClearBufferBinds() 
        for attribute in attributes:            
            type, offs, count = attribute[0], attribute[1], attribute[3]
            if type == 0:
                rapi.rpgBindPositionBufferOfs(vBuffer, noesis.RPGEODATA_FLOAT, count * 4, offs) 
                posOffset = offs             
            elif type == 1:
                rapi.rpgBindNormalBufferOfs(vBuffer, noesis.RPGEODATA_FLOAT, count * 4, offs)
                normalOffset = offs
            elif type == 2:
                rapi.rpgBindUV1BufferOfs(vBuffer, noesis.RPGEODATA_FLOAT, count * 4, offs)
            elif type == 3:
                rapi.rpgBindUV2BufferOfs(vBuffer, noesis.RPGEODATA_FLOAT, count * 4, offs)
            elif type == 4:
                rapi.rpgBindUVXBufferOfs(vBuffer, noesis.RPGEODATA_FLOAT, count * 4, 2, 2, offs)
            elif type == 6:
                boneBs = NoeBitStream(vBuffer)
                boneBs.seek(offs)
                jIdxCount = count
                jIdxValues = boneBs.read(str(vCount * count) +'f')
                jIdxValues = [int(value) for value in jIdxValues]
                jointIndexBuffer = struct.pack("<" + 'H'*len(jIdxValues), *jIdxValues)
                rapi.rpgBindBoneIndexBuffer(jointIndexBuffer, noesis.RPGEODATA_USHORT, count * 2, count)
            elif type == 7:
                rapi.rpgBindBoneWeightBufferOfs(vBuffer, noesis.RPGEODATA_FLOAT, count * 4, offs, count)

      
        skinModeCached = None
        for submeshInfoOffs in submeshInfoOffsets:
            bs.seek(submeshInfoOffs)
            idxBufferInfoOffset = bs.readUInt()
            skinMode = bs.readUInt()
            
            if skinModeCached is not None:
                if skinMode != skinModeCached:
                    print("different skin modes for same mesh")
            else:
                skinModeCached = skinMode
            if skinMode != 1:     
                nonRigidMeshesInfo.append([vBufferOffset, vBufferSize, attributes, submeshInfoOffsets, transform, meshIdx, vCount, skinMode])       
            else:
                boneTableCount = bs.readUInt()
                boneTableOffset = bs.readUInt()
                
                bs.seek(boneTableOffset)
                boneMap = [bs.readUInt() for _ in range(boneTableCount)]
                rapi.rpgSetBoneMap(boneMap)
                
                bs.seek(idxBufferInfoOffset + 0xC)           
                idxCount = bs.readUInt()
                idxOffset = bs.readUInt()
                
                bs.seek(idxOffset)
                idxBuffer = bs.readBytes(idxCount*2)

                mat = NoeMat43()
                mat[3] = transform
                rapi.rpgSetTransform(mat)

                rapi.rpgSetName(meshNames[meshIdx])
                bAtLeastOneRigid = True
                
                rapi.rpgSetMaterial(materials[meshIdx].name)
                
                rapi.rpgCommitTriangles(idxBuffer,noesis.RPGEODATA_USHORT , idxCount,noesis.RPGEO_TRIANGLE, 1)
    if bAtLeastOneRigid:
        rapi.rpgSkinPreconstructedVertsToBones(boneList)
    try:
        mdl = rapi.rpgConstructModel()
    except:
        mdl = NoeModel()
        
    #second batch of models
    for m in nonRigidMeshesInfo:
        vBufferOffset, vBufferSize, attributes, submeshInfoOffsets, transform, nameIdx, vCount, skinMode = m
        
        bs.seek(vBufferOffset)
        vBuffer = None
        vBuffer = bs.readBytes(vBufferSize)
        rapi.rpgClearBufferBinds()
        for attribute in attributes:            
            type, offs, count = attribute[0], attribute[1], attribute[3]
            if type == 0:
                rapi.rpgBindPositionBufferOfs(vBuffer, noesis.RPGEODATA_FLOAT, count * 4, offs) 
            elif type == 1:
                rapi.rpgBindNormalBufferOfs(vBuffer, noesis.RPGEODATA_FLOAT, count * 4, offs)
            elif type == 2:
                rapi.rpgBindUV1BufferOfs(vBuffer, noesis.RPGEODATA_FLOAT, count * 4, offs)
            elif type == 3:
                rapi.rpgBindUV2BufferOfs(vBuffer, noesis.RPGEODATA_FLOAT, count * 4, offs)
            elif type == 4:
                rapi.rpgBindUVXBufferOfs(vBuffer, noesis.RPGEODATA_FLOAT, count * 4, 2, 2, offs)
            elif type == 6:
                boneBs = NoeBitStream(vBuffer)
                boneBs.seek(offs)
                jIdxValues = boneBs.read(str(vCount * count) +'f')
                jIdxValues = [int(value) for value in jIdxValues]
                jointIndexBuffer = struct.pack("<" + 'H'*len(jIdxValues), *jIdxValues)
                rapi.rpgBindBoneIndexBuffer(jointIndexBuffer, noesis.RPGEODATA_USHORT, count * 2, count)
            elif type == 7:
                rapi.rpgBindBoneWeightBufferOfs(vBuffer, noesis.RPGEODATA_FLOAT, count * 4, offs, count)
        
        for submeshInfoOffs in submeshInfoOffsets:
            bs.seek(submeshInfoOffs)
            idxBufferInfoOffset = bs.readUInt()
            skinMode = bs.readUInt()        
            boneTableCount = bs.readUInt()
            boneTableOffset = bs.readUInt()
                
            bs.seek(boneTableOffset)
            boneMap = [bs.readUInt() for _ in range(boneTableCount)]
            rapi.rpgSetBoneMap(boneMap)
            
            bs.seek(idxBufferInfoOffset + 0xC)           
            idxCount = bs.readUInt()
            idxOffset = bs.readUInt()
            
            bs.seek(idxOffset)
            idxBuffer = bs.readBytes(idxCount*2)
            
            if skinMode == 0:
                jIdxValues = [0 for i in range(vCount)]
                jointIndexBuffer = struct.pack("<" + 'H'*len(jIdxValues), *jIdxValues)
                rapi.rpgBindBoneIndexBuffer(jointIndexBuffer, noesis.RPGEODATA_USHORT, 2, 1)

            mat = NoeMat43()
            mat[3] = transform
            if not skinMode:
                mat *= boneList[boneMap[0]].getMatrix()
            rapi.rpgSetTransform(mat)

            rapi.rpgSetName(meshNames[nameIdx])

            rapi.rpgSetMaterial(materials[nameIdx].name)
            
            rapi.rpgCommitTriangles(idxBuffer,noesis.RPGEODATA_USHORT , idxCount,noesis.RPGEO_TRIANGLE, 1)
    try:
        mdl = rapi.rpgConstructModel()
    except:
        mdl = NoeModel()
    mdl.setModelMaterials(NoeModelMaterials(textureList, materials))
    mdl.setBones(boneList)
    mdl.setAnims(animList)
    mdlList.append(mdl)
    
    return 1
    
    
