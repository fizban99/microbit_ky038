micropython library to calibrate and use a sound sensor KY038
##############################################################

This library helps calibrating a sound sensor KY038 with the micro:bit. It also provides a clap counter functionality. It assumes the Digital output of the sound sensor is connected to pin0 of the micro:bit.


.. contents::

.. section-numbering::


Main features
=============

* Helps calibrate the sound sensor showing an arrow on the micro:bit indicating the direction to turn the potentiometer
* Has a clap counter included

Library usage
=============


calibrate()
+++++++++++


Inititalizes the calibration routine. The micro:bit will display an arrow indicating the direction that you should be turning the potentiometer with a screwdriver.

.. code-block:: python

   from ky038 import KY038 
   
   KY038.calibrate()


count_claps()
+++++++++++++


Count the number of claps or any consecutive sudden sound.

.. code-block:: python

   from ky038 import KY038 
   
   KY038.calibrate()
   while True:
       print(KY038.count_claps())
   