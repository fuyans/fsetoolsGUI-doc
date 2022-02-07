Eurocode 3 Heat Transfer to External Steelwork
**********************************************

.. warning::
    Work in progress

B.1.2(1), Equation B.1

.. math::
    \sigma T_m^4+\alpha T_m=\sum_{i=1}^4I_{z,i}+\sum_{i=1}^4I_{f,i}+293\alpha

Forced Draught (FD)
===================

Column not engulfed in flame (FD)
=================================

Beam not engulfed in flame (FD)
===============================

Column engulfed in flame (FD)
=============================

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

:math:`\lambda_2` is given by Equation :eq:`bsen3-1-2-b.4-fd_lbd_2`.

.. math::
    \lambda_2=w_t-\lambda_1-d_2
    :label: bsen3-1-2-b.4-fd_lbd_2

:math:`\lambda_4` is given by Equation :eq:`bsen3-1-2-b.4-fd_lbd_4`.

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
    :label: bsen3-1-2-b.4-fd_lbd_4

The axial distance between the column and window opening is given by Equation
:eq:`bsen3-1-2-b.4-fd_l`. This is used to calculate the flame temperature
at the window opening :math:`T_z`. *B.4(5)*.

.. math::
    l=L_x=\min
    \begin{Bmatrix}
    \frac{\left(\lambda_3+0.5d_1\right)L_L}{L_H}\\
    \frac{0.5h_{eq}\cdot L_L}{L_H}
    \end{Bmatrix}
    :label: bsen3-1-2-b.4-fd_l

(BS EN 1991-1-2:2001 B.4.1(10), B.15) The flame temperature along the flame axis at
the centroid of the column section is given by Equation :eq:`bsen3-1-2-b.4-fd_T_z`.

.. math::
    T_z=\left(T_w-T_0\right)\left(1-0.4725\frac{L_x\cdot w_t}{Q}\right)+T_0
    :label: bsen3-1-2-b.4-fd_T_z

B.4(2), ??,  the emissivity of the flames for each of the faces 1, 2, 3 and 4 of the column are:

.. math::
    \varepsilon_{z,i}=1-e^{-0.3\lambda_i}
    :label: bsen3-1-2-b.4-fd_epsilon_z_i

Clause B.4 (1), the radiative heat flux from the flames for each of the faces 1, 2, 3 and 4 of the column are:

.. math::
    I_{z,i}=C_i\cdot \varepsilon_{z,i}\sigma \cdot T^4
    :label: bsen3-1-2-b.4-fd_I_z_i

Clause B.1.3 (5), the radiative heat flux from an opening for each of the faces 1, 2, 3, and 4 of the column are

.. math::
    I_{f,i}=\phi_f\cdot\varepsilon_f\left(1-\varepsilon_{z,i}\right)\sigma\cdot T_f^4
    :label: bsen3-1-2-b.4-fd_I_f_i

BS EN 1991-1-2 Clause B.4.1 (12), the convective heat transfer coefficientα(αcWm2·Kin BS EN 1991-1-2,
this is converted tokWm2·Kat later parts of this assessment) is

.. math::
    \alpha_c=4.67\left(\frac{1}{d_{eq}}\right)^{0.4}\left(\frac{Q}{A_v}\right)^{0.6}
    :label: bsen3-1-2-b.4-fd_alpha_c

Clause B.1.3 (3), the temperature of the steel member for each of its faces 1, 2, 3, and 4 are:

.. math::
    \sigma T_{m,i}^4+\alpha T_{m,i}=I_{z,i}+I_{f,i}+293\alpha
    :label: bsen3-1-2-b.4-fd_T_m_i

4(1), Equation B.18

.. math::
    I_z=\frac{(I_{z,1}+I_{z,2})\cdot d_1+(I_{z,3}+I_{z,4})\cdot d_2}{(C_1+C_2)\cdot d_1+(C_3+C_4)\cdot d_2}

Beam fully or partially engulfed in flame (FD)
==============================================
