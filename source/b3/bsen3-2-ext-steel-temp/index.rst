Eurocode 3 Heat Transfer to External Steelwork
**********************************************

.. warning::
    Work in progress

Calculation documented herein follows annex B in BS EN 1993-1-2:2005 "Eurocode 3: Design of steel structures —
Part 1-2: General rules — Structural fire design". This method allows the determination of the average temperature of
an external steel member.

Units, symbols and abbreviations are consistent with BS EN 1991-1-3 unless explicitly stated. Reference texts in
*italic* refers to BS EN 1993-1-2:2005 unless explicitly stated.

.. important::
    1. In this method, the fire compartment is assumed to be confined to one storey only. All windows or other similar openings in the fire compartment are assumed to be rectangular.
    2. The determination of the temperature of the compartment fire, the dimensions and temperatures of the flames projecting from the openings, and the radiation and convection parameters should be performed according to annex B of BS EN 1991-1-2:2002.
    3. A distinction should be made between members not engulfed in flame and members engulfed in flame, depending on their locations relative to the openings in the walls of the fire compartment.
    4. A member that is not engulfed in flame should be assumed to receive radiative heat transfer from all the openings in that side of the fire compartment and from the flames projecting from all these openings.
    5. A member that is engulfed in flame should be assumed to receive convective heat transfer from the engulfing flame, plus radiative heat transfer from the engulfing flame and from the fire compartment opening from which it projects. The radiative heat transfer from other flames and from other openings may be neglected.

.. include:: fd-col-engulfed.rst
.. include:: fd-col-not-engulfed.rst
.. include:: ufd-col-engulfed.rst
.. include:: ufd-col-not-engulfed.rst
