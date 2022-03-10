Eurocode 1 Parametric Fire
**************************

Introduction
============

.. important::
    1. It is assumed that the fire load of the compartment is completely burnt out.
    2. Compartment floor area :math:`A_f` should be less than 500 :math:`m^2`.
    3. Compartment should only have ventilation openings on walls. i.e., without openings in the roof or floor.
    4. Compartment height should be less than 4 :math:`m`.
    5. Opening factor should be within the range of :math:`0.02 \leq O\leq 0.2`.
    6. The total design fire load :math:`q_{t,d}` should be in the range of :math:`50\leq q_{t,d} \leq 1000`.

If fire load densities are specified without specific consideration to the combustion behaviour (see Annex E), then
this approach should be limited to fire compartments with mainly cellulosic type fire loads.

The temperature-time curves in the heating phase are given by:

.. math::
    \Theta_g=\begin{cases}
    20+1325 \left(1-0.324e^{-0.2t^*}-0.204e^{-1.7t^*}-0.472e^{-19t^*}\right) &\text{if } t^*\le t_{max}^*\\
    625\left(t^*-t_{max}^*.x\right) &\text{if } t^* > t_{max}^* \text{ and } t_{max}^* \leq 0.5\\
    \Theta_{max}-250\left(3-t_{max}^*\right)\left(t^*-t_{max}^*\cdot x\right) &\text{if } t^* > t_{max}^* \text{ and } 0.5 < t_{max}^* < 2\\
    \Theta_{max}-250\left(t^*-t_{max}^*\cdot x\right) &\text{if } t^* > t_{max}^* \text{ and } t_{max}^* \geq 2\\
    \end{cases}
    :label: en1-2-b-Theta_g

Where

    | :math:`\Theta_g`  [:math:`^oC`], is the gas temperature in the fire compartment.
    | :math:`t^*`       [:math:`h`], see Eq. :eq:`en1-1-2-a-t_star`
    | :math:`t_{max}^*` [:math:`h`], see Eq. :eq:`en1-1-2-a-t_star_max`

.. math::
    t^* = \begin{cases}
    t\cdot \Gamma &\text{when } t_{max}<t_{lim}\\
    t\cdot \Gamma_{lim} &\text{when }t_{max}=t_{lim}
    \end{cases}
    :label: en1-1-2-a-t_star

.. math::
    t_{max}^* = (0.2\cdot 10^{-3}\cdot q_{t,d} /O)\cdot \Gamma
    :label: en1-1-2-a-t_star_max


Where

    | :math:`t`  [:math:`h`], time


.. math::
    O=A_v \frac{\sqrt{h_eq}}{A_t}
    :label: en1-2-b-O

Where
    | :math:`A_v`  [:math:`m^2`], total area of vertical openings on all walls
    | :math:`h_eq`  [:math:`m`], weighted average of window height on all walls
    | :math:`A_t`  [:math:`m^2`], total area of enclosure (Walls, ceiling and floor, including openings)

.. math::
    \Gamma= [O/b]^2/(0.04/1160)^2
    :label: en1-2-b-Gamma

Where
    | :math:`b=\sqrt{\rho c \lambda}`
    | :math:`\rho`  [:math:`kg/m^3`], the density of the boundary enclosure
    | :math:`c`  [:math:`J/kg/K`], specific heat of boundary of enclosure
    | :math:`\lambda`  [:math:`W/m/K`], thermal conductivity of boundary of enclosure

.. note::
    In case of :math:`\Gamma=1`, equation :eq:`en1-2-b-Theta_g` approximates the standard temperature-time curve.

.. hint::
    For the calculation of the :math:`b` factor, the density :math:`\rho`, the specific heat :math:`c` and the thermal
    conductivity :math:`\lambda` of the boundary may be taken at ambient temperature.

The maximum temperature :math:`\Theta_{max}` in the heating phase happens for :math:`t^*=t_{max}^*`.

.. math::
    t_{max}^*=t_{max}\cdot \Gamma
    :label: en1-2-b-t_max_star

with :math:`\begin{split}t_{max}=\max\begin{Bmatrix}\frac{0.2\cdot10^{-3}\cdot q_{t,d}}{O}\\t_{lim}\end{Bmatrix}\end{split}`

where
    | :math:`q_{t,d}`  [math:`a`], is the design value of the fire load density related to the total surface area. See :eq:`en1-2-b-q_t_d`
    | :math:`t_{lim}`  [math:`h`], is given by :eq:`en1-2-t_lim`

.. math::
    q_{t,d}=q_{f,d}\frac{A_f}{A_t}

where
    | :math:`q_{f,d}`  [:math:`MJ/m^2`], is the design fire load density associated with the floor.



.. note::
    The limit :math:`t_{max}` corresponding to the maximum temperature is given by :math:`t_{lim}` in case the fire is 
    fuel controlled. If :math:`t_{lim}` is given by :math:`0.2\cdot 10^{-3}\cdot q_{t,d} / O`, the fire is ventilation 
    controlled.

When :math:`t_{max}=t_{lim}`, :math:`t^*` used in equation :eq:`en1-2-theta_g` is replaced by:

.. math::
    \Gamma_{lim}=\begin{cases}
    k\cdot \left(\frac{O_{lim}/b}{0.04/1160}\right)^2 &\text{if }O>0.04 \text{ and } q_{t,d}<75 \text{ and } b<1160\\
    \left(\frac{O_{lim}/b}{0.04/1160}\right)^2 &\text{for other cases}\\
    \end{cases}

with :math:`O_{lim} = 0.1\cdot 10^{-3}\cdot q_{t,d} / t_{lim}`

with :math:`k=1+\frac{O-0.04}{0.04}\cdot \frac{q_{t,d}-75}{75}\cdot \frac{1160-b}{1160}`

.. math::
    t_{lim}=\begin{cases}
    25 min &\text{slow fire growth rate}\\
    20 min &\text{medium fire growth rate}\\
    15 min &\text{fast fire growth rate}\\
    \end{cases}


.. list-table:: Fire growth rate and heat release rate per unit area for different occupancies
    :header-rows: 1

    * - Occupancy
      - Fire growth rate
      - t_alpha [s]
      - RHR_f [kW/m²]
    * - Dwelling
      - Medium
      - 300
      - 250
    * - Hospital (room)
      - Medium
      - 300
      - 250
    * - Hotel (room)
      - Medium
      - 300
      - 250
    * - Library
      - Fast
      - 150
      - 500
    * - Office
      - Medium
      - 300
      - 250
    * - School classroom
      - Medium
      - 300
      - 250
    * - Shopping centre
      - Fast
      - 150
      - 250
    * - Theatre (cinema)
      - Fast
      - 150
      - 500
    * - Transport (public space)
      - Slow
      - 600
      - 250

