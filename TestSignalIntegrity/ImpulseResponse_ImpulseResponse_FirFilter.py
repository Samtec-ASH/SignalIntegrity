class ImpulseResponse(Waveform):
...
    def FirFilter(self):
        td=self.TimeDescriptor()
        return FirFilter(FilterDescriptor(1,-td.H*td.Fs,td.K-1),self.Values())