from DataCompiler import Processor
import PlotAssist, EZColors
import numpy as np 

FlightTest = Processor('ElevatorTest').getCompiled()


#make a plot of time vs pressure
Time = np.array(FlightTest['Time'])
Pressure = np.array(FlightTest['Pressure'])

HPlot = PlotAssist.HigsPlot()
Clr = EZColors.CustomColors(colorLabel = 'red')
HPlot.AxLabels(X = "Time (s)", Y = "Pressure (Pa)")
#HPlot.SetTicks('Y',0.0,1,0.2)
HPlot.SetLim(Left = 0, Right = 250, Top = 100500, Bottom = 100200)
#HPlot.SetTicks('Y',1,11,1)
HPlot.Plot((Time/1000, Pressure), Color = Clr)
HPlot.Finalize()
HPlot.Show()