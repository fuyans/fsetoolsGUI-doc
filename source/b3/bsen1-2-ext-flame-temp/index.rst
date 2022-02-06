Eurocode 1 Thermal Actions for External Members
***********************************************

Introduction
============

This method allows the determination of:

* the maximum temperatures of a compartment fire;
* the size and temperatures of the flame from openings;
* radiation and convection parameters.

.. important::
    1. This method considers steady-state conditions for the various parameters.
    2. The method is valid only for fire loads :math:`q_{f,d}` higher than 200 :math:`MJ/m^2`.
    3. All parts of an external wall that do not have the fire resistance (REI) required for the stability of the building should be classified as window areas.
    4. The size of the fire compartment should not exceed 70 m in length, 18 m in width and 5 m in height.
    5. The flame temperature should be taken as uniform across the width and the thickness of the flame.
    6. Clause B.3 considers wind effects which is currently NOT included in this document.

.. _fig-fire_compartment:

.. figure:: fig-fire_compartment.png
    :alt: Fire Compartment Figure

    Illustration of a fire compartment with vertical window opening and optional core


Where
    | :math:`W_1`           [:math:`m`], is the wall with greatest window opening area.
    | :math:`W_2`           [:math:`m`], is the wall with lesser window opening area as compared to :math:`W_2`.
    | :math:`A_{v1}`        [:math:`m^2`], is the total window opening area on :math:`W_1`. :math:`A_{v1}=A_v` if window only exist on :math:`W_1`.
    | :math:`A_{v}`         [:math:`m^2`], is the total window opening area on all walls.
    | :math:`W_c`           [:math:`m`], is the width of core. Set to 0 if no core is present.
    | :math:`L_c`           [:math:`m`], is the depth of core. Set to 0 if no core is present.
    | :math:`w_t`           [:math:`m`], is the sum of window widths (:math:`w_t=\sum_{i=1}^{\text{tot. win.}}{w_i}`).
    | :math:`h_{eq}`        [:math:`m`], is weighted average height of all windows.
    | :math:`S_w`           [:math:`m`], is the separation between windows.
    | :math:`\mathrm{B}_w`  [:math:`1`], :math:`\mathrm{B}_w=True` means there is wall above the window, otherwise :math:`\mathrm{B}_w=False`.

Opening factor
--------------

Opening factor of the fire compartment is given by Equation :eq:`en1-b-O` (Clause 1.6(1)).

.. math:: O=\frac{A_v\sqrt{h_{eq}}}{A_t}
    :label: en1-b-O

where
    | :math:`O` [:math:`m^{0.5}`], is the opening factor of the fire compartment.
    | :math:`A_v` [:math:`m^2`], is the total area of vertical openings on all walls.
    | :math:`A_t` [:math:`m^2`], is the total area of enclosure (walls, ceiling and floor, including openings).

Compartment :math:`D/W`
-----------------------

The compartment and opening arrangement is partly described by the :math:`D/W` is given by Equation :eq:`D/W` (Clause B.2, BS EN 1991-1-2:2002).

.. math:: D/W=\frac{W_2-L_c}{W_1-W_c}\frac{A_{v1}}{A_v}
    :label: D/W

No Forced Draught (NFD)
=======================

Heat release rate (NFD)
-----------------------

The rate of burning or the rate of heat release is given by Equation :eq:`en1-b4.1-Q` (Clause B.4.1(1), Equation B.4).

.. math::
    Q=\min\begin{Bmatrix}
    \frac{A_f\cdot q_{f,d}}{\tau_F}\\
    3.15\left(1-e^\frac{-0.036}{O}\right)A_v\sqrt{\frac{h_{eq}}{D/W}}
    \end{Bmatrix}
    :label: en1-b4.1-Q

Where
    | :math:`Q`         [:math:`MW`], is the rate of heat release.
    | :math:`A_f`       [:math:`m^2`], is the compartment floor area.
    | :math:`q_{td}`    [:math:`MJ/m^2`], is the design fuel load density.
    | :math:`\tau_F`    [:math:`s`], is the free burning fire duration (assumed to be 1200 [:math:`s`]).
    | :math:`O`         [:math:`?`], is the opening factor as per Equation :eq:`en1-b-O`.

Flame height (NFD)
------------------

The flame height is given by Equation :eq:`en1-b4.1-L_L` (Clause B.4.1(3), Equation B.6).

.. math::
    L_L = \max
    \begin{Bmatrix}
    0\\
    h_{eq}\left(2.37\left(\frac{Q}{A_v\rho_g\sqrt{h_{eq}g}}\right)^{2/3}-1\right)
    \end{Bmatrix}
    :label: en1-b4.1-L_L

Where
    | :math:`L_L`       [:math:`m`], is the flame height.
    | :math:`\rho_g`    [:math:`kg/m^3`], is the air density.
    | :math:`g`         [:math:`m/s^2`], is the gravity.

.. note::
    With :math:`\rho_g=0.45kg/m^3` and :math:`g=9.81m/s^2`, Equation :eq:`en1-b4.1-L_L` may be simplified to :math:`L_L =\left(1.9\frac{Q}{w_t}\right)^{2/3}-h_{eq}`

Flame horizontal projection (NFD)
---------------------------------

The horizontal projection of the flame is given by Equation :eq:`en1-b4.1-L_H` (Clause 4.1(6), Equation B.8 to B.11).

.. math::
    L_H=
    \begin{cases}
    & \text{if }\mathrm{B}_w\text{ and }h_{eq}\le1.25w_t &1/3\cdot h_{eq}\\
    & \text{else if }\mathrm{B}_w\text{ and }h_{eq}>1.25w_t\text{ and }S_w>4w_t &0.3h_{eq}\left(\frac{h_{eq}}{w_t}\right)^{0.54}\\
    & \text{else if }\mathrm{B}_w &0.454h_{eq}\left(\frac{h_{eq}}{2w_t}\right)^{0.54}\\
    & \text{else if }\mathrm{B}_w=False &0.6h_{eq}\left(\frac{L_L}{h_{eq}}\right)^{1/3}
    \end{cases}
    :label: en1-b4.1-L_H

Where
    | :math:`L_H` [:math:`m`], is the horizontal projection of the external flame.

Flame length (NFD)
------------------

The flame length along axis is given by Equation :eq:`en1-b4.1-L_f` (Clause B.4.1(7), Equation B.12 & B.13).

.. math::
    L_f=
    \begin{cases}
    &\text{if }\mathrm{B}_w\text{ and }h_{eq}\le1.25w_t &L_L+0.5h_{eq}\\
    &\text{else }&\sqrt{L_L^2+\left(L_H=h_{eq}/3\right)^2}+0.5h_{eq}
    \end{cases}
    :label: en1-b4.1-L_f

Where
    | :math:`L_f` [:math:`m`], is the flame length along axis.

Flame temperature at the window (NFD)
-------------------------------------

The flame temperature at the window is given by Equation :eq:`en1-b4.1-T_w` (Clause B.4.1(8), Equation B.14).

.. math:: T_w=\frac{520}{1-0.4725L_f\cdot w_t/Q}+T_0
    :label: en1-b4.1-T_w

Where
    | :math:`T_w` [:math:`K`], is the flame temperature at the window.
    | :math:`T_0` [:math:`K`], is the ambient temperature.

Flame temperature along the axis (NFD)
--------------------------------------

The flame temperature along the axis is given by Equation :eq:`en1-b4.1-T_z` (Clause B.4.1(10), Equation B.15).

.. math:: T_z=\left(T_w-T_0\right)\left(1-0.4725\frac{L_x\cdot w_t}{Q}\right)+T_0
    :label: en1-b4.1-T_z

Where
    | :math:`T_z` [:math:`K`], is the flame temperature along the axis at :math:`L_x`.
    | :math:`L_x` [:math:`m`], is the axis length from the window to the point where the calculation is made.

The following parameters are not used to derive the external flame dimension and temperature (e.g. :math:`L_H`, :math:`L_L` and :math:`T_z` etc.) but are may be used for other purposes (e.g., to derive external steel temperature).

Compartment temperature (NFD)
-----------------------------

The temperature of the fire compartment is given by Equation :eq:`en1-b4.1-T_f` (Clause B.4.1(2), Equation B.5).

.. math:: T_f=6000\left(1-e^{-0.1/O}\right)O^{-1/2}\left(1-e^{-0.00286\Omega}\right)+T_0
    :label: en1-b4.1-T_f

Where
    | :math:`T_f` [:math:`K`], is the temperature of the fire compartment.

Forced Draught (FD)
===================

Heat release rate (FD)
----------------------

The rate of burning or the rate of heat release is given by Equation :eq:`en1-b4.2-Q` (Clause B.4.2(1), Equation B.18).

.. math:: Q=\frac{A_f\cdot q_{f,d}}{\tau_F}
    :label: en1-b4.2-Q

Where
    | :math:`Q` [:math:`MW`], is the rate of heat release.
    | :math:`\tau_F`    [:math:`s`], is the free burning fire duration (assumed to be 1200 [:math:`s`]).

Fire compartment temperature (FD)
---------------------------------

The temperature of the fire compartment is given by Equation :eq:`en1-b4.2-T_f` (Clause B.4.2(2), Equation B.19).

.. math:: T_f=1200\left(1-e^{-0.00228\Omega}\right)+T_0
    :label: en1-b4.2-T_f

Where
    | :math:`T_f` [:math:`K`], is the temperature of the fire compartment.

Flame height (FD)
-----------------

The flame height is given by Equation :eq:`en1-b4.2-L_L` (Clause B.4.2(3), Equation B.20).

.. math:: L_L=\left(1366\left(\frac{1}{u}\right)^{0.43}\frac{Q}{\sqrt{A_f}}\right)-h_{eq}
    :label: en1-b4.2-L_L

Where
    | :math:`L_L` [:math:`m`], is the flame height.

Flame horizontal projection (FD)
--------------------------------

The horizontal projection of flames is given by Equation :eq:`en1-b4.2-L_H` (Clause B.4.2(4), Equation B.21).

.. math:: L_H=0.605\left(\frac{u^2}{h_{eq}}\right)^{0.22}\left(L_L+h_{eq}\right)
    :label: en1-b4.2-L_H

Where
    | :math:`L_H` [:math:`m`], is the horizontal projection of flame.

.. note::
    With :math:`u=6m/s`, :math:`L_H=1.33\left(L_L+h_{eq}\right)/h_{eq}^{0.22}`


Flame width (FD)
----------------

The flame width is given by Equation :eq:`en1-b4.2-w_f` (Clause B.4.2(5), Equation B.22).

.. math:: w_f=w_t+0.4L_H
    :label: en1-b4.2-w_f

Where
    | :math:`w_f` [:math:`m`], is the flame width.

Flame length (FD)
-----------------

The flame length along axis is given by Equation :eq:`en1-b4.2-L_f` (Clause B.4.2(6), Equation B.23).

.. math:: L_f=\sqrt{L_L^2+L_H^2}
    :label: en1-b4.2-L_f

Where
    | :math:`L_f` [:math:`m`], is the flame length along axis.

Flame temperature at the window (FD)
------------------------------------

The flame temperature at the window is given by Equation :eq:`en1-b4.2-T_w` (Clause B.4.2(7), Equation B.24).

.. math:: T_w=\frac{520}{1-0.3325L_f\frac{\sqrt{A_v}}{Q}}+T_0
    :label: en1-b4.2-T_w

Where
    | :math:`T_w` [:math:`K`], is the flame temperature at the window.

.. warning::
    :math:`L_f\sqrt{A_v}/Q<1`.

Flame temperature along the axis (FD)
-------------------------------------

The flame temperature along the axis is given by Equation :eq:`en1-b4.2-T_z` (Clause B.4.2(9), Equation B.25).

.. math:: T_z=\left(1-0.3325\frac{L_x\sqrt{A_v}}{Q}\right)\left(T_w-T_0s\right)+T_0
    :label: en1-b4.2-T_z

Where
    | :math:`T_z` [:math:`K`], is the flame temperature along the axis.
    | :math:`L_x` [:math:`m`], is the axis length from the window to the point where the calculation is made.

Miscellaneous
=============

Flame emissivity
----------------

The emissivity of flame is given by Equation :eq:`en1-b4.1-epsilon_f` (Clause B.4.1(11), Equation B.16).


.. math:: \varepsilon_f=1-e^{-0.3d_f}
    :label: en1-b4.1-epsilon_f

Where
    | :math:`\varepsilon_f` [:math:`1`], is the emissivity of flames.

Convective heat transfer coefficient
------------------------------------

The convective heat transfer coefficient is given by Equation :eq:`en1-b4.1-alpha_c` (Clause B.4.1(12), Equation B.17).

.. math:: \alpha_c=4.67\left(1/d_{eq}\right)^{0.4}\left(Q/A_v\right)^{0.6}
    :label: en1-b4.1-alpha_c

Where
    | :math:`\alpha_c` [:math:`1`], is the convective heat transfer coefficient of the flame.

Overall Configuration Factors
=============================

Radiative heat transfer from an opening
---------------------------------------

The overall configuration factor :math:`\phi_f`, of a member for radiative heat transfer from an opening should be determined from Equation :eq:`en1-b5-phi_f` (Clause B5(1), Equation B.28).

.. math:: \phi_f=\frac{\left(C_1\phi_{f,1}+C_2\phi_{f,2}\right)d_1+\left(C_3\phi_{f,3}+C_4\phi_{f,4}\right)d_2}{\left(C_1+C_2\right)d_1+\left(C_3+C_4\right)d_2}
    :label: en1-b5-phi_f

Where
    | :math:`\phi_{f,i}`    [:math:`1`], is the configuration factor of member face i for that **opening**.
    | :math:`d_i`           [:math:`1`], is the cross-sectional dimension of member face :math:`i`.
    | :math:`C_i`           [:math:`1`], is the protection coefficient of member face :math:`i` as follows:
    |   for a protected face: :math:`C_i=0`.
    |   for an unprotected face: :math:`C_i=1`.

The configuration factor :math:`\phi_{f,i}`, for a member face from which the opening is not visible should be taken as zero.

Radiative heat transfer from a flame
------------------------------------

The overall configuration factor :math:`\phi_z` of a member for radiative heat transfer from a flame should be determined from Equation :eq:`en1-b5-phi_z` (Clause B5(3), Equation B.29).

.. math:: \phi_z=\frac{\left(C_1\phi_{z,1}+C_2\phi_{z,2}\right)d_1+\left(C_3\phi_{z,3}+C_4\phi_{z,4}\right)d_2}{\left(C_1+C_2\right)d_1+\left(C_3+C_4\right)d_2}
    :label: en1-b5-phi_z

Where
    | :math:`\phi_{z,i}` [:math:`1`], is the configuration factor of member face i for that **flame**.

The configuration factors :math:`\phi_{z,i}` of individual member faces for radiative heat transfer from flames may be based on equivalent rectangular flame dimensions. The dimensions and locations of equivalent rectangles representing the front and sides of a flame for this purpose should be determined as given in annex G. For all other purposes, the flame dimensions given in B.4 of this annex should be used.
