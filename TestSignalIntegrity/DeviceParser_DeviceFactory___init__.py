class DeviceFactory(object):
    def __init__(self):
        self.deviceList=[
        ParserDevice('file',None,True,{'':None},True,
            "SParameterFile(arg[''],50.).Resample(f)"),
        ParserDevice('c',1,True,{'':None,'df':0.,'esr':0.,'z0':50.},True,
            "TerminationC(f,float(arg['']),float(arg['z0']),\
            float(arg['df']),float(arg['esr']))"),
        ParserDevice('c',2,True,{'':None,'df':0.,'esr':0.,'z0':50.},True,
            "SeriesC(f,float(arg['']),float(arg['z0']),float(arg['df']),\
            float(arg['esr']))"),
        ParserDevice('l',1,True,{'':None},True,"TerminationL(f,float(arg['']))"),
        ParserDevice('l',2,True,{'':None},True,"SeriesL(f,float(arg['']))"),
        ParserDevice('r',1,True,{'':None},False,"TerminationZ(float(arg['']))"),
        ParserDevice('r',2,True,{'':None},False,"SeriesZ(float(arg['']))"),
        ParserDevice('shunt','2-4',True,{'':None},False,
            "ShuntZ(ports,float(arg['']))"),
        ParserDevice('m',4,True,{'':None},True,"Mutual(f,float(arg['']))"),
        ParserDevice('ground',1,False,{},False,"Ground()"),
        ParserDevice('open',1,False,{},False,"Open()"),
        ParserDevice('thru',2,False,{},False,"Thru()"),
        ParserDevice('directionalcoupler','3-4',False,{},False,
            "DirectionalCoupler(ports)"),
        ParserDevice('termination',None,False,{},False,
            "zeros(shape=(ports,ports)).tolist()"),
        ParserDevice('tee',None,False,{},False,"Tee(ports)"),
        ParserDevice('mixedmode',4,True,{'':'power'},False,
            "(MixedModeConverterVoltage() if arg[''] == 'voltage'\
            else MixedModeConverter())"),
        ParserDevice('idealtransformer',4,True,{'':1.},False,
            "IdealTransformer(float(arg['']))"),
        ParserDevice('voltagecontrolledvoltagesource',4,True,{'':None},False,
            "VoltageControlledVoltageSource(float(arg['']))"),
        ParserDevice('currentcontrolledcurrentsource',4,True,{'':None},False,
            "CurrentControlledCurrentSource(float(arg['']))"),
        ParserDevice('currentcontrolledvoltagesource',4,True,{'':None},False,
            "CurrentControlledVoltageSource(float(arg['']))"),
        ParserDevice('voltagecontrolledcurrentsource',4,True,{'':None},False,
            "VoltageControlledCurrentSource(float(arg['']))"),
        ParserDevice('voltageamplifier','2-4',False,{'gain':None,'zo':0,'zi':1e8,
            'z0':50.},False,"VoltageAmplifier(ports,float(arg['gain']),\
            float(arg['zi']),float(arg['zo']))"),
        ParserDevice('currentamplifier','2-4',False,{'gain':None,'zo':1e8,'zi':0,
            'z0':50.},False,"CurrentAmplifier(ports,float(arg['gain']),\
            float(arg['zi']),float(arg['zo']))"),
        ParserDevice('transresistanceamplifier','2-4',False,{'gain':None,'zo':0.,
            'zi':0.,'z0':50.},False,"TransresistanceAmplifier(ports,\
            float(arg['gain']),float(arg['zi']),float(arg['zo']))"),
        ParserDevice('transconductanceamplifier','2-4',False,{'gain':None,'zo':1e8,
            'zi':1e8,'z0':50.},False,"TransconductanceAmplifier(ports,\
            float(arg['gain']),float(arg['zi']),float(arg['zo']))")]
        ParserDevice('opamp',3,False,{'zi':1e8,'zd':1e8,'zo':0.,'gain':1e8,'z0':50.},
            False,"OperationalAmplifier(float(arg['zi']),float(arg['zd']),\
            float(arg['zo']),float(arg['gain']),float(arg['z0']))"),
...
