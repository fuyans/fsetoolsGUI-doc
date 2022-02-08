Column Engulfed in Flame (Forced Draught)
=========================================

The convention for geometrical data may be taken from the figure below.

.. figure:: fig-geometrical-data-convention.png
    :alt: Geometrical Data Convention

The following parameters should be given prior the assessment:

| :math:`\lambda_1` [:math:`m`] is the distance between side of the column and the window opening edge.
| :math:`\lambda_3` [:math:`m`] is the separation between the column and the window opening.
| :math:`d_1`       [:math:`m`] is the column dimension transverse to the wall.
| :math:`d_2`       [:math:`m`] is the column dimension longitudinal to the wall.
| :math:`C_i`       [:math:`1`] is the coefficient associated with protection.
| :math:`L_L`       [:math:`m`] is the external flame height.
| :math:`L_H`       [:math:`m`] is the external flame projection transverse to the wall.
| :math:`w_t`       [:math:`m`] is the window opening width.
| :math:`h_{eq}`    [:math:`m`] is the window opening height.
| :math:`T_f`       [:math:`K`] is the flame temperature at the window opening.

Column location parameter :math:`\lambda_2`
-------------------------------------------

:math:`\lambda_2` is given by:

.. math::
    \lambda_2=w_t-\lambda_1-d_2

Column location parameter :math:`\lambda_4`
-------------------------------------------

:math:`\lambda_4` is given by:

.. math::
    \lambda_4=\max
    \begin{Bmatrix}
    0\\
    \min
    \begin{Bmatrix}
    \frac{1}{2}h_{eq}\cdot \frac{L_H}{L_L}\\
    h_{eq}\frac{L_H}{L_L}-(\lambda_3+d_1)\\
    \end{Bmatrix}
    \end{Bmatrix}

Distance from the window to column along flame axis
---------------------------------------------------

The distance from the window to column along flame axis :math:`l` is given by:

.. math::
    l=L_x=\min
    \begin{Bmatrix}
    \left(\lambda_3+0.5d_1\right)\frac{L_L}{L_H}\\
    0.5h_{eq}\frac{L_L}{L_H}
    \end{Bmatrix}

*Equation B19.a and B.19b, Clause B.4(5)*

.. note::
    This is the same as :math:`L_x` in BS EN 1991-1-2:2002

Flame temperature column
------------------------

The flame temperature along the flame axis at the the column is given by:

.. math::
    T_z=\left(T_w-T_0\right)\left(1-0.4725\frac{L_x\cdot w_t}{Q}\right)+T_0

*Equation B.15, Clause B.4.1(10)*

The emissivity of the flames
----------------------------

The emissivity of the flames for each of the faces 1, 2, 3 and 4 of the column are:

.. math::
    \varepsilon_{z,i}=1-e^{-0.3\lambda_i}

*Equation XX, Clause B.4(2)*

The radiative heat flux from flames
-----------------------------------

The radiative heat flux from the flames for each of the faces 1, 2, 3 and 4 of the column are:

.. math::
    I_{z,i}=C_i\cdot \varepsilon_{z,i}\sigma \cdot T^4

*Equation XX, Clause B.4 (1)*

The radiative heat flux from an opening
---------------------------------------

The radiative heat flux from an opening for each of the faces 1, 2, 3, and 4 of the column are:

.. math::
    I_{f,i}=\phi_f\cdot\varepsilon_f\left(1-\varepsilon_{z,i}\right)\sigma\cdot T_f^4

*Equation XX, Clause B.1.3 (5)*

The convective heat transfer coefficient
----------------------------------------

The convective heat transfer coefficient :math:`\alpha` is given by:

.. math::
    \alpha_c=4.67\left(\frac{1}{d_{eq}}\right)^{0.4}\left(\frac{Q}{A_v}\right)^{0.6}

*Clause B.4.1 (12) in BS EN 1991-1-2:2002*

.. note::
    This is the same as :math:`α_c` in BS EN 1991-1-2 with unit :math:`\frac{W}{m^2\cdot K}`. This is converted to
    :math:`\frac{kW}{m^2\cdot K}` for this assessment.

Steel temperature at its four sides
-----------------------------------

The temperature of the steel member for each of its faces 1, 2, 3, and 4 can be calculated by solving the heat
balancing equation:

.. math::
    \sigma T_{m,i}^4+\alpha T_{m,i}=I_{z,i}+I_{f,i}+293\alpha

*Equation B.2 in Clause B.1.3(3)*

Radiative heat flux from flames
-------------------------------

The radiative heat flux :math:`I_z` from the flames should be determined from:

.. math::
    I_z=\frac{(I_{z,1}+I_{z,2})\cdot d_1+(I_{z,3}+I_{z,4})\cdot d_2}{(C_1+C_2)\cdot d_1+(C_3+C_4)\cdot d_2}

*Equation B.18, Clause B.4(1)*

Radiative heat flux from an opening
-----------------------------------

The radiative heat flux :math:`I_f` from an opening should be determined from:

.. math::
    I_f = \phi_f \cdot \varepsilon_f \left(1-a_z\right)\cdot \sigma \cdot T_f^4

*Equation B.3, Clause B.1.3(5)*

Average steel temperature
-------------------------

The average temperature of the steel member :math:`T_m` [:math:`K`] should be determined from the solution of the
following heat balance:

.. math::
    \sigma \cdot T_m^4 + \alpha \cdot T_m = I_z + I_f + \alpha \cdot T_z

*Equation B.2, B.1.3(3)*
