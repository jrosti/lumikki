import memcache

class conf:
    def __init__(self):
        self.mc = memcache.Client(['127.0.0.1:11211'], debug=0)

    def getAndSetCurrent(self, inputMap):
        retDict = dict()
        for key in configurationMap: 
            inKeys = inputMap.keys()
            if key in inKeys:
                self.set(key, inputMap[key])
            retDict[key] = self.get(key)
        return retDict

    def get(self, key):
        value = self.mc.get(key)
        if not value: 
            svalue = configurationMap[key]
            if svalue:
                self.mc.set(key,svalue)
            return svalue
        else:
            return value

    def set(self, key, value):
        self.mc.set(key,value)

class staticglobals: 
    ttm = 0
    ae = 1
    cam = 2
    ir = 3

configurationMap = {
    'g_active':[False, False, False, False]
    , 'g_measurementid'     : 'default'
    , 'cam_parentfolder' : 'F:\data'
    , 'cam_packetsize' : '9144'
    , 'cam_xoffset' : '0'
    , 'cam_yoffset' : '0'
    , 'cam_width' : '1024'
    , 'cam_height' : '768'
    , 'cam_ip': '130.233.203.154'
    , 'cam_port' : "6423"
    , 'cam_exposure' : '300'
    , 'cam_rawfps' : '1000'
    , 'ttm_ramprate' : '0.2'
    , 'ttm_rampamplitude' : '2'
    , 'ttm_setpoint' : '1'
    , 'ttm_setpointtime' : '1'
    , 'ttm_ip' : '127.0.0.1'
    , 'ttm_port' : '80'
    , 'ir_framerate' : '30'
    , 'ir_recordtime' : '5.0'
    , 'ir_filename' : 'irpicture'
    , 'ir_ip' : '127.0.0.1'
    , 'ir_port' : '57944'
}