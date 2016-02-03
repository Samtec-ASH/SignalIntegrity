class WaveformTrimmer(FilterDescriptor):
    def __init__(self,TrimLeft,TrimRight):
        FilterDescriptor.__init__(self,1,TrimRight,TrimLeft+TrimRight)
    def TrimWaveform(self,wf):
        return Waveform(wf.TimeDescriptor()*self,
            [wf[k+self.TrimLeft()]
            for k in range(wf.TimeDescriptor().N-self.TrimTotal())])