#!/usr/bin/env python

from lib.lumilib import *
from lib import cam
from lib import ttm
from lib import ir
from lib import ae
from lib.config import conf
from lib.config import staticglobals as mg

try: 
    ## send to all active devices
    jsonMessage = get_json()
    commandId = jsonMessage['id']
    c = conf()
    active = c.get('g_active')
    
    if active[mg.cam]:  cam.stop()
    if active[mg.ttm]:
        ttm.connectAndStop()
    if active[mg.ir]:   ir.connectAndStopRecording()
    if active[mg.ae]:   ae.stop()
    
    put_json({'st':0, 'id':commandId})
    
except Exception as e:
    put_json({'id':commandId, 'st':1, 'msg':'Stop failed [' + str(e) + ']'})
    raise
