from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class EnergyMonitor(ArduinoObject):

    def __init__(self, _iPin, CT_Ratio, Burden_Resistance, _SupplyVoltage=0, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new', _iPin, CT_Ratio, Burden_Resistance, _SupplyVoltage)

    @returns(float)
    @arduinoobjectmethod
    def readCurrent(self, numberSamples):
        pass

